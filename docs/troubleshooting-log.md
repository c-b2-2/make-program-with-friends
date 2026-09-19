# Troubleshooting Log

2026-09-19 기준 병합된 PR과 Git 이력에서 확인한 네 가지 실습입니다. 참가자의 터미널 기록에만 남은 명령은 그렇게 표시하고, Codex 실행을 팀원 직접 실행으로 바꾸어 적지 않습니다.

## `git commit --amend`

- **참여자·역할:** 임효정 (`gittul-123`)이 로컬 커밋 메시지 수정과 push 거절 상황을 실습·기록했습니다([PR #29](https://github.com/c-b2-2/make-program-with-friends/pull/29)).
- **상황:** 마지막 커밋의 메시지나 내용을 수정한 뒤 커밋 ID가 어떻게 달라지는지 확인합니다.
- **실행 명령:** PR에 기록된 순서는 일반 커밋 → `git commit --amend` → `git log --oneline -1` → push 후 다시 amend → 일반 push 거절 확인 → `git push --force-with-lease`입니다. 정확한 amend 옵션과 전체 터미널 출력은 저장소에 남아 있지 않습니다.
- **결과:** 참가자가 남긴 전후 로그에는 `3b60279`에서 `380c23a`로 커밋 ID가 바뀐 기록이 있습니다. PR 본문은 공유 커밋을 다시 amend한 후 non-fast-forward 거절과 `--force-with-lease` 성공도 보고합니다. 전후 단축 SHA와 해당 원격 push 출력은 현재 저장소의 Git ref만으로 다시 검증할 수 없습니다.
- **선택 이유:** 마지막 로컬 커밋을 바로잡기 위해 amend를 사용했습니다.
- **주의점·배운 점:** amend는 새 커밋 ID를 만듭니다. 공유 브랜치에서의 이력 재작성은 다른 사람 작업을 덮을 수 있으므로 팀 합의 없이 사용하지 않습니다. `--force-with-lease`도 공유 브랜치의 사전 합의를 대신하지 않습니다.

## `git reset --soft HEAD~1`

- **참여자·역할:** 김보민 (`nengrafi`)이 별도 `test` 브랜치에서 실습·기록했습니다([PR #28](https://github.com/c-b2-2/make-program-with-friends/pull/28)).
- **상황:** 로컬 실습 커밋을 취소하면서 파일 변경을 다시 커밋할 수 있게 남깁니다.
- **터미널 기록의 명령:**

```bash
git add .
git commit -m "test:트러블슈팅 테스트"
git reset --soft HEAD~1
git log --oneline -5
```

- **결과:** 참가자 로그에서 실습 커밋 `2d64afc` 생성 후 reset을 실행했고, 이어진 로그의 HEAD는 이전 커밋 `82ba2d7`입니다. reset 직후의 `git status` 출력은 보존되지 않아 변경이 실제로 staged였는지는 그 기록만으로 확인할 수 없습니다.
- **선택 이유:** `--soft`는 HEAD를 이전 커밋으로 옮기고 인덱스·작업 파일을 그대로 두는 방법이라 다시 커밋할 때 적합합니다.
- **주의점·배운 점:** 이미 공유한 커밋에는 reset을 사용해 원격 이력을 다시 쓰지 않습니다. 다음에는 `git status --short`로 staged 상태까지 기록해야 결과를 완전히 재현할 수 있습니다.

## `git revert`

- **참여자·역할:** 김강현 (`kanghyki`)이 실습용 변경을 원격에 공유하고 되돌린 뒤 결과를 기록했습니다([PR #32](https://github.com/c-b2-2/make-program-with-friends/pull/32)).
- **상황:** 실수로 공유한 `revert-practice.txt`를 기존 커밋을 지우지 않고 취소합니다.
- **실행 명령:**

```bash
git show --stat e5fa1a6
git revert --no-edit e5fa1a6
git log --oneline -3
git status --short
git diff HEAD~2 HEAD
test ! -e revert-practice.txt
```

- **결과:** 원래 커밋 [`e5fa1a6`](https://github.com/c-b2-2/make-program-with-friends/commit/e5fa1a6e380df4e77e758fb1b7fe4ae592f3390f)과 취소 커밋 [`944e17d`](https://github.com/c-b2-2/make-program-with-friends/commit/944e17d234590a4d289d2fcaa85b642f6900c72b)이 모두 `main` 이력에 남았습니다. 파일은 삭제됐고 실습 전후 파일 상태가 일치합니다.
- **선택 이유:** 공유된 커밋을 취소하면서 이력을 보존합니다.
- **주의점·배운 점:** `revert`는 과거 커밋을 삭제하지 않고 반대 변경을 담은 새 커밋을 만듭니다. 되돌릴 커밋과 영향을 먼저 확인해야 합니다.

## `git stash` / `git stash apply`·`pop`

- **참여자·역할:** 이준혁 (`Cerhovah`)의 stash·pop 실습은 [PR #24](https://github.com/c-b2-2/make-program-with-friends/pull/24)에 기록됐습니다. 최건영 (`00skgun`)은 [PR #36](https://github.com/c-b2-2/make-program-with-friends/pull/36)의 실습을 요청하고 결과 문서를 커밋했습니다. 아래 최건영 관련 명령의 **실행 주체는 Codex**이며 최건영의 직접 터미널 재현은 확인되지 않았습니다.
- **상황:** 미완성 변경을 임시 보관한 채 브랜치를 바꾸거나, 파일을 보관·복원합니다.
- **기록된 명령:**

```bash
# 이준혁의 stash·pop 실습 기록
git stash -u
git stash list
git switch main
git switch feature/stash-practice
git stash pop

# 최건영 요청으로 Codex가 실행한 untracked 파일 시연
git stash push -u -m "00skgun stash demonstration" -- docs/stash-practice-00skgun.txt
git stash apply 'stash@{0}'
git stash drop 'stash@{0}'
```

- **결과:** PR #24는 브랜치 복귀 후 변경 복원을 보고합니다. PR #36의 Codex 시연은 untracked 파일이 보관 후 사라지고 apply 후 두 줄로 복원되며 stash 항목이 유지되는 것을 확인했습니다. 시연 stash SHA는 `9e03ef0abab06b732fcd10b32b82f6c7bcba064c`입니다. 최건영이 작성한 후속 커밋 [`808fa9e`](https://github.com/c-b2-2/make-program-with-friends/commit/808fa9eb35db4ba67ae73765f4c3665caf2f1221)은 tracked 파일의 추가 검증을 기록하지만, 그 문서도 Codex 실행이라고 명시합니다. 관련 [PR #38](https://github.com/c-b2-2/make-program-with-friends/pull/38)은 열려 있으며 후속 커밋은 현재 `main`에 포함되지 않았습니다.
- **선택 이유:** `-u`는 추적되지 않은 파일까지 보관합니다. `apply`는 복원 확인 전까지 stash를 유지할 수 있어 시연에 적합했습니다.
- **주의점·배운 점:** `pop`은 적용 성공 시 보관 항목을 제거하지만 `apply`는 유지합니다. 복원을 확인하기 전 다른 stash를 잘못 지우지 않도록 목록과 메시지를 확인합니다. 최건영의 직접 실행 증빙은 별도 확인이 필요하며 Codex 실행을 개인 실습으로 세지 않습니다.
