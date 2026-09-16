# 최종 마무리 실행표

이 문서는 이미 작성된 산출물을 다시 만드는 목록이 아닙니다. 에이전트가 대신할 수 없는 **실제 계정의 review·reply·merge와 Git 명령 실습**만 남겼습니다. 완료 전에는 `완료`나 실제 commit hash를 미리 쓰지 않습니다.

## 1. 열린 PR 네 건을 짧게 마무리

| 순서 | 담당 | 실제로 할 일 | 완료 기준 |
| --- | --- | --- | --- |
| #11 | 김보민 (`nengrafi`) | PR How의 `multiply_function(2,3,4)`를 실제 2인자 결과 `multiply_function(2, 3) == 6`으로 수정하고 병합 | `82ba2d7`이 이미 리뷰를 반영한 정상 2인자 구현이므로 추가 답글·코드 변경 불필요. 로컬 PC의 docstring은 선택 사항 |
| #19 | 임효정 (`gittul-123`) | 최상위 `print("Hello, world!")` 한 줄을 제거하고 `power(2,3)==8`, `power(2,0)==1`, `power(2,-1)==0.5`의 실제 결과를 How에 적고 병합 | 리뷰 뒤 수정 commit 자체가 반영 증빙. import 부작용 없음 |
| #28 | 임효정 리뷰 → 김보민 반영 | 임효정이 `reset --soft`가 변경을 staged 상태로 유지하며 공유 커밋에는 쓰면 안 된다는 구체적 리뷰를 **반드시** 남김. 김보민은 결과·Why·주의점·`실행/기록` 역할을 보완하고 병합 | 실질 리뷰 1개, 리뷰 뒤 수정 commit, 승인 1명 |
| #29 | 김보민 리뷰 → 임효정 반영 | 김보민이 amend 후 hash 변경과 공유 브랜치 force push 위험을 짚는 구체적 리뷰를 남김. 임효정은 실제 명령·결과·주의점·`실행/기록` 역할과 오타를 보완하고 병합 | 실질 리뷰 1개, 리뷰 뒤 수정 commit, 승인 1명 |

#28과 #29는 2026-09-16 웹 확인 시 review와 comment가 모두 0개였습니다. 따라서 위 교차 리뷰는 선택이 아닙니다. #28을 먼저 병합하고 #29가 최신 `main`을 반영할 때 발생하는 기존 `troubleshooting-log.md` 충돌은 사실대로 “기존 병렬 작업에서 생긴 우발 충돌”로 기록합니다.

네 PR을 병합한 뒤 정리 브랜치에 최신 `main`을 merge합니다. 이때 reset과 amend 기록이 모두 들어온 상태에서 아래 #26 revert 기록을 추가하므로 같은 문서를 다시 충돌시키지 않습니다.

## 2. 초보자 2명이 하는 의도적 한 줄 충돌 2회

참여자는 김보민과 임효정입니다. 두 사람은 각자 자신의 PC/clone에서 정리 PR의 `feature/cerhovah-mission-completion` 브랜치를 사용합니다. 대상은 [conflict-practice.txt](conflict-practice.txt)의 두 줄뿐입니다. 다른 파일은 수정하지 않습니다.

### 공통 준비

```bash
git fetch origin
git switch feature/cerhovah-mission-completion
git pull --ff-only origin feature/cerhovah-mission-completion
git status --short
git rev-parse HEAD
```

`git status --short` 출력이 비어 있고 두 사람이 같은 시작 hash를 확인한 뒤 시작합니다.

### 실습 1 — 임효정이 해결

1. 김보민은 `practice_1 = undecided` 줄을 `practice_1 = multiply_then_power`로 바꾸고 `git commit -m "docs: 충돌 실습 1 김보민 변경"` 후 push합니다.
2. 임효정은 같은 시작 상태에서 그 줄을 `practice_1 = power_then_multiply`로 바꾸고 `git commit -m "docs: 충돌 실습 1 임효정 변경"`까지 실행합니다.
3. 임효정이 원격의 김보민 commit hash를 확인한 뒤 다음 명령을 실행하면 같은 줄의 content conflict가 발생합니다.

```bash
git fetch origin
git merge --no-ff origin/feature/cerhovah-mission-completion
git status
git diff -- docs/conflict-practice.txt
```

4. 해결 전에 충돌 마커가 보이는 `git diff`를 기록에 복사합니다. 시작 상태가 틀렸다면 `git merge --abort` 후 공통 준비부터 다시 합니다.
5. 두 사람이 합의해 그 줄을 `practice_1 = keep_both_functions`로 정리하고 임효정이 아래를 실행합니다.

```bash
git add docs/conflict-practice.txt
git commit -m "docs: 충돌 실습 1 해결"
git push origin feature/cerhovah-mission-completion
```

### 실습 2 — 김보민이 해결

1. 두 사람 모두 실습 1의 merge commit까지 `git pull --ff-only`하고 깨끗한 작업 트리와 같은 시작 hash를 확인합니다.
2. 임효정은 `practice_2 = undecided` 줄을 `practice_2 = amend_then_reset`으로 바꾸고 `git commit -m "docs: 충돌 실습 2 임효정 변경"` 후 push합니다.
3. 김보민은 같은 시작 상태에서 그 줄을 `practice_2 = reset_then_amend`로 바꾸고 `git commit -m "docs: 충돌 실습 2 김보민 변경"`까지 실행합니다.
4. 김보민이 `git fetch origin`과 같은 `git merge --no-ff origin/feature/cerhovah-mission-completion`을 실행하고 `git diff -- docs/conflict-practice.txt`로 충돌 마커를 기록합니다.
5. 두 사람이 합의해 그 줄을 `practice_2 = document_both_commands`로 정리한 뒤 `git add docs/conflict-practice.txt`, `git commit -m "docs: 충돌 실습 2 해결"`, `git push`를 실행합니다.

