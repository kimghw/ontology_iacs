#!/usr/bin/env python3
"""UserPromptSubmit hook: append user prompt to memory_query.md with timestamp."""
import sys
import json
import datetime
from pathlib import Path

LOG_FILE = Path("/home/kimghw/ontology_iacs/user_query.md")

try:
    data = json.load(sys.stdin)
    prompt = data.get("prompt", "").strip()
    if not prompt:
        sys.exit(0)
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"\n## {ts}\n\n{prompt}\n"
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(entry)
except Exception:
    pass
sys.exit(0)
