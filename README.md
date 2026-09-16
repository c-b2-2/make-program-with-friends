# make-program-with-friends

5명이 GitHub Flow, Issue, Pull Request, 코드 리뷰와 Git 문제 해결을 함께 연습하는 저장소입니다. 복잡한 기능보다 협업 기록을 재현 가능하게 남기는 것을 목표로 하며, 결과물은 **Python 유틸 함수 모음(A)** 을 선택했습니다.

- 저장소: <https://github.com/c-b2-2/make-program-with-friends>
- 실행 환경: Python 3.10 이상
- 현재 상태(2026-09-16 KST): 최종 제출 전 정리 중. 열린 PR과 사람 확인이 필요한 항목은 [미션 정합성 보고서](docs/mission-audit.md)에 구분했습니다.

## 팀

| 이름 | GitHub | 관심 분야 | 희망 직군 |
| --- | --- | --- | --- |
| 이준혁 | [`Cerhovah`](https://github.com/Cerhovah) | Big Data, AI | AI 서비스 기획자 |
| 김강현 | [`kanghyki`](https://github.com/kanghyki) | AI | AI 설계자 |
| 최건영 | [`00skgun`](https://github.com/00skgun) | Big Data, 로봇, AI | 제공되지 않음 |
| 김보민 | [`nengrafi`](https://github.com/nengrafi) | AI, 보안 | AI 모델 개발자, NLP 전문가 |
| 임효정 | [`gittul-123`](https://github.com/gittul-123) | 프로그래밍 언어, 모바일 웹 개발 | 로봇 엔지니어, AI 윤리 전문가 |

## GitHub Flow를 선택한 이유

`main`을 항상 확인 가능한 상태로 유지하고 작업을 `feature/*` 브랜치로 분리합니다.
모든 변경을 Issue와 PR로 추적하고, 병합 전에 다른 팀원의 리뷰를 받습니다.
작은 단위의 병합과 기록을 통해 충돌 원인과 결정 과정을 다시 확인할 수 있습니다.

## 유틸 함수

| 작성자 | 함수 | 상태 | 간단 사용 예시 |
| --- | --- | --- | --- |
| 김강현 | `add(a, b)` | `main` 병합 완료 | `add(2, 3) == 5` |
| 이준혁 | `subtract(a, b)` | `main` 병합 완료 | `subtract(10, 3) == 7` |
| 최건영 | `divide(a, b)` | `main` 병합 완료 | `divide(8, 2) == 4` |
| 김보민 | `multiply_function(a, b)` | [PR #11](https://github.com/c-b2-2/make-program-with-friends/pull/11) 열림 | 병합 후 `multiply_function(2, 3) == 6` |
| 임효정 | `power(base, exponent)` | [PR #19](https://github.com/c-b2-2/make-program-with-friends/pull/19) 열림 | 병합 후 `power(2, 3) == 8` |

현재 `main`에서 사용할 수 있는 함수는 다음과 같습니다.

```python
from src.divide import divide
from src.main import add
from src.subtract import subtract

assert add(2, 3) == 5
assert subtract(10, 3) == 7
assert divide(8, 2) == 4
```

## 검증

```bash
python -m unittest discover -s tests -v
```

## 문서

- [기여 및 협업 규칙](docs/CONTRIBUTING.md)
- [충돌 해결 기록](docs/conflict-resolution.md)
- [Git 트러블슈팅 기록](docs/troubleshooting-log.md)
- [미션 정합성 보고서](docs/mission-audit.md)
- [Pull Request 증빙 감사](docs/pr-evidence.md)
- [사람이 직접 남겨야 할 최소 행동](docs/human-actions.md)
- [팀 검증 및 AI 사용 기록](docs/team-verification.md)
- [제출 인덱스](SUBMISSION.md)
