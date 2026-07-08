# PM License Appeal Toolkit

Legal-Tech / Civic-Tech / Public Documentation / Administrative Appeal Templates

이 저장소는 대한민국에서 개인형 이동장치(PM, 전동킥보드 등) 관련 운전면허 결격, 운전면허시험 응시원서 접수 거부처분, 행정심판 청구 절차를 이해하기 쉽게 정리한 공개 자료집입니다.

이 자료는 실제 행정심판 경험과 공개 가능한 법리 검토를 바탕으로 작성되었으나, 법률 자문이 아니며 변호사, 행정사, 관할 행정기관의 상담을 대체하지 않습니다. 공개 저장소에는 실명, 주소, 사건번호, 접수번호, 원본 처분서, 원본 재결서 등 개인정보 또는 민감정보를 절대 업로드하지 마십시오.

## 프로젝트 포지셔닝

이 저장소는 단순한 사건 후기 저장소가 아니라, 실제 행정절차에서 반복되는 문제를 재사용 가능한 공개 문서와 템플릿으로 정리하는 프로젝트입니다.

* Legal-Tech: 법률ㆍ행정 절차를 문서 구조와 체크리스트로 정리
* Civic-Tech: 개인이 공공 행정 절차를 이해하고 접근할 수 있도록 도움
* Public Documentation: 공개 가능한 범위에서 절차, 용어, 흐름, 주의사항을 문서화
* Privacy-first Templates: 원본 사건자료가 아닌 익명 예시와 민감정보 점검 도구 제공

추천 GitHub topics:

`legal-tech`, `civic-tech`, `public-documentation`, `administrative-appeal`, `korea`, `road-traffic-law`, `personal-mobility`, `templates`, `privacy`

## 누구를 위한 자료인가

이 저장소는 다음 상황을 겪는 사람이 절차와 문서 구조를 이해할 수 있도록 돕기 위한 자료입니다.

* 개인형 이동장치 음주운전 후 운전면허 결격 문제가 생긴 경우
* 운전면허시험장에서 응시원서 접수 거부처분을 받은 경우
* 행정심판 청구서, 청구취지, 청구이유, 보충의견서를 작성해야 하는 경우
* 인용 재결 후 경찰서 또는 면허 담당 부서에 전산 반영을 요청해야 하는 경우
* 무면허 전동킥보드 6개월 결격 사안에서 가능한 주장 구조를 검토하려는 경우

## 다루는 주제

* 개인형 이동장치 음주운전 후 면허 결격
* 응시원서 접수 거부처분
* 행정심판 청구 절차
* 피청구인 답변서 송달 후 보충의견서 작성
* 인용 재결서 수령 후 경찰 전산 반영 요청
* 무면허 전동킥보드 사안에서 가능한 주장 구조
* 공개 문서 작성 전 개인정보 제거 점검

## 저장소 구성

| 경로 | 내용 |
| --- | --- |
| `docs/00_disclaimer.md` | 면책 고지와 개인정보 업로드 금지 원칙 |
| `docs/01_overview.md` | 개인형 이동장치 면허 결격 문제 개요 |
| `docs/02_process_flow.md` | 행정심판 접수부터 재결 후 전산 반영까지의 흐름 |
| `docs/03_case_study_pm_dui_appeal.md` | PM 음주 관련 익명 사례와 쟁점 구조 |
| `docs/04_case_study_pm_unlicensed_possible_arguments.md` | 무면허 PM 사안에서 가능한 주장 구조 |
| `docs/05_terms.md` | 청구인, 피청구인, 처분, 재결 등 용어 정리 |
| `docs/06_faq.md` | 자주 묻는 질문 |
| `docs/07_checklist.md` | 접수 전, 접수 후, 재결 후, 공개 전 체크리스트 |
| `templates/` | 청구취지, 청구이유, 보충의견서, 증거목록, 전산 반영 요청문 |
| `examples/` | 공개 가능한 익명 처분서ㆍ재결서 요약 예시 |
| `scripts/redact_check.py` | 공개 전 민감정보 패턴 점검 스크립트 |

## 빠른 시작

1. 처분서 또는 접수 거부처분서를 수령합니다.
2. 행정심판 청구기간을 확인합니다.
3. 행심24 또는 관할 행정심판위원회 절차를 확인합니다.
4. 청구취지를 작성합니다.
5. 청구이유를 작성합니다.
6. 답변서가 송달되면 보충의견서를 제출합니다.
7. 인용 재결서를 수령하면 재결서를 다운로드합니다.
8. 경찰서 또는 면허 담당 부서에 결격 해제 전산 반영을 요청합니다.
9. 반영 여부를 확인한 뒤 운전면허시험장을 방문합니다.

