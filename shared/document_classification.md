# Document Classification

Classification scheme and structural pattern definitions extracted from source documents (IACS, IMO, KR, EU maritime regulations).

> **Authoring policy** — This document is written to reflect the results after source document analysis is complete. When a new Authority, DocType, or Source Family is identified, the corresponding entry is added.

## Authority

Organizations or regulatory frameworks that issue regulations.

| Authority | Description |
|:---|:---|
| **IACS** | International Association of Classification Societies |
| **IMO** | International Maritime Organization |
| **KR** | Korean Register of Shipping |
| **EU** | European Union maritime legislation |

## DocType

Document type classification within each Authority.

| Authority | DocType | Description |
|:---|:---|:---|
| IACS | `UR` | Unified Requirements |
| IACS | `UI` | Unified Interpretations |
| IACS | `Rec` | Recommendations |
| IACS | `PR` | Procedural Requirements |
| IMO | `SOLAS` | Safety of Life at Sea |
| IMO | `MARPOL` | Marine Pollution Prevention |
| KR | `Rules` | Classification Rules |
| EU | `Directive` | EU Directives |
| EU | `Regulation` | EU Regulations |

## Source Family (Examples)

Supergroup of DocTypes. Determines segmentation criteria, grammar selection, and normalization rules.

| Source Family | Included DocTypes | Document Boundary Criteria |
|:---|:---|:---|
| **IACS UR/UI/Rec/PR** | UR, UI, Rec, PR | 1 File = 1 Document. Multi-document or duplicate content → escalate to user. |
| **IMO Conventions** | SOLAS, MARPOL | 1 Chapter or Annex = 1 Document |
| **KR Rules** | Rules | 1 Part + Chapter = 1 Document |
| **EU Legislation** | Directive, Regulation | 1 Directive / Regulation = 1 Document |

## Heading Level

Structural hierarchy within a document. The level names used vary by source family.

### IACS

```
Document → Part → Section → Paragraph → Sub-paragraph
```

### IMO (SOLAS/MARPOL)

```
Document → Part → Chapter → Regulation → Paragraph
```

### KR Rules

```
Document → Part → Chapter → Section → Paragraph
```

### EU Legislation

```
Document → Title → Chapter → Article → Paragraph
```

> Heading level names are defined in the grammar for each source family. The hierarchies above are representative patterns and may vary depending on the actual document.
