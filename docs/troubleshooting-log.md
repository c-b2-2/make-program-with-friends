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