## 템플릿 사용 흐름

1. `docs/00_disclaimer.md`와 `docs/01_overview.md`를 먼저 읽습니다.
2. `docs/02_process_flow.md`로 전체 절차를 확인합니다.
3. 처분 유형에 따라 `docs/03_case_study_pm_dui_appeal.md` 또는 `docs/04_case_study_pm_unlicensed_possible_arguments.md`를 참고합니다.
4. `templates/appeal_claim_purpose.md`로 청구취지를 정리합니다.
5. `templates/appeal_reason_pm_dui.md`를 사건 사실관계에 맞게 수정합니다.
6. 피청구인 답변서가 오면 `templates/supplemental_opinion.md`를 사용해 반박 구조를 정리합니다.
7. 제출 자료는 `templates/evidence_list.md`로 관리합니다.
8. 인용 재결 후에는 `templates/police_submission_request.md`를 참고해 전산 반영 요청문을 작성합니다.
9. 공개 전에는 반드시 `scripts/redact_check.py`를 실행합니다.

## 중요한 주의

이 저장소는 음주운전이나 무면허운전을 정당화하지 않습니다. 개인형 이동장치도 도로교통법상 규율 대상이며, 실제 처분과 행정심판 결과는 사안별 사실관계, 법령, 재결례, 행정청 실무에 따라 달라질 수 있습니다.

법령은 개정될 수 있습니다. 이 문서는 2026-07-08 기준으로 공개 자료를 확인하여 작성했으며, 실제 사건에 사용하기 전에는 반드시 최신 법령과 전문가 상담을 확인해야 합니다.

## 공식 참고 자료

* [행정심판법 제27조: 심판청구의 기간](https://www.law.go.kr/LSW//lsSideInfoP.do?docCls=jo&joBrNo=00&joNo=0027&lsiSeq=249041&urlMode=lsScJoRltInfoR)
* [국민권익위원회 온라인 행정심판 안내](https://www.acrc.go.kr/menu.es?mid=a10103050000)
* [온라인행정심판 행심24](https://www.simpan.go.kr/)
* [도로교통법상 개인형 이동장치 정의 관련 조문](https://www.law.go.kr/lsLinkProc.do?ancYd=20221017&joNo=000200&lsClsCd=L&lsId=2000518&lsNm=%EB%8F%84%EB%A1%9C%EA%B5%90%ED%86%B5%EB%B2%95&mode=4)
* [국가법령정보센터 공개 재결례 예시](https://www.law.go.kr/DRF/lawService.do?ID=272179&OC=shkff&mobileYn=Y&target=decc&type=HTML)

## 개인정보 업로드 금지

공개 GitHub 저장소에는 다음 자료를 올리지 마십시오.

* 실명, 주소, 주민등록번호
* 전화번호, 이메일
* 사건번호, 접수번호
* 원본 처분서, 원본 재결서
* 병원기록, 진단서, 입원확인서 원본
* 경찰서, 시험장, 행정기관 담당자 실명 또는 연락처

공개 전에는 `scripts/redact_check.py`를 실행하여 민감정보 패턴을 점검하십시오.

```bash
python scripts/redact_check.py docs templates examples
```

## 기여 원칙

이 저장소에 기여할 때는 다음 원칙을 지켜 주십시오.

* 실제 사건번호, 접수번호, 실명, 주소, 전화번호, 이메일을 포함하지 않습니다.
* 원본 처분서, 원본 재결서, 진단서, 병원기록, 경찰 또는 행정기관 문서를 업로드하지 않습니다.
* 법령 또는 공개 재결례를 인용할 때는 출처 링크를 함께 남깁니다.
* 특정 사건의 승소 가능성을 단정하지 않습니다.
* 음주운전, 무면허운전, 안전의무 위반을 정당화하는 표현을 쓰지 않습니다.

## 로드맵

* [ ] 행심24 제출 화면 기준 입력항목 가이드 추가
* [ ] 공개 재결례 링크 목록 정리
* [ ] 템플릿별 작성 예시 확대
* [ ] 민감정보 점검 스크립트 패턴 보강
* [ ] 영어 요약 섹션 추가

## 라이선스

이 저장소는 MIT License로 배포됩니다.
