# Conflict Resolution Log

이 문서는 Git 커밋과 `git show --remerge-diff`로 확인되는 실제 충돌을 기록합니다.

> 아래 세 건은 **우발적으로 발생한 실제 충돌**입니다. 당시 터미널 명령 전문은 저장되지 않았으므로 명령 순서는 Git 히스토리를 바탕으로 재구성했습니다. 따라서 미션이 요구하는 “의도적으로 만든 충돌 실습 2회”에는 세지 않으며, 별도의 의도적 실습 2회가 필요합니다.

## 우발 충돌 1: 곱셈 함수와 덧셈 함수 통합

- 해결 커밋: [`2507c00`](https://github.com/c-b2-2/make-program-with-friends/commit/2507c00cd475a452bbe8abf8003efd7851cd518a)
- 해결자: 김보민 (`nengrafi`)
- 브랜치/파일: `feature/multiply_function`, `src/main.py`
- 충돌 원인: 기능 브랜치의 곱셈 구현과 `main`의 덧셈 구현이 파일 시작의 같은 hunk를 서로 다르게 수정했습니다.

히스토리로 재구성한 절차:

```bash
git switch feature/multiply_function
git fetch origin
git merge origin/main
git status
# src/main.py에서 충돌 마커를 제거하고 두 함수를 함께 유지
git add src/main.py
git commit
```

서로 다른 기능이므로 한쪽을 버리지 않고 곱셈과 덧셈을 모두 유지했습니다. 이후 import 시 출력되는 임시 코드와 함수 인터페이스는 별도 수정 대상이 되었습니다. 작은 함수라도 같은 파일 상단을 함께 수정하면 충돌할 수 있으므로 최신 `main`을 먼저 반영하고, 해결 뒤 두 함수 모두를 실행해야 한다는 점을 배웠습니다.

## 우발 충돌 2: 거듭제곱 함수와 덧셈 함수 통합

- 해결 커밋: [`fd980f2`](https://github.com/c-b2-2/make-program-with-friends/commit/fd980f2b4b6320e4407d85660b6ad52c9470950c)
- 해결 커밋 작성자: 김강현 (`kanghyki`)
- 기능 작성자: 임효정 (`gittul-123`)
- 브랜치/파일: `feature/etc`, `src/main.py`
- 충돌 원인: 거듭제곱 함수와 `main`의 덧셈 함수가 파일 시작의 같은 hunk를 수정했습니다.

히스토리로 재구성한 절차:

```bash
git switch feature/etc
git fetch origin
git merge origin/main
git status
# src/main.py에서 power와 add를 모두 남기고 충돌 마커 제거
git add src/main.py
git commit
```

두 함수의 역할이 겹치지 않아 양쪽 구현을 모두 유지했습니다. 다만 충돌 해소는 “마커 제거”로 끝나지 않으며, 합쳐진 파일의 불필요한 최상위 출력까지 검토해야 한다는 점을 배웠습니다.

## 우발 충돌 3: 두 협업 규칙 섹션 통합

- 해결 커밋: [`bad04f8`](https://github.com/c-b2-2/make-program-with-friends/commit/bad04f8b09c587af60a9e6ffd92b494cfac33c04)
- 해결자: 김보민 (`nengrafi`)
- 브랜치/파일: `feature/code_review_rule`, `docs/CONTRIBUTING.md`
- 충돌 원인: 코드 리뷰 규칙과 충돌 대응 규칙이 문서 끝의 같은 hunk에 각각 추가됐습니다.

히스토리로 재구성한 절차:

```bash
git switch feature/code_review_rule
git fetch origin
git merge origin/main
git status
# 두 문서 섹션을 모두 유지하도록 순서를 정리하고 마커 제거
git add docs/CONTRIBUTING.md
git commit
```

두 섹션 모두 협업 지침에 필요해 하나를 선택하지 않고 순서대로 합쳤습니다. 문서도 같은 끝부분에 동시에 내용을 추가하면 코드처럼 충돌하며, 제목 단계와 문장 연결까지 함께 확인해야 한다는 점을 배웠습니다.

## 의도적 충돌 실습 1 

참여자 A 실제 이름 / GitHub ID:
이준혁 / Cerhovah

참여자 B 실제 이름 / GitHub ID:
최건영 / 00skgun

실습 1 시작 hash:
32f1d9199c51e22de159bbd629b6ce693fe1792c

A commit hash:
8213827284e6d7c37b1d4583e73246fc575d023a

B commit hash:
33ecd38c09eb6e2158cba019c7d57d031d276dd9

실습 1 merge commit hash:
4d112a4eeceb952ad9ef136097824b6290a983a4

실제 사용 명령:
git fetch origin
git merge --no-ff origin/feature/cerhovah-mission-completion
git status
git diff -- docs/conflict-practice.txt

충돌 marker:
<<<<<<< HEAD
practice_1 = use_option_b
=======
practice_1 = use_option_a
>>>>>>> origin/feature/cerhovah-mission-completion

최종 선택:
practice_1 = combine_both_options

선택 이유:
두 참가자가 같은 시작 상태에서 practice_1 한 줄을 서로 다른 값으로 수정하여 충돌을 재현했고, 두 변경을 확인한 뒤 합의한 결과를 practice_1 = combine_both_options로 정리함.

결과:
참여자 A가 practice_1 = use_option_a 변경을 commit·push하고, 참여자 B가 같은 시작점에서 practice_1 = use_option_b를 별도로 commit한 뒤 원격 브랜치를 merge하여 실제 content conflict를 발생시킴. 충돌을 합의된 값으로 해결한 뒤 merge commit을 생성하고 원격 브랜치에 push함.

주의점:
충돌을 해결할 참가자는 상대가 먼저 push한 변경을 미리 pull하지 않아야 함. 같은 시작 commit에서 각각 독립적으로 변경을 commit한 뒤 fetch와 merge를 해야 의도한 동일 줄 충돌을 재현할 수 있음.

각자 배운 점:
이준혁: 같은 시작 commit에서 동일한 줄을 서로 다르게 수정하면 Git이 자동으로 어느 변경을 선택할지 결정할 수 없어 실제 content conflict가 발생한다는 것을 확인함.

최건영: 충돌 발생 후 HEAD와 원격 변경의 차이를 직접 확인하고, 충돌 marker를 제거한 뒤 합의한 최종 내용을 선택하여 add → commit → push 순서로 충돌을 해결하는 과정을 확인함.

## 의도적 충돌 실습 2 — 완료

- 참여자 A 실제 이름·GitHub ID: `이준혁 / Cerhovah`

- 참여자 B 실제 이름·GitHub ID: `최건영 / 00skgun`

- 역할: 참여자 B(첫 commit·push), 참여자 A(두 번째 commit·충돌 해결)

- 대상: `docs/conflict-practice.txt`의 `practice_2` 한 줄

- 시작 commit: `4d112a4eeceb952ad9ef136097824b6290a983a4`

- 참여자 B commit: `[최건영 측 실습 2 B commit hash 입력]`

- 참여자 A commit: `19cd9f4758859beabcf536a6413efb0428481267`

- 해결 merge commit: `2ae0b6c5e2ba26938bd5e76108c817b63c049f8d`

- 실제 수행 명령:

```bash
git fetch origin
git merge --no-ff origin/feature/cerhovah-mission-completion
git status
git diff -- docs/conflict-practice.txt
## 검증 방법

각 과거 충돌은 다음 명령으로 다시 확인할 수 있습니다.

```bash
git show --remerge-diff 2507c00
git show --remerge-diff fd980f2
git show --remerge-diff bad04f8
```
