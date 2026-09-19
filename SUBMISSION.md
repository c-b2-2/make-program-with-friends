# 제출 인덱스

> 2026-09-19 KST 기준. GitHub PR·Issue·review와 PR #38 병합 후 `origin/main`의 `78829e14fc2f7646fa6f3a530349357bacd2c235`를 대조했습니다. 완료된 작업과 아직 증빙이 필요한 작업을 아래에 구분합니다.

이번 문서 정리는 [Issue #39](https://github.com/c-b2-2/make-program-with-friends/issues/39)와 [PR #40](https://github.com/c-b2-2/make-program-with-friends/pull/40)에서 추적합니다.

## 저장소와 결과물

- [저장소](https://github.com/c-b2-2/make-program-with-friends): 팀원 5명이 GitHub Flow로 작업하는 Python 유틸 함수 모음(A)
- `main`에는 [`add`](https://github.com/c-b2-2/make-program-with-friends/pull/13), [`subtract`](https://github.com/c-b2-2/make-program-with-friends/pull/6), [`divide`](https://github.com/c-b2-2/make-program-with-friends/pull/18), [`multiply_function`](https://github.com/c-b2-2/make-program-with-friends/pull/11), [`power`](https://github.com/c-b2-2/make-program-with-friends/pull/19)가 모두 병합됐습니다. 각 함수의 사용 예시는 [README](README.md)에 있습니다.
- `main`의 [활성 ruleset](https://github.com/c-b2-2/make-program-with-friends/settings/rules)은 PR, 다른 사람의 Approve 1개, 리뷰 대화 해결을 요구하고 강제 push와 브랜치 삭제를 제한합니다. 브랜치·Issue·PR 규칙은 [CONTRIBUTING](docs/CONTRIBUTING.md)에 있습니다.

## 팀원별 작업과 협업 기록

아래 PR 수는 **병합 완료** 기준입니다. 리뷰 예시는 작성자 본인의 PR을 제외한 사람 리뷰입니다. 파일의 동작·결과·위험 또는 수정 필요 사항을 구체적으로 짚은 경우만 실질 리뷰로 셌습니다. 확인·칭찬·승인만 남긴 경우는 제외했습니다.

| 팀원 | 주요 Issue → 병합 PR | 병합 PR 수 | 확인한 타인 실질 리뷰 | 자기 PR 피드백 반영 예시 |
| --- | --- | ---: | --- | --- |
| 이준혁 (`Cerhovah`) | [#1](https://github.com/c-b2-2/make-program-with-friends/issues/1)→[#6](https://github.com/c-b2-2/make-program-with-friends/pull/6), [#15](https://github.com/c-b2-2/make-program-with-friends/issues/15)→[#21](https://github.com/c-b2-2/make-program-with-friends/pull/21), [#23](https://github.com/c-b2-2/make-program-with-friends/issues/23)→[#24](https://github.com/c-b2-2/make-program-with-friends/pull/24), [#30](https://github.com/c-b2-2/make-program-with-friends/issues/30)→[#31](https://github.com/c-b2-2/make-program-with-friends/pull/31), [#33](https://github.com/c-b2-2/make-program-with-friends/issues/33)→[#34](https://github.com/c-b2-2/make-program-with-friends/pull/34) | 5 | [#10](https://github.com/c-b2-2/make-program-with-friends/pull/10), [#18](https://github.com/c-b2-2/make-program-with-friends/pull/18) | [#21](https://github.com/c-b2-2/make-program-with-friends/pull/21)의 리뷰 후 답변 |
| 김강현 (`kanghyki`) | [#5](https://github.com/c-b2-2/make-program-with-friends/issues/5)→[#7](https://github.com/c-b2-2/make-program-with-friends/pull/7), [#12](https://github.com/c-b2-2/make-program-with-friends/issues/12)→[#13](https://github.com/c-b2-2/make-program-with-friends/pull/13), [#26](https://github.com/c-b2-2/make-program-with-friends/issues/26)→[#32](https://github.com/c-b2-2/make-program-with-friends/pull/32) | 3 | [#18](https://github.com/c-b2-2/make-program-with-friends/pull/18), [#28](https://github.com/c-b2-2/make-program-with-friends/pull/28) | [#13](https://github.com/c-b2-2/make-program-with-friends/pull/13) 리뷰 뒤 `e3b21a0` 수정 커밋 |
| 최건영 (`00skgun`) | [#3](https://github.com/c-b2-2/make-program-with-friends/issues/3)→[#4](https://github.com/c-b2-2/make-program-with-friends/pull/4), [#8](https://github.com/c-b2-2/make-program-with-friends/issues/8)→[#10](https://github.com/c-b2-2/make-program-with-friends/pull/10), [#16](https://github.com/c-b2-2/make-program-with-friends/issues/16)→[#18](https://github.com/c-b2-2/make-program-with-friends/pull/18), [#35](https://github.com/c-b2-2/make-program-with-friends/issues/35)→[#36](https://github.com/c-b2-2/make-program-with-friends/pull/36), [#37](https://github.com/c-b2-2/make-program-with-friends/issues/37)→[#38](https://github.com/c-b2-2/make-program-with-friends/pull/38) | 5 | [#13](https://github.com/c-b2-2/make-program-with-friends/pull/13), [#21](https://github.com/c-b2-2/make-program-with-friends/pull/21) | [#18](https://github.com/c-b2-2/make-program-with-friends/pull/18) 리뷰 뒤 `6979f4d` 수정 커밋 |
| 김보민 (`nengrafi`) | [#9](https://github.com/c-b2-2/make-program-with-friends/issues/9)→[#11](https://github.com/c-b2-2/make-program-with-friends/pull/11), [#20](https://github.com/c-b2-2/make-program-with-friends/issues/20)→[#22](https://github.com/c-b2-2/make-program-with-friends/pull/22), [#27](https://github.com/c-b2-2/make-program-with-friends/issues/27)→[#28](https://github.com/c-b2-2/make-program-with-friends/pull/28) | 3 | [#13](https://github.com/c-b2-2/make-program-with-friends/pull/13) 1건 확인. 다른 승인에는 구체적 피드백이 부족함 | [#11](https://github.com/c-b2-2/make-program-with-friends/pull/11) 리뷰 뒤 `82ba2d7` 수정 커밋 |
| 임효정 (`gittul-123`) | [#17](https://github.com/c-b2-2/make-program-with-friends/issues/17)→[#19](https://github.com/c-b2-2/make-program-with-friends/pull/19), [#25](https://github.com/c-b2-2/make-program-with-friends/issues/25)→[#29](https://github.com/c-b2-2/make-program-with-friends/pull/29) | 2 | [#11](https://github.com/c-b2-2/make-program-with-friends/pull/11) 1건 확인. [#24](https://github.com/c-b2-2/make-program-with-friends/pull/24)는 일반 확인 | [#19](https://github.com/c-b2-2/make-program-with-friends/pull/19)의 리뷰 후 답변 |

현재 기준 위 18개 PR은 모두 병합됐습니다. 제출 정리 중 사용한 `#11`, `#19`, `#28`, `#29`, `#31`, `#34`, `#38`도 더 이상 열린 PR이 아닙니다. 개인별 병합 PR 최소 2개와 위의 자기 PR 피드백 예시는 확인됩니다. 김보민과 임효정의 **두 번째 구체적 타인 리뷰**는 별도 확인이 필요합니다.

임효정의 [PR #11 리뷰](https://github.com/c-b2-2/make-program-with-friends/pull/11#pullrequestreview-5210163092)는 곱셈 반복에서 `num` 대신 `args` 전체를 쓰는 코드를 특정해 동작상 의문을 제기했으므로 실질 리뷰입니다. [PR #24 승인 리뷰](https://github.com/c-b2-2/make-program-with-friends/pull/24#pullrequestreview-5210395216)는 시나리오·참여자·상황·명령을 확인했다고만 적었고, 특정 결과·위험·수정 제안은 없습니다. 해당 PR의 인라인 리뷰 댓글도 없어 일반 확인으로 분류합니다. [PR #34 승인 리뷰](https://github.com/c-b2-2/make-program-with-friends/pull/34)도 구체적 검토 근거가 없어 같은 기준으로 제외했습니다.

## 충돌과 트러블슈팅

- [충돌 기록](docs/conflict-resolution.md): 우발 충돌 3건은 의도적 실습에서 제외합니다. 이준혁·최건영의 `practice_1` 같은 줄 충돌 1건은 Git 이력으로 확인됐습니다. `practice_2` 시도에는 최건영의 해당 줄 변경 커밋이 없어 **필수 의도적 실습은 현재 확인 가능한 1/2회**입니다.
- [트러블슈팅 기록](docs/troubleshooting-log.md): amend는 임효정의 [#29](https://github.com/c-b2-2/make-program-with-friends/pull/29), reset은 김보민의 [#28](https://github.com/c-b2-2/make-program-with-friends/pull/28), revert는 김강현의 [#32](https://github.com/c-b2-2/make-program-with-friends/pull/32), stash는 이준혁의 [#24](https://github.com/c-b2-2/make-program-with-friends/pull/24)와 최건영 요청으로 진행한 [#36](https://github.com/c-b2-2/make-program-with-friends/pull/36)·[#38](https://github.com/c-b2-2/make-program-with-friends/pull/38)에 기록됐습니다. #38은 `main`에 병합됐고, untracked 파일 시연과 tracked 수정분 검증을 각각 보존했습니다. 최건영 명의의 문서 커밋과 Codex 실행을 구분했으며, 최건영 본인의 직접 명령 실행은 확인되지 않았습니다.

## 제출 파일과 확인 결과

- [README](README.md) · [협업 규칙](docs/CONTRIBUTING.md) · [충돌 기록](docs/conflict-resolution.md) · [트러블슈팅 기록](docs/troubleshooting-log.md)
- [Git 히스토리 텍스트](docs/git-history.txt) · [충돌 실습 최종 파일](docs/conflict-practice.txt)
- `python3 -m unittest discover -s tests -v`: 기존 테스트 4건 통과. 다섯 함수의 예시 입력 직접 호출도 통과했습니다.
- 중간 감사·과거 작업 목록·고의 오류 문서는 삭제했습니다. 이 문서가 현재 상태의 단일 제출 인덱스입니다.

## 남은 실제 사람 작업

1. 이준혁과 최건영이 같은 새 시작 커밋에서 `practice_2`를 각각 바꿔 충돌·해결하고, 두 변경 커밋과 병합 커밋을 [충돌 기록](docs/conflict-resolution.md)에 추가해야 합니다.
2. 김보민과 임효정이 각각 타인 PR에 파일·동작·위험을 근거로 한 구체적 리뷰를 한 건 더 남겨야 합니다. 최종 정리 PR에서 남기는 리뷰도 실제로 작성되면 증빙이 됩니다.
3. 트러블슈팅의 전원 직접 실행이 미션 기준이라면 최건영이 자신의 stash 명령과 결과를 직접 남겨야 합니다. Codex 시연은 그 증빙을 대신하지 않습니다.
4. [문서 정리 PR #40](https://github.com/c-b2-2/make-program-with-friends/pull/40)도 다른 팀원의 실제 리뷰와 Approve 후 `main`에 병합해야 합니다.

따라서 다섯 유틸 함수와 병합 PR 수는 충족됐지만, **현재 상태를 미션 전체의 최종 완료로 판정하지 않습니다.**
