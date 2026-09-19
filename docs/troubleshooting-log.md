# Troubleshooting Log

## 시나리오: git stash / git stash pop

### 참여자
- 이준혁 (`Cerhovah`): 실습 실행·기록
- 김강현 (`kanghyki`): 브랜치 전환과 복원 결과 확인(팀 확인 필요)

### 상황
작업 중인 tracked·untracked 변경사항을 commit하지 않은 상태에서 다른 브랜치로 이동해야 하는 상황을 가정했다.

### 시도한 명령

```bash
git status --short
git stash -u
git stash list
git switch main
git switch feature/stash-practice
git stash pop
```

## 시나리오 : git reset --soft HEAD~1

### 참여자
- 김보민

### 상황
test로 branch를 생성후 test code를 삽입하고 commit한뒤 reset --soft HEAD~1을 이용해서 commit을 제거하였다.

### 시도한 명령
```bash
nengrafi@localhost:~/workspace/codyssey/B2-2$ git add .
nengrafi@localhost:~/workspace/codyssey/B2-2$ git commit -m "test:트러블슈팅 테 스트"
[test 2d64afc] test:트러블슈팅 테스트
 1 file changed, 2 insertions(+)
nengrafi@localhost:~/workspace/codyssey/B2-2$ git reset --soft HEAD~1
nengrafi@localhost:~/workspace/codyssey/B2-2$ git log --oneline -5
82ba2d7 (HEAD -> test, origin/feature/multiply_function, feature/multiply_function) fix:곱셈함수
2507c00 Merge branch 'main' into feature/multiply_function
8d8ca7f Merge pull request #21 from c-b2-2/feature/lee-conflict-guide
f8224fd Merge pull request #13 from c-b2-2/feature/add-function
e3b21a0 refactor: 덧셈 함수만 남기도록 정리
nengrafi@localhost:~/workspace/codyssey/B2-2$
```
git status --short
```

### 결과

`git stash list`에서 보관 항목을 확인했고, 원래 브랜치로 돌아온 뒤 `git stash pop`으로 작업 중 변경사항이 복원된 것을 `git status`로 확인했다. 이 결과는 PR #24 본문의 실제 검증 기록을 기준으로 보완했다.

### 왜 이 방법을 선택했는가

완성되지 않은 변경을 임시 commit으로 남기지 않으면서 다른 브랜치로 안전하게 이동하기 위해 stash를 사용했다. `-u`는 아직 추적하지 않은 파일도 함께 보관하기 위해 사용했다.

### 주의점

- `git stash pop`은 현재 작업과 겹치면 충돌할 수 있으므로 먼저 작업 트리가 깨끗한지 확인한다.
- 복원 결과를 확인하기 전 stash를 보존하려면 `pop` 대신 `git stash apply`를 사용하고, 확인 후 `git stash drop`으로 지운다.
- `-u`는 untracked 파일을 포함하지만 ignored 파일까지 포함하지는 않는다.


## 시나리오: git revert

### 참여자와 역할

- 김강현: 실습용 커밋 공유, revert 실행, 결과 확인 및 기록

### 상황

실수로 파일을 추가하고 원격에 push한 상황을 만들었다.
별도 feature 브랜치에서 `git revert`를 실행해 변경을 취소하고,
원래 커밋과 취소 커밋이 모두 이력에 남는지 확인했다.

### 실행한 명령

```bash
# docs/revert-practice-draft 브랜치에서 실습용 파일을 커밋하고 원격에 공유
printf '잘못 추가한 내용\n' > revert-practice.txt
git add revert-practice.txt
git commit -m "chore: revert 실습용 파일 추가"
git push origin docs/revert-practice-draft

# 취소 대상과 영향 확인: 실습 파일 하나에 한 줄 추가
git show --stat e5fa1a6
git show e5fa1a6:revert-practice.txt

# 별도 feature 브랜치에서 공유된 커밋 되돌리기
git switch -c feature/revert-practice
git revert --no-edit e5fa1a6

