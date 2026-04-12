import sys, re, json, glob, os
import language_tool_python

EXCLUDE_RULES = {"BRITISH_ENGLISH_DETECTOR"}
AUTO_CATS = {"TYPOS", "MISSPELLING"}

def clean(text):
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
    text = re.sub(r'\$\$.*?\$\$', '', text, flags=re.DOTALL)
    text = re.sub(r'\$[^$\n]+\$', '', text)
    return text

def lang_of(text):
    total = max(1, sum(1 for c in text if c.isalpha() or '\uac00' <= c <= '\ud7a3'))
    ko = sum(1 for c in text if '\uac00' <= c <= '\ud7a3')
    return ko / total

manual_review = []
auto_fixed = []
tool_en = language_tool_python.LanguageTool("en-US")
try:
    tool_ko = language_tool_python.LanguageTool("ko-KR")
except Exception:
    tool_ko = None

files = sorted(glob.glob(sys.argv[1]))
for fp in files:
    name = os.path.basename(fp)
    with open(fp, encoding="utf-8") as fh:
        raw = fh.read()
    text = clean(raw)
    kr = lang_of(text)
    tools = []
    if kr >= 0.3 and tool_ko: tools.append(("ko", tool_ko))
    if kr < 1.0: tools.append(("en", tool_en))
    for lbl, tool in tools:
        matches = tool.check(text)
        for m in matches:
            if m.rule_id in EXCLUDE_RULES: continue
            entry = {
                "file": name, "lang": lbl, "rule": m.rule_id, "cat": m.category,
                "msg": m.message, "ctx": m.context,
                "offset": m.offset, "length": m.error_length,
                "repl": m.replacements[:5],
            }
            manual_review.append(entry)

with open(sys.argv[2], "w", encoding="utf-8") as fh:
    json.dump({"auto_fixed": auto_fixed, "manual_review": manual_review}, fh, ensure_ascii=False, indent=2)
print(f"manual_review={len(manual_review)}")
