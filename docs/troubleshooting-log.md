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
