# Pull Request 증빙 감사

> 이 문서는 2026-09-16 검증 시점의 감사 스냅샷입니다. 이후 실제 완료 상태와 최종 링크는 [SUBMISSION.md](../SUBMISSION.md)를 기준으로 확인합니다.

2026-09-16 KST에 GitHub의 실제 Conversation 타임라인, commit과 현재 파일을 함께 확인했습니다. `실질 리뷰`는 특정 파일·동작·위험·대안을 언급한 코멘트만 인정했고, 단순 승인·칭찬은 보수적으로 제외했습니다. 수정 commit은 리뷰 반영 상호작용으로 인정했습니다.

| PR | 작성자 | 상태·Issue | What/Why/How | 실질 리뷰 | 작성자 상호작용 | 필요한 최소 보완 |
| --- | --- | --- | --- | --- | --- | --- |
| [#4](https://github.com/c-b2-2/make-program-with-friends/pull/4) | 최건영 | 병합 · #3 | 충족 | 이준혁의 커밋 예시 제안 | 없음 | 최건영이 사실 확인 답글 1개 |
| [#6](https://github.com/c-b2-2/make-program-with-friends/pull/6) | 이준혁 | 병합 · #1 | 충족 | 기존 “정상 동작”은 근거가 약함 | 없음 | 김보민이 음수 입력 등 구체적 코멘트, 이준혁 답글 |
| [#7](https://github.com/c-b2-2/make-program-with-friends/pull/7) | 김강현 | 병합 · #5 | How 공란 | 이준혁이 How 누락 지적 | 없음 | How 보완과 김강현 답글 |
| [#10](https://github.com/c-b2-2/make-program-with-friends/pull/10) | 최건영 | 병합 · #8 | 충족 | 이준혁이 기존 규칙 충돌 지적 | 수정 commit·답글 확인 | 없음 |
| [#11](https://github.com/c-b2-2/make-program-with-friends/pull/11) | 김보민 | 열림 · #9 | How가 과거 3인자 구현 | 임효정이 `args` 사용 오류 지적 | `82ba2d7` 수정 commit 확인 | How를 현재 2인자로 정정 후 병합 |
| [#13](https://github.com/c-b2-2/make-program-with-friends/pull/13) | 김강현 | 병합 · #12 | 충족 | 최건영이 import 부작용 지적 | `e3b21a0` 수정 commit 확인 | 없음 |
| [#18](https://github.com/c-b2-2/make-program-with-friends/pull/18) | 최건영 | 병합 · #16 | 본문은 ValueError, 최종 코드는 ZeroDivisionError | 김강현이 예외 타입 지적 | `6979f4d` 수정 commit 확인 | 본문 설명만 최종 코드에 맞춤 |
| [#19](https://github.com/c-b2-2/make-program-with-friends/pull/19) | 임효정 | 열림 · #17 | 구현 설명만 있고 실행 결과 부족 | 이준혁이 0·음수 지수 검증 제안 | 없음 | 최상위 출력 제거, 세 테스트와 답글 후 병합 |
| [#21](https://github.com/c-b2-2/make-program-with-friends/pull/21) | 이준혁 | 병합 · #15 | 존재하지 않는 `conflict-resolution.md` 추가를 주장 | 최건영의 절차·위험 확인 | 없음 | 본문 사실 정정과 이준혁 답글 |
| [#22](https://github.com/c-b2-2/make-program-with-friends/pull/22) | 김보민 | 병합 · #20 | How가 `merge확인`으로 불충분 | 김강현의 구체적 문서 구조 평가 | 없음 | How 보완과 김보민 답글 |
| [#24](https://github.com/c-b2-2/make-program-with-friends/pull/24) | 이준혁 | 병합 · #23 | PR 본문은 충족, 병합 파일은 결과·Why·주의점과 코드 펜스가 미완성이었음 | 임효정의 기존 코멘트는 일반 확인 수준 | 없음 | 이 정리 PR에서 문서 보완. 임효정이 위험/대안 코멘트 보강, 이준혁 답글 |
| [#28](https://github.com/c-b2-2/make-program-with-friends/pull/28) | 김보민 | 열림 · #27 | 상황·명령만 있어 결과·Why·주의점·역할 부족 | 0개 | 0회 | 임효정 필수 리뷰 → 김보민 문서·답글 보완 → 승인·병합 |
| [#29](https://github.com/c-b2-2/make-program-with-friends/pull/29) | 임효정 | 열림 · #25 | PR 본문은 상세하지만 실제 문서에 명령·결과·Why·주의점·역할 부족 | 0개 | 0회 | 김보민 리뷰 → 임효정 문서·답글 보완 → 승인·병합 |

## 개인별 최소 기준 판정

| 팀원 | 병합 PR | 확실한 타인 실질 리뷰 | 자기 PR 리뷰 반영 | 판정 |
| --- | ---: | ---: | --- | --- |
| 이준혁 (`Cerhovah`) | 3 | 2회 이상 | 미확인 | 정리 PR에서 최건영 리뷰에 답하거나 수정하면 충족 |
| 김강현 (`kanghyki`) | 2 | 2회 이상 | #13 수정 commit | 충족 |
| 최건영 (`00skgun`) | 3 | 2회 이상 | #10 수정·답글 | 충족 |
| 김보민 (`nengrafi`) | 1 | 1회 | #11 수정 commit | #11·#28 병합 및 #6 또는 #29 실질 리뷰 필요 |
| 임효정 (`gittul-123`) | 0 | 1회 | 미확인 | #19·#29 병합, #28 실질 리뷰, 자기 PR 답글 필요 |

과거에 이미 병합된 PR의 사후 답글이 당시 상호작용으로 인정되는지는 평가 정책에 따라 달라질 수 있습니다. 이 제한을 숨기거나 과거 행동을 새로 지어내지 않습니다.
