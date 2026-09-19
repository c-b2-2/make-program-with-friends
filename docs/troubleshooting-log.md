# Troubleshooting Log

2026-09-19 기준 병합된 PR과 Git 이력에서 확인한 amend·reset·revert·stash 실습입니다. stash는 브랜치 전환, untracked 파일, tracked 수정분을 각각 기록합니다. 참가자의 터미널 기록에만 남은 명령은 그렇게 표시하고, Codex 실행을 팀원 직접 실행으로 바꾸어 적지 않습니다.

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

## `git stash` / `git stash pop`: 이준혁의 브랜치 전환 실습

- **참여자·역할:** 이준혁 (`Cerhovah`)이 실습과 기록을 맡았습니다([PR #24](https://github.com/c-b2-2/make-program-with-friends/pull/24)). 김강현 (`kanghyki`)의 브랜치 전환·복원 결과 확인은 원문에 `팀 확인 필요`로 적혀 있어 완료된 역할로 세지 않습니다.
- **상황:** 커밋하지 않은 tracked·untracked 변경을 임시 보관하고 다른 브랜치로 이동합니다.
- **기록된 명령:**

```bash
git status --short
git stash -u
git stash list
git switch main
git switch feature/stash-practice
git stash pop
git status --short
```

- **결과:** PR #24 본문은 `stash list`에서 보관 항목을 확인하고, 원래 브랜치 복귀 후 `stash pop`으로 변경을 복원했다고 기록합니다. 터미널 전체 출력은 남아 있지 않습니다.
- **선택 이유:** 임시 커밋 없이 브랜치를 바꾸기 위해 stash를 사용했습니다. `-u`는 untracked 파일을 포함합니다.
- **주의점:** `pop`은 적용 성공 시 stash를 제거하며 현재 변경과 겹치면 충돌할 수 있습니다. 복원을 검증하기 전 보관본을 유지하려면 `apply`를 사용하고 확인 후 `drop`합니다. `-u`는 ignored 파일을 포함하지 않습니다.

## 시나리오 1: 최건영 요청 — untracked 파일의 stash 보관·복원

### 참여자와 수행 범위

- 최건영 (`00skgun`): stash 실습 요청.
- Codex: 사용자 요청에 따라 명령 실행, 파일 복원 확인 및 기록 작성.
- 최건영이 직접 터미널 명령을 실행한 기록은 아니며, 직접 수행·학습 소감은 별도로 확인하지 않았다.

### 상황과 선택 이유

새로 만든 미완성 파일을 잠시 치웠다가 복원하는 상황이다. 아직 추적되지 않은 파일이므로 `-u`를 사용했다. 복원 확인 전 보관본을 유지하기 위해 `pop` 대신 `apply`를 선택했다.

### 실행 환경과 명령

- 날짜: 2026-09-19
- 브랜치: `feature/00skgun-stash-practice`
- 시작 커밋: `7e2731be178d8b68aa3868b0c4e605e242729486`
- 대상: `docs/stash-practice-00skgun.txt` 한 파일
- 시작 당시 기존 stash와 작업 트리 변경 없음.

```bash
git status --short
git stash push -u -m "00skgun stash demonstration" -- docs/stash-practice-00skgun.txt
git stash list
git rev-parse 'stash@{0}'
git stash apply 'stash@{0}'
git stash list
git status --short
# 파일 내용 복원을 확인한 다음 실행
git stash drop 'stash@{0}'
git stash list
```

### 실제 관찰 결과

- 시작 상태: `?? docs/stash-practice-00skgun.txt`
- stash 생성 후 PowerShell `Test-Path docs/stash-practice-00skgun.txt`: `False`.
- 생성된 stash 해시: `9e03ef0abab06b732fcd10b32b82f6c7bcba064c`.
- apply 후 아래 두 줄이 복원됐고 파일은 다시 untracked 상태였다.

```text
participant = 00skgun
practice = stash untracked file and restore safely
```

- apply 후에도 `git stash list`에 보관 항목이 남았다.
- 복원 확인 후 이번 실습 stash만 drop했고, 최종 stash 목록은 비어 있다. 복원 파일은 유지했다.

### 주의점

- untracked 파일은 기본 stash 대상이 아니므로 `-u`가 필요하다. ignored 파일은 `-u`로 포함되지 않는다.
- 대상 경로를 지정하여 다른 작업 파일이 함께 보관되지 않도록 한다.
- `apply` 후 파일 내용과 untracked 상태를 확인한 다음 해당 stash만 삭제한다.

## 시나리오 2: 최건영 요청 — tracked 수정분의 stash·apply·blob 비교·drop 검증

### 참여자와 수행 범위

- 최건영 (`00skgun`): 추가 보관·복원 검증 실행 요청.
- Codex: tracked 파일 수정, stash와 apply 실행, Git blob 해시 비교, 검증 후 drop 및 결과 기록.
- 이 기록은 최건영의 요청과 Codex의 실행을 구분한다. 최건영 본인의 직접 실행이나 이해도 확인을 대신하지 않는다.

### 상황과 선택 이유

시나리오 1 이후 파일이 커밋되어 tracked 상태가 됐다. 이번에는 기존 파일에 추가한 수정분만 잠시 보관하고 정확히 복원되는지 검증했다. untracked 파일을 보관하는 실습과 달리 `-u` 없이 대상 경로를 지정했다. 복원 내용을 검증할 때까지 보관본을 유지하기 위해 `apply`를 선택했다.

### 실행 환경과 준비

- 날짜: 2026-09-19
- 실행 당시 브랜치: `feature/00skgun-stash-practice`
- 시작 커밋: `1a21ad1cc061cbfa4f5d367e46e08c65141cb45c`
- 대상: tracked 파일 `docs/stash-practice-00skgun.txt`
- 수정 전 작업 트리는 깨끗했고 stash 목록은 비어 있었다.
- 기존 두 줄을 유지하고 아래 한 줄을 추가한 뒤 명령을 실행했다.

```text
verification = tracked change restored with stash apply
```

### 실제 실행 명령

```powershell
git diff -- docs/stash-practice-00skgun.txt
git stash push -m "00skgun requested stash verification" -- docs/stash-practice-00skgun.txt
git rev-parse "stash@{0}"
Get-Content docs/stash-practice-00skgun.txt
git status --short
git stash apply "stash@{0}"
Get-Content docs/stash-practice-00skgun.txt
git stash list
git rev-parse "stash@{0}:docs/stash-practice-00skgun.txt"
git hash-object --path=docs/stash-practice-00skgun.txt docs/stash-practice-00skgun.txt
# 위 두 Git blob 해시가 일치하는 것을 확인한 뒤 실행
git stash drop "stash@{0}"
git stash list
```

### 검증 결과

- stash 해시: `e8e08143125f54a8e1b6c9324c44146573c19233`.
- 보관 후 파일 자체는 남고 추가한 verification 줄만 사라졌다. tracked 파일의 수정분을 보관했기 때문이다.
- 보관 직후 `git status --short`는 출력이 없었다.
- apply 후 verification 줄이 복원됐고 기존 두 줄도 유지됐다.
- apply 후에도 stash 목록에 이번 보관 항목이 남았다.
- Windows 줄바꿈 변환 때문에 SHA256 파일 바이트 해시는 달랐다. 저장소 줄바꿈 규칙을 적용한 `git hash-object --path`와 stash의 blob 해시가 일치해 Git 기준 내용 복원을 확인했다.
- 두 명령에서 확인한 Git blob 해시: `e2a48afdd8b03af69533ff3595d7fbc7bcb22086`.
- 복원 확인 후 이번 stash를 drop했고 최종 stash 목록은 비었다. 복원된 수정은 실습 파일에 남겼다.

### 주의점

- tracked 파일의 수정분은 `-u` 없이 보관할 수 있으며, 보관 후 파일 자체가 사라지는 것이 아니라 커밋된 내용으로 돌아간다.
- 실행 전에 `git status --short`와 `git stash list`를 확인한다. 다른 stash가 있다면 메시지와 해시로 대상 항목을 식별하고 `stash@{0}`을 무조건 사용하지 않는다.
- `apply` 중 충돌하거나 내용이 일치하지 않으면 stash를 삭제하지 않는다. 복원 내용과 blob 해시를 확인한 뒤 검증한 항목만 drop한다.
- Git blob 해시 일치는 저장소 규칙으로 정규화된 내용의 일치를 의미하며, 작업 파일의 줄바꿈까지 바이트 단위로 같다는 뜻은 아니다.
- `drop`은 보관본을 제거하므로 복원 검증 전에 실행하지 않는다.

### 확인한 원리와 기록 범위

검증으로 확인한 원리: `apply`는 복원 후에도 보관본을 유지하므로 결과를 확인한 다음 삭제할 수 있다. `pop`은 적용이 성공하면 보관 항목을 제거한다. 최건영의 직접 수행·학습 소감은 별도로 확인하지 않았다.
