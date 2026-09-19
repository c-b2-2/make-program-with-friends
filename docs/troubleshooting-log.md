# Troubleshooting Log

## 시나리오: git stash / git stash pop

### 참여자
- 이준혁
- 강현

### 상황
작업 중인 변경사항을 commit하지 않은 상태에서
다른 브랜치로 이동해야 하는 상황을 가정했다.

### 시도한 명령

```bash
git stash
git stash list
git switch main
git switch feature/stash-practice
git stash pop
```

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
