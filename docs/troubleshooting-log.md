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

### 참여자

- 김강현

### 상황

실수로 추가한 파일을 커밋한 상황을 가정하고,
`git revert`로 해당 변경을 되돌리는 과정을 체험한다.

### 실습할 명령

검토용 초안이다. 작업 중인 변경은 커밋하거나 stash로 보관한 뒤 시작한다.
아래 브랜치와 파일 이름은 아직 사용하지 않은 상태를 전제로 한다.

```bash
git switch -c feature/revert-practice

# 실수로 파일을 추가하고 커밋한 상황 만들기
printf '잘못 추가한 내용\n' > revert-practice.txt
git add revert-practice.txt
git commit -m "chore: revert 실습용 파일 추가"
git log --oneline -2

# 방금 만든 커밋의 변경 되돌리기
git revert --no-edit HEAD

# 결과 확인하기
git log --oneline -3
git show --stat HEAD
git status
```

### 예상 결과

- 추가했던 `revert-practice.txt` 파일이 삭제된다.
- 원래 커밋은 남아 있고, 변경을 취소하는 `Revert` 커밋이 새로 생긴다.
- 작업 디렉터리에 커밋할 변경사항이 남지 않는다.

직접 체험한 뒤 이곳에 실제 실행 결과를 기록한다.

### 핵심 내용

`git revert`는 기존 커밋을 삭제하지 않고, 그 변경을 취소하는 새 커밋을 만든다.
`HEAD`는 최신 커밋을 뜻하며, `--no-edit`는 기본 커밋 메시지를 그대로 사용하는 옵션이다.