# 이력과 파일 상태 확인
git log --oneline -3
git status --short
git diff HEAD~2 HEAD
test ! -e revert-practice.txt && echo '실습 파일 삭제 확인'
```

### 실제 결과

```text
944e17d Revert "chore: revert 실습용 파일 추가"
e5fa1a6 chore: revert 실습용 파일 추가
39fc4eb docs: git revert 트러블슈팅 실습 초안 추가
```

- 원래 커밋: [e5fa1a6](https://github.com/c-b2-2/make-program-with-friends/commit/e5fa1a6e380df4e77e758fb1b7fe4ae592f3390f)
- revert 커밋: [944e17d](https://github.com/c-b2-2/make-program-with-friends/commit/944e17d234590a4d289d2fcaa85b642f6900c72b)
- `revert-practice.txt`의 `잘못 추가한 내용` 한 줄과 파일 자체가 삭제되었다.
- 삭제 확인 명령은 `실습 파일 삭제 확인`을 출력했다.
- revert 직후 `git status --short`와 `git diff HEAD~2 HEAD`는 출력이 없었다.
- 파일 상태는 실습 전으로 돌아왔으며, 계산기 코드는 변경되지 않았다.
- 충돌 없이 revert가 완료되었고, 원래 커밋 해시는 그대로 유지되었다.

### 알게 된 점

`git revert`는 기존 커밋을 삭제하지 않고, 그 변경을 취소하는 새 커밋을 만든다.
`reset`으로 브랜치를 과거로 이동하는 방식과 달리 공유 히스토리를 보존하며,
강제 push 없이 원격에 반영할 수 있다.
`--no-edit`는 기본 revert 커밋 메시지를 그대로 사용하는 옵션이다.

### PR 및 병합 상태

[PR #32](https://github.com/c-b2-2/make-program-with-friends/pull/32)에서 검토한다.
`feature/revert-practice`의 원래 커밋과 revert 커밋을 기존 PR 브랜치에 fast-forward로 반영한다.
현재 main 병합은 대기 중이다. 팀원 1명 이상의 Approve 후 **merge commit 방식**으로 병합해야
두 실습 커밋을 main 이력에도 유지할 수 있다. Squash merge는 사용하지 않는다.


## git commit --amend 실습

### 작성자
```
- 임효정
```

### git commit --amend 실습 전
```
3b60279 (HEAD -> feature/etc) add modulo function
e6104b4 feat: add power utility
3486a5a (origin/main, origin/HEAD, master) Merge pull request #6 from c-b2-2/feature/lee-subtract
0789bb8 Merge pull request #7 from c-b2-2/feature/5-add-main-py
18c3fd5 Merge pull request #4 from c-b2-2/docs/commit-guidelines
eee867a (origin/feature/lee-subtract) feat: add subtraction utility
4b7255d feat: add main py with hello world
de29726 (origin/docs/commit-guidelines) docs: 커밋 메시지 규칙 작성
```

### git commit --amend 실습 후
```
380c23a (HEAD -> feature/etc) feat: add modulo function
e6104b4 feat: add power utility
3486a5a (origin/main, origin/HEAD, master) Merge pull request #6 from c-b2-2/feature/lee-subtract
0789bb8 Merge pull request #7 from c-b2-2/feature/5-add-main-py
18c3fd5 Merge pull request #4 from c-b2-2/docs/commit-guidelines
eee867a (origin/feature/lee-subtract) feat: add subtraction utility
4b7255d feat: add main py with hello world
de29726 (origin/docs/commit-guidelines) docs: 커밋 메시지 규칙 작성
4251988 chore: init
```

## 시나리오: 최건영의 stash 보관·복원 검증

### 참여자와 수행 범위

- 최건영 (`00skgun`): 실습 요청. 아래 직접 재현 및 결과 확인은 아직 대기 중이다.
- Codex: 사용자 요청으로 로컬 명령 실행, 파일 복원 확인 및 기록 작성.
- 이 기록만으로 최건영이 직접 명령을 실행했다고 주장하지 않는다. 직접 재현 후 본인의 실제 결과와 배운 점을 추가한다.

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

- `-u`는 untracked 파일을 포함하지만 ignored 파일은 포함하지 않는다.
- apply는 stash를 삭제하지 않는다. 복원 내용을 확인한 다음 해당 항목을 drop한다.
- 다른 stash가 있다면 목록과 메시지를 확인해 실습 항목을 식별한다.
- apply 중 충돌하면 해결·검증이 끝나기 전에 보관본을 삭제하지 않는다.

### 최건영 직접 재현 및 확인 — 대기

현재 실습 파일이 untracked인 상태에서 위 명령을 직접 실행할 수 있다. 실행 전에 `git stash list`와 `git status --short`를 확인하고 대상 파일만 보관한다. 위 해시는 Codex 시연의 값이며 본인 실행 시 생성되는 해시로 별도 기록한다.

- 본인 실행 stash 해시: 미기록
- 보관 후 파일이 사라짐 / apply 후 두 줄 복원 / apply 후 stash 유지 / drop 후 해당 항목 제거: 확인 대기
- 본인이 이해한 `apply`와 `pop` 차이: 직접 작성 대기
