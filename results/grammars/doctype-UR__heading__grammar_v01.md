# IACS UR Heading Grammar v01

> **DocType:** UR (Unified Requirements)
> **Authority:** IACS
> **Source Family:** IACS UR/UI/Rec/PR
> **Version:** v01
> **Created:** 2026-04-07

## Heading Hierarchy

```
DocumentRoot (UR {letter}{number})
  └─ Section (# {letter}{number} ...)           Depth=1
       └─ Subsection (## {letter}{number}.{N} ...)   Depth=2
            └─ Paragraph (### {letter}{number}.{N}.{N} ...)   Depth=3
                 └─ Sub-paragraph (#### {letter}{number}.{N}.{N}.{N} ...)   Depth=4
                      └─ Sub-sub-paragraph (##### ...)   Depth=5
```

## Numbering Schemes

| Level | Pattern | Examples |
|:---|:---|:---|
| Section | `{Letter}{Number}` | `A2`, `E26`, `I3`, `M56` |
| Subsection | `{Letter}{Number}.{N}` | `A2.0`, `E26.1`, `I3.1` |
| Paragraph | `{Letter}{Number}.{N}.{N}` | `A2.1.1`, `E26.1.1`, `I3.1.1` |
| Sub-paragraph | `{Letter}{Number}.{N}.{N}.{N}` | `A2.1.1.1`, `E26.1.1.1` |
| Sub-sub-paragraph | Keyword or continuation | `Table 1`, `Note:`, `Appendix` |

## Structural Patterns

1. **Document root**: The UR identifier (e.g., `A2`, `E26`) appears as the first `#` heading
2. **Revision metadata**: Appears as plain text immediately after the root heading (dates in parentheses)
3. **Application section**: Typically the first subsection (e.g., `A2.0 Application and definitions`)
4. **Numbered paragraphs**: Follow `{DocID}.{N}.{N}` pattern consistently
5. **Tables**: May appear as headings (e.g., `#### Table 1`) or as inline content
6. **Notes**: May appear as sub-paragraph headings or inline bold text
7. **Deleted URs**: Contain only a root heading with deletion notice text

## Regex Patterns

```json
[
  {
    "pattern": "^(?P<hashes>#{1,6})\\s+(?P<full_text>(?P<number>[A-Z]\\d+(?:\\.\\d+)*)\\s+(?P<text>.+))$",
    "expected_level": "auto",
    "number_group": "number",
    "text_group": "text",
    "flags": [],
    "priority": 1,
    "notes": "Numbered IACS UR heading (e.g., A2.1.3 Load considerations)"
  },
  {
    "pattern": "^(?P<hashes>#{1,6})\\s+(?P<text>(?:Table|Annex|Appendix|Note|Figure)\\s*.*)$",
    "expected_level": "auto",
    "number_group": null,
    "text_group": "text",
    "flags": ["IGNORECASE"],
    "priority": 2,
    "notes": "Keyword-based headings (Table, Annex, Appendix, Note, Figure)"
  },
  {
    "pattern": "^(?P<hashes>#{1,6})\\s+(?P<text>.+)$",
    "expected_level": "auto",
    "number_group": null,
    "text_group": "text",
    "flags": [],
    "priority": 3,
    "notes": "Generic ATX markdown heading (fallback)"
  }
]
```

## Level Skip Handling

IACS UR documents sometimes skip markdown heading levels (e.g., `#` followed directly by `###` with no `##`). Per the depth compression rule, tree depth is compressed to sequential values:

- `#` (H1) → Depth 1
- `###` (H3, but first child of H1) → Depth 2 (compressed from 3)
- `####` (H4, child of compressed H3) → Depth 3 (compressed from 4)

## Observations

- Most small/deleted URs have only 1 heading (the document title section)
- Large URs (E26, I3, I2, M56) have 40-125 headings with up to 5 depth levels
- Heading numbers are always prefixed with the UR identifier letter+number
- Some documents contain two sibling sections at Depth=1 (e.g., continuation pages)
