R1	임계값 일관성	documentSplit(64K), Chunk(32K), WU(16K-32K) 수치가 문서 전체에서 일관되는지, 상호 관계가 논리적인지
R2	documentSplit/Chunk/WU 개념 중복	세 단위의 역할 구분이 명확한지, Chunk와 WU의 관계가 모호하지 않은지
R3	파일명 체계 일관성	wu- vs doc- 스코프 사용이 일관되는지, 예시가 규칙과 일치하는지
R4	절차 흐름 논리성	Step 0 → 1.1 → 1.2 → 1.3.1-1.3.5 순서가 논리적인지, 빠진 단계나 순환 참조가 없는지
R5	Lifecycle/상태 머신 완전성	WU lifecycle states, transition triggers 가 빠짐없이 정의되었는지
R6	Downstream 정합성	agents.md, task_brief_generator.md 와의 용어/참조 일치
R7	잔존 오류/불일치

논리적 일관성 (Logical Consistency) — 임계값, 용어, 규칙 간 모순 여부
품질 및 완성도 (Quality & Completeness) — 정의 명확성, 누락 항목, 모호한 표현
작업 플로우 (Workflow) — 단계 간 전환 논리, 선후관계, 병렬/순차 설계
목적 정합성 (Purpose Alignment) — PRE 범위 준수, 다운스트림 연계 적정성
실행 가능성 (Implementability) — 에이전트가 실제로 수행 가능한지, 모호한 판단 기준
편집 확인 - 동일 수치에 대한 확인, heading 값에 대한 확인