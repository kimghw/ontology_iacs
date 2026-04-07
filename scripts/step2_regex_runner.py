#!/usr/bin/env python3
"""
Step 2 Regex Runner — Executes regex spec against canonical input.
Produces full match set for Pass 2-4.
"""
import re, json, sys, os

def load_regex_spec(spec_path):
    with open(spec_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def run_regex(input_path, spec):
    """Run regex patterns against input file, return full match set."""
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    flag_map = {
        'IGNORECASE': re.IGNORECASE,
        'MULTILINE': re.MULTILINE,
    }

    # Compile patterns
    compiled = []
    for idx, entry in enumerate(spec):
        flags = 0
        for flag_name in entry.get('flags', []):
            flags |= flag_map.get(flag_name, 0)
        try:
            pattern = re.compile(entry['pattern'], flags)
            compiled.append((idx, pattern, entry))
        except re.error as e:
            print(f"WARNING: Pattern {idx} compile error: {e}", file=sys.stderr)
            compiled.append((idx, None, entry))

    # Scan all lines
    matches = []
    for line_no, line in enumerate(lines, 1):
        line_stripped = line.rstrip('\n')
        candidates = []
        for idx, pattern, entry in compiled:
            if pattern is None:
                continue
            m = pattern.match(line_stripped)
            if m:
                candidates.append({
                    'line': line_no,
                    'pattern_index': idx,
                    'priority': entry.get('priority', 999),
                    'match_len': m.end() - m.start(),
                    'expected_level': entry.get('expected_level', ''),
                    'number_group': entry.get('number_group'),
                    'text_group': entry.get('text_group'),
                    'match_obj': m,
                    'matched_text': line_stripped,
                })

        if candidates:
            # Multi-match resolution: lowest priority value wins, then longest, then array order
            candidates.sort(key=lambda c: (c['priority'], -c['match_len'], c['pattern_index']))
            best = candidates[0]
            
            # Extract number and text from named groups
            heading_number = ''
            heading_text = ''
            if best['number_group']:
                try:
                    heading_number = best['match_obj'].group(best['number_group']) or ''
                except (IndexError, re.error):
                    pass
            if best['text_group']:
                try:
                    heading_text = best['match_obj'].group(best['text_group']) or ''
                except (IndexError, re.error):
                    pass

            matches.append({
                'line': best['line'],
                'matched_pattern_index': best['pattern_index'],
                'expected_level': best['expected_level'],
                'heading_number': heading_number,
                'heading_text': heading_text.strip(),
                'matched_text': best['matched_text'],
            })

    return matches, len(lines)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: step2_regex_runner.py <input_file> <regex_spec.json> [output.json]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    spec_file = sys.argv[2]
    output_file = sys.argv[3] if len(sys.argv) > 3 else None

    spec = load_regex_spec(spec_file)
    matches, total_lines = run_regex(input_file, spec)

    result = {
        'input_file': input_file,
        'spec_file': spec_file,
        'total_lines': total_lines,
        'match_count': len(matches),
        'matches': matches,
    }

    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
    else:
        print(json.dumps(result, indent=2, ensure_ascii=False))
