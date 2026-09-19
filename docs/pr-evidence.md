# Pull Request 증빙 감사

> 이 문서는 2026-09-16 검증 시점의 감사 스냅샷입니다. 이후 실제 완료 상태와 최종 링크는 [SUBMISSION.md](../SUBMISSION.md)를 기준으로 확인합니다.

2026-09-16 KST에 GitHub의 실제 Conversation 타임라인, commit과 현재 파일을 함께 확인했습니다. 이후 Issue #30과 Draft PR #31을 만들고 #6·#21·#24에 사후 기록을 남긴 결과도 아래 표에 반영했습니다. `실질 리뷰`는 특정 파일·동작·위험·대안을 언급한 코멘트만 인정했고, 단순 승인·칭찬은 보수적으로 제외했습니다. 수정 commit은 리뷰 반영 상호작용으로 인정했습니다.

| PR | 작성자 | 상태·Issue | What/Why/How | 실질 리뷰 | 작성자 상호작용 | 필요한 최소 보완 |
| --- | --- | --- | --- | --- | --- | --- |
| [#4](https://github.com/c-b2-2/make-program-with-friends/pull/4) | 최건영 | 병합 · #3 | 충족 | 이준혁의 커밋 예시 제안 | 없음 | 최건영이 사실 확인 답글 1개 |
| [#6](https://github.com/c-b2-2/make-program-with-friends/pull/6) | 이준혁 | 병합 · #1 | 충족 | 기존 “정상 동작”은 근거가 약함 | 이준혁이 현재 `main`의 양수·음수 두 사례를 사후 재검증 | 김보민이 음수 입력 등 구체적 코멘트 1개 |
| [#7](https://github.com/c-b2-2/make-program-with-friends/pull/7) | 김강현 | 병합 · #5 | How 공란 | 이준혁이 How 누락 지적 | 없음 | How를 리뷰 반영 수정으로 보완. 별도 답글은 선택 |
| [#10](https://github.com/c-b2-2/make-program-with-friends/pull/10) | 최건영 | 병합 · #8 | 충족 | 이준혁이 기존 규칙 충돌 지적 | 수정 commit·답글 확인 | 없음 |
| [#11](https://github.com/c-b2-2/make-program-with-friends/pull/11) | 김보민 | 열림 · #9 | How가 과거 3인자 구현 | 임효정이 `args` 사용 오류 지적 | `82ba2d7` 수정 commit 확인 | How를 현재 2인자로 정정 후 병합 |
| [#13](https://github.com/c-b2-2/make-program-with-friends/pull/13) | 김강현 | 병합 · #12 | 충족 | 최건영이 import 부작용 지적 | `e3b21a0` 수정 commit 확인 | 없음 |
| [#18](https://github.com/c-b2-2/make-program-with-friends/pull/18) | 최건영 | 병합 · #16 | 본문은 ValueError, 최종 코드는 ZeroDivisionError | 김강현이 예외 타입 지적 | `6979f4d` 수정 commit 확인 | 본문 설명만 최종 코드에 맞춤 |
| [#19](https://github.com/c-b2-2/make-program-with-friends/pull/19) | 임효정 | 열림 · #17 | 구현 설명만 있고 실행 결과 부족 | 이준혁이 0·음수 지수 검증 제안 | 없음 | 최상위 출력 제거와 세 테스트를 리뷰 반영 commit으로 남긴 뒤 병합 |
| [#21](https://github.com/c-b2-2/make-program-with-friends/pull/21) | 이준혁 | 병합 · #15 | 실제 diff가 `CONTRIBUTING.md`뿐임을 본문에 사후 정정 | 최건영의 절차·위험 확인 | 이준혁의 사실 정정 답글 확인 | 없음 |
| [#22](https://github.com/c-b2-2/make-program-with-friends/pull/22) | 김보민 | 병합 · #20 | How가 `merge확인`으로 불충분 | 김강현의 구체적 문서 구조 평가 | 없음 | How를 리뷰 반영 수정으로 보완. 별도 답글은 선택 |
| [#24](https://github.com/c-b2-2/make-program-with-friends/pull/24) | 이준혁 | 병합 · #23 | PR 본문은 충족, 병합 파일의 결과·Why·주의점과 코드 펜스는 #31에서 보완 | 임효정의 기존 코멘트는 일반 확인 수준 | 이준혁의 사후 보완 답글 확인 | 임효정이 위험/대안 코멘트 1개 보강 |
| [#28](https://github.com/c-b2-2/make-program-with-friends/pull/28) | 김보민 | 열림 · #27 | 상황·명령만 있어 결과·Why·주의점·역할 부족 | 0개 | 0회 | 임효정 필수 리뷰 → 김보민 문서 수정 commit → 승인·병합 |
| [#29](https://github.com/c-b2-2/make-program-with-friends/pull/29) | 임효정 | 열림 · #25 | PR 본문은 상세하지만 실제 문서에 명령·결과·Why·주의점·역할 부족 | 0개 | 0회 | 김보민 리뷰 → 임효정 문서 수정 commit → 승인·병합 |
| [#31](https://github.com/c-b2-2/make-program-with-friends/pull/31) | 이준혁 | Draft · #30·#26 | 미실행 작업은 증빙 게이트로 구분. 공개된 리뷰 실습용 고의 오류 1줄은 수정 전 | 최건영에게 리뷰 요청, 아직 리뷰 전 | 0회 | 오류 줄 리뷰 → 이준혁 수정·답글 → 나머지 증빙 반영 → 최건영 승인·병합 |

## 개인별 최소 기준 판정

| 팀원 | 병합 PR | 확실한 타인 실질 리뷰 | 자기 PR 리뷰 반영 | 판정 |
| --- | ---: | ---: | --- | --- |
| 이준혁 (`Cerhovah`) | 3 | 2회 이상 | #21 사후 정정·답글 | 실행 증빙 있음. 사후 답글 인정 여부만 평가 정책 확인 |
| 김강현 (`kanghyki`) | 2 | 2회 이상 | #13 수정 commit | 충족 |
| 최건영 (`00skgun`) | 3 | 2회 이상 | #10 수정·답글 | 충족 |
| 김보민 (`nengrafi`) | 1 | 1회 | #11 수정 commit | #11·#28 병합 및 #6 또는 #29 실질 리뷰 필요 |
| 임효정 (`gittul-123`) | 0 | 1회 | 미확인 | #19·#29 병합, #28 실질 리뷰, 자기 PR의 리뷰 반영 수정 필요 |

과거에 이미 병합된 PR의 사후 답글이 당시 상호작용으로 인정되는지는 평가 정책에 따라 달라질 수 있습니다. 이 제한을 숨기거나 과거 행동을 새로 지어내지 않습니다.