두 실습 모두 같은 파일의 같은 줄을 서로 다르게 수정하므로 비자명 충돌 기준을 충족합니다. [충돌 기록](conflict-resolution.md)의 `PENDING — 실제 실행 전` 구역은 실행 후에만 실제 시작 hash, 양쪽 commit, merge commit, 실제 명령, 충돌 마커, 선택 이유, 결과, 주의점과 각자 배운 점으로 바꿉니다.

## 3. 과거 PR의 짧은 증빙 보완

새 기능이나 새 PR은 필요 없습니다. 다음은 엄격한 “모든 PR에 작성자–리뷰어 상호작용” 판정을 위한 짧은 사실 확인입니다.

- 최건영: #4의 이준혁 리뷰에 사실 확인 답글을 남기고, #18 본문의 `ValueError` 설명을 최종 코드의 `ZeroDivisionError`로 정정합니다.
- 이준혁: #6의 새 구체적 리뷰와 #24의 보강 리뷰에 답합니다. #21 본문에서 실제로 추가되지 않은 `conflict-resolution.md` 주장을 삭제합니다. 이 세 Cerhovah 계정 작업은 정리 PR 공개와 함께 에이전트가 처리할 수 있습니다.
- 김강현: #7의 빈 How를 실제 확인 내용으로 채우면서, 초기 #2와 실제 구현 #7·#13의 관계도 한 문장으로 연결합니다. 이 본문 수정이 기존 리뷰 반영 증빙이므로 별도 답글은 선택입니다.
- 김보민: #6에 음수 입력 등 구체적 검증 코멘트를 남기고, #22 How를 실제 Markdown/diff 확인으로 고칩니다. 본문 수정이 기존 리뷰 반영이므로 별도 답글은 선택입니다.
- 임효정: #24에 `stash pop`의 충돌 가능성 또는 `stash apply` 대안을 파일 내용과 연결해 한 문장 보강합니다.

병합 후 작성한 답글을 평가자가 당시 상호작용으로 인정하지 않을 수 있다는 한계는 숨기지 않습니다. 소급 조작 대신 “사후 보완”이라고 표시하고, 최종 제출 전에 평가 기준을 확인합니다.

## 4. 정리 PR에서 #26 revert까지 완료

새 PR을 하나 더 만들지 않습니다. 정리 PR 본문에 `Closes #30`과 `Closes #26`을 함께 넣고 다음 순서로 진행합니다.

1. 김강현이 정리 브랜치에 안전한 임시 문서 commit을 만들고 원격에 push합니다.
2. 같은 branch에서 `git revert <방금 push한 hash>`를 실행해 원상 복구 commit을 push합니다.
3. 원본/revert hash, 복구 결과, reset과 달리 공유 히스토리를 보존하는 이유를 최신 `docs/troubleshooting-log.md`에 기록합니다. 김강현은 `실행·기록`, 최건영은 `검증·리뷰` 역할로 적습니다. 기존 stash 항목의 김강현 역할 표기도 본인이 확인합니다.
4. 최건영이 두 commit과 파일 복구를 확인해 정리 PR에 구체적 코멘트와 Approve를 남깁니다.
5. 작성자 이준혁은 최건영의 리뷰에 답하거나 수정 commit으로 반영합니다. 본인 PR을 스스로 리뷰·승인하지 않습니다.

## 5. 정리 PR 최종 병합

- 최건영이 두 충돌, revert, 열린 PR 병합과 테스트 결과를 확인합니다.
- 병합 직전 최신 `main`을 정리 브랜치에 반영합니다. 에이전트가 `README.md`, `SUBMISSION.md`, 테스트와 `docs/git-history.txt`를 최종 상태로 갱신하고, 날짜가 있는 감사 문서에는 “최종 상태는 SUBMISSION 참조”를 표시합니다.
- 최건영이 승인 상태와 대화 해결을 확인한 뒤 정리 PR을 병합합니다.

## 6. 최종 확인

- [ ] #11, #19, #28, #29가 병합되고 정리 PR이 #26도 함께 닫음
- [ ] 다섯 명 모두 병합 PR 2개 이상, 타인 실질 리뷰 2개 이상, 자기 PR 피드백 반영 1회 이상
- [ ] 과거 PR 보완은 실제 작성자/리뷰어 계정에서 사실대로 남음
- [ ] 의도적 충돌 2회의 실제 commit·marker·결과가 기록됨
- [ ] amend/reset/revert/stash 4종에 상황·명령·결과·Why·주의점과 전원 이름/역할이 있음
- [ ] 함수 5개와 사용 예시가 최신 `main`에서 동작하고 전체 테스트가 통과함
- [ ] 팀이 [검증·AI 사용 기록](team-verification.md)을 읽고 오류를 정정함(미션 외 책임 분산용 확인)
- [ ] 최신 Git graph를 갱신한 뒤 타인 승인으로 정리 PR을 병합함
