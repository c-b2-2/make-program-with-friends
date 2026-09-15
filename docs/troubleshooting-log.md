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