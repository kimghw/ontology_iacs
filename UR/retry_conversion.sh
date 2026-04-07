#!/bin/bash
# Retry failed PDF to Markdown conversions
# Smaller batch size to avoid rate limits

BATCH_SIZE=5
STAGGER_DELAY=5
MODEL="gemini-2.5-flash"
FAILED_LIST="/home/kimghw/iacs/UR/failed_files.txt"
LOG_FILE="/home/kimghw/iacs/UR/retry_log.txt"
ERROR_LOG="/home/kimghw/iacs/UR/retry_errors.txt"
PROGRESS_FILE="/home/kimghw/iacs/UR/retry_progress.txt"

> "$LOG_FILE"
> "$ERROR_LOG"
> "$PROGRESS_FILE"

mapfile -t PDF_FILES < "$FAILED_LIST"
TOTAL=${#PDF_FILES[@]}
echo "$(date '+%Y-%m-%d %H:%M:%S') Retrying $TOTAL failed files" | tee -a "$LOG_FILE"

convert_pdf() {
    local pdf_path="$1"
    local dir=$(dirname "$pdf_path")
    local basename=$(basename "$pdf_path" .pdf)
    local md_path="${dir}/${basename}.md"

    if [ -f "$md_path" ] && [ -s "$md_path" ]; then
        echo "SKIP: $pdf_path" >> "$PROGRESS_FILE"
        return 0
    fi

    local max_retries=5
    local retry=0
    local result=""
    local exit_code=1

    while [ $retry -lt $max_retries ]; do
        result=$(gemini -m "$MODEL" -p "Read this PDF file and convert its entire content to well-formatted Markdown. Preserve all text, tables, headings, lists, and structure faithfully. Output ONLY the markdown content, no explanations or commentary. File: $pdf_path" --yolo 2>/dev/null)
        exit_code=$?

        if [ $exit_code -eq 0 ] && [ -n "$result" ]; then
            break
        fi

        retry=$((retry + 1))
        if [ $retry -lt $max_retries ]; then
            local backoff=$((retry * 15))
            echo "[RETRY] $(basename "$pdf_path") attempt $((retry+1))/$max_retries (waiting ${backoff}s)" >> "$LOG_FILE"
            sleep $backoff
        fi
    done

    if [ $exit_code -eq 0 ] && [ -n "$result" ]; then
        echo "$result" > "$md_path"
        echo "$(date '+%H:%M:%S') [OK] $(basename "$pdf_path")" | tee -a "$LOG_FILE"
        echo "OK: $pdf_path" >> "$PROGRESS_FILE"
    else
        echo "$(date '+%H:%M:%S') [ERROR] $(basename "$pdf_path")" >> "$ERROR_LOG"
        echo "ERROR: $pdf_path" >> "$PROGRESS_FILE"
    fi
}

export -f convert_pdf
export LOG_FILE ERROR_LOG PROGRESS_FILE MODEL

completed=0
batch_num=0

while [ $completed -lt $TOTAL ]; do
    batch_num=$((batch_num + 1))
    batch_end=$((completed + BATCH_SIZE))
    if [ $batch_end -gt $TOTAL ]; then
        batch_end=$TOTAL
    fi

    echo "$(date '+%H:%M:%S') === Batch $batch_num: $((completed+1))-$batch_end of $TOTAL ===" | tee -a "$LOG_FILE"

    pids=()
    for ((i=completed; i<batch_end; i++)); do
        convert_pdf "${PDF_FILES[$i]}" &
        pids+=($!)
        sleep $STAGGER_DELAY
    done

    for pid in "${pids[@]}"; do
        wait "$pid" 2>/dev/null
    done

    completed=$batch_end

    ok_count=$(grep -c "^OK:" "$PROGRESS_FILE" 2>/dev/null || echo 0)
    err_count=$(grep -c "^ERROR:" "$PROGRESS_FILE" 2>/dev/null || echo 0)
    echo "$(date '+%H:%M:%S') Progress: $completed/$TOTAL (OK: $ok_count, ERROR: $err_count)" | tee -a "$LOG_FILE"

    if [ $completed -lt $TOTAL ]; then
        echo "Waiting 10s before next batch..." | tee -a "$LOG_FILE"
        sleep 10
    fi
done

echo "" | tee -a "$LOG_FILE"
echo "=== RETRY COMPLETE $(date '+%Y-%m-%d %H:%M:%S') ===" | tee -a "$LOG_FILE"
echo "Total: $TOTAL" | tee -a "$LOG_FILE"
echo "Success: $(grep -c '^OK:' "$PROGRESS_FILE" 2>/dev/null || echo 0)" | tee -a "$LOG_FILE"
echo "Errors: $(grep -c '^ERROR:' "$PROGRESS_FILE" 2>/dev/null || echo 0)" | tee -a "$LOG_FILE"
