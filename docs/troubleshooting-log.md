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

### git commit --amend 실습 후ㄴ
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

