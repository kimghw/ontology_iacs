#!/bin/bash
# Simplified PDF to Markdown converter for a single file

MODEL="gemini-2.5-flash"
LOG_FILE="/mnt/d/OneDrive - 한국선급/업무/(2) ontology/iacs/UR/conversion_log.txt"
ERROR_LOG="/mnt/d/OneDrive - 한국선급/업무/(2) ontology/iacs/UR/conversion_errors.txt"

# Check if a PDF file path is provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <path_to_pdf_file>"
    exit 1
fi

pdf_path="$1"
dir=$(dirname "$pdf_path")
basename=$(basename "$pdf_path" .pdf)
md_path="${dir}/${basename}.md"

# Clear logs for a single run
> "$LOG_FILE"
> "$ERROR_LOG"

echo "$(date '+%Y-%m-%d %H:%M:%S') Starting conversion for: $pdf_path" | tee -a "$LOG_FILE"

# Retry up to 3 times with exponential backoff
max_retries=3
retry=0
result=""
exit_code=1

while [ $retry -lt $max_retries ]; do
    result=$(gemini -m "$MODEL" -p "Read this PDF file and convert its entire content to well-formatted Markdown. Preserve all text, tables, headings, lists, and structure faithfully. Output ONLY the markdown content, no explanations or commentary. File: \"$pdf_path\"" --yolo 2>/dev/null)
    exit_code=$?

    if [ $exit_code -eq 0 ] && [ -n "$result" ]; then
        break
    fi

    retry=$((retry + 1))
    if [ $retry -lt $max_retries ]; then
        backoff=$((retry * 10))
        echo "[RETRY] $pdf_path attempt $((retry+1))/$max_retries (waiting ${backoff}s)" >> "$LOG_FILE"
        sleep $backoff
    fi
done

if [ $exit_code -eq 0 ] && [ -n "$result" ]; then
    echo "$result" > "$md_path"
    echo "$(date '+%H:%M:%S') [OK] $(basename "$pdf_path") converted to $md_path" | tee -a "$LOG_FILE"
    echo "$result" # Output the markdown content to stdout
else
    echo "$(date '+%H:%M:%S') [ERROR] Failed to convert: $pdf_path (exit: $exit_code, retries: $retry)" >> "$ERROR_LOG"
    echo "Error: Failed to convert $pdf_path. Check $ERROR_LOG for details."
    exit 1
fi
