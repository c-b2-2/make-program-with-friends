# Submission Index

> 2026-09-16 KST 기준 작업 인덱스입니다. 열린 PR과 사람 확인 항목을 모두 끝낸 뒤 상태와 Git 히스토리 증빙을 한 번 갱신해야 최종 제출본이 됩니다.

## 저장소와 팀

- 저장소: <https://github.com/c-b2-2/make-program-with-friends>
- 선택 결과물: Python 유틸 함수 모음(A)
- 팀원: 이준혁(`Cerhovah`), 김강현(`kanghyki`), 최건영(`00skgun`), 김보민(`nengrafi`), 임효정(`gittul-123`)

## 팀원별 Issue와 PR

| 팀원 | 직접 만든 Issue | 작성 PR과 연결 Issue |
| --- | --- | --- |
| 이준혁 (`Cerhovah`) | [#1](https://github.com/c-b2-2/make-program-with-friends/issues/1) 닫힘, [#14](https://github.com/c-b2-2/make-program-with-friends/issues/14) 열림, [#15](https://github.com/c-b2-2/make-program-with-friends/issues/15) 닫힘, [#23](https://github.com/c-b2-2/make-program-with-friends/issues/23) 닫힘, [#30](https://github.com/c-b2-2/make-program-with-friends/issues/30) 열림 | [#6](https://github.com/c-b2-2/make-program-with-friends/pull/6) 병합→#1, [#21](https://github.com/c-b2-2/make-program-with-friends/pull/21) 병합→#15, [#24](https://github.com/c-b2-2/make-program-with-friends/pull/24) 병합→#23, 정리 PR 예정→#30·#26 |
| 김강현 (`kanghyki`) | [#2](https://github.com/c-b2-2/make-program-with-friends/issues/2) 닫힘, [#5](https://github.com/c-b2-2/make-program-with-friends/issues/5) 닫힘, [#12](https://github.com/c-b2-2/make-program-with-friends/issues/12) 닫힘, [#25](https://github.com/c-b2-2/make-program-with-friends/issues/25) 열림, [#26](https://github.com/c-b2-2/make-program-with-friends/issues/26) 열림, [#27](https://github.com/c-b2-2/make-program-with-friends/issues/27) 열림 | [#7](https://github.com/c-b2-2/make-program-with-friends/pull/7) 병합→#5, [#13](https://github.com/c-b2-2/make-program-with-friends/pull/13) 병합→#12 |
| 최건영 (`00skgun`) | [#3](https://github.com/c-b2-2/make-program-with-friends/issues/3) 닫힘, [#8](https://github.com/c-b2-2/make-program-with-friends/issues/8) 닫힘, [#16](https://github.com/c-b2-2/make-program-with-friends/issues/16) 닫힘 | [#4](https://github.com/c-b2-2/make-program-with-friends/pull/4) 병합→#3, [#10](https://github.com/c-b2-2/make-program-with-friends/pull/10) 병합→#8, [#18](https://github.com/c-b2-2/make-program-with-friends/pull/18) 병합→#16 |
| 김보민 (`nengrafi`) | [#9](https://github.com/c-b2-2/make-program-with-friends/issues/9) 열림, [#20](https://github.com/c-b2-2/make-program-with-friends/issues/20) 닫힘 | [#11](https://github.com/c-b2-2/make-program-with-friends/pull/11) 열림→#9, [#22](https://github.com/c-b2-2/make-program-with-friends/pull/22) 병합→#20, [#28](https://github.com/c-b2-2/make-program-with-friends/pull/28) 열림→#27 |
| 임효정 (`gittul-123`) | [#17](https://github.com/c-b2-2/make-program-with-friends/issues/17) 열림 | [#19](https://github.com/c-b2-2/make-program-with-friends/pull/19) 열림→#17, [#29](https://github.com/c-b2-2/make-program-with-friends/pull/29) 열림→#25 |

PR 연결이 확인되지 않은 Issue는 #2, #14, #26입니다. #2는 초기 덧셈 Issue로 `completed` 종료됐고 실제 덧셈 구현은 #7·#13에서 추적됐지만 #2와 자동 연결되지는 않았습니다. #14의 대화형 계산기 통합은 선택한 결과물 A의 최소 기준보다 큰 별도 enhancement라서 이번 제출 필수 작업에서 제외합니다. #26은 이 문서들을 담는 정리 PR에서 함께 `Closes #26`으로 연결할 예정입니다.

## 필수 문서

- [README](README.md)
- [기여 및 협업 규칙](docs/CONTRIBUTING.md)
- [충돌 해결 기록](docs/conflict-resolution.md)
- [트러블슈팅 기록](docs/troubleshooting-log.md)
- [미션 정합성 보고서](docs/mission-audit.md)
- [Pull Request 증빙 감사](docs/pr-evidence.md)
- [사람별 최소 행동](docs/human-actions.md)
- [팀 검증 및 AI 사용 기록](docs/team-verification.md)

## 증빙

- [Git 히스토리 텍스트](docs/git-history.txt)
- [Branch Protection 설정](https://github.com/c-b2-2/make-program-with-friends/settings/rules): PR 병합 필수, 승인 1명, 대화 해결, force push 차단 확인
- [전체 Pull Requests](https://github.com/c-b2-2/make-program-with-friends/pulls?q=is%3Apr)
- [전체 Issues](https://github.com/c-b2-2/make-program-with-friends/issues?q=is%3Aissue)

## 제출 전 상태

- 병합 PR: 9개 / 열린 PR: #11, #19, #28, #29
- 유틸 함수: `main` 3개 / 열린 PR 2개
- 실제 우발 충돌: 3회 기록 / 필수 의도적 충돌: 0/2회
- 트러블슈팅: stash 내용은 이 정리 PR에서 보완(김강현 역할 확인 필요), reset·amend PR 열림, revert 미수행

최종 남은 행동은 [사람이 직접 남겨야 할 최소 행동](docs/human-actions.md)만 따르면 됩니다.
