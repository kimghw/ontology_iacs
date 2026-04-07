SKOS 작업할 때 특히 유용한 힌트
처음부터 하나의 공통 개념으로 합치지 않는 것이 좋습니다. IMO/IACS/KR가 같은 headword를 써도 정의·적용범위가 조금씩 다를 수 있는데, SKOS는 “어떤 특정 관계나 정의가 어느 scheme에 속하는지”를 세밀하게 기록하는 데 한계가 있습니다. 그래서 1차는 source-specific concept로 분리하고, 나중에 mapping으로 잇는 방식이 안전합니다.
cross-source 연결은 기본을 skos:closeMatch, 정말 동일하다고 확신할 때만 skos:exactMatch를 권합니다. closeMatch는 비추이적이고, exactMatch는 추이적이라서 과하게 쓰면 연쇄적인 오판정이 생길 수 있습니다. owl:sameAs는 서로 다른 concept scheme의 SKOS 개념을 연결할 때 일반적으로 부적절하다고 W3C가 경고합니다.
약어/동의어 정책은 일찍 정해 두는 게 좋습니다. 약어·acronym·정상적인 변형은 skos:altLabel, 검색 전용 변형이나 dotted form, OCR 변형, 오탈자형은 **skos:hiddenLabel**이 잘 맞습니다. prefLabel은 언어당 1개만 허용됩니다.
Pattern 11의 example/enumeration tail은 custom field보다 skos:example 하나를 추가하는 편이 SKOS 친화적입니다. 또 “Type A, B, C”가 실제 하위종류라면 altLabel로 먹이지 말고 나중에 별도 concept + narrower relation로 빼는 편이 낫습니다. SKOS Primer도 이런 upward posting 방식은 권장하지 않습니다.
문서별/장별/출처별 묶음은 broader/narrower로 만들지 말고, skos:ConceptScheme나 skos:Collection으로 처리하는 게 좋습니다. Collection은 grouping용이고, Concept/ConceptScheme과 구분됩니다.
나중에 “이 약어가 이 풀네임의 acronym이다”처럼 라벨끼리의 관계까지 관리하고 싶다면, 그때 SKOS-XL을 검토하면 됩니다. SKOS-XL은 label을 일급 리소스로 다루고 label relation을 붙일 수 있습니다. 다만 1차에서는 기본 SKOS의 altLabel만으로도 충분한 경우가 많습니다.
QA는 초반부터 SHACL을 붙이는 게 좋습니다. SHACL은 RDF 그래프를 제약조건으로 검증하는 표준이라서, “영문 필드에 한글 금지”, “source 누락 금지”, “언어별 prefLabel 중복 금지” 같은 규칙을 자동 검사하기 좋습니다.