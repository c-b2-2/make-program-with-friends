# Conflict Resolution Log

이 문서는 Git 커밋과 `git show --remerge-diff`로 확인되는 실제 충돌을 기록합니다.

> 아래 세 건은 **우발적으로 발생한 실제 충돌**입니다. 당시 터미널 명령 전문은 저장되지 않았으므로 명령 순서는 Git 히스토리를 바탕으로 재구성했습니다. 따라서 미션이 요구하는 “의도적으로 만든 충돌 실습 2회”에는 세지 않습니다. 의도적 실습은 아래에 별도로 기록합니다.

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

## 의도적 충돌 실습 1 — 확인됨

- 참여자: A 이준혁 (`Cerhovah`), B 최건영 (`00skgun`)
- 역할: A가 먼저 변경하고, B가 독립적으로 변경한 뒤 병합 충돌을 해결
- 대상: `docs/conflict-practice.txt`의 `practice_1`
- 공통 시작 커밋: `32f1d9199c51e22de159bbd629b6ce693fe1792c`
- A 변경 커밋: `8213827284e6d7c37b1d4583e73246fc575d023a` — `use_option_a`
- B 변경 커밋: `33ecd38c09eb6e2158cba019c7d57d031d276dd9` — `use_option_b`
- B의 해결 병합 커밋: `4d112a4eeceb952ad9ef136097824b6290a983a4`

두 변경 커밋의 부모가 같은 시작 커밋입니다. `git show --remerge-diff 4d112a4`로 확인한 충돌 부분은 다음과 같습니다. 마커 옆의 커밋 표시는 Git이 병합을 재현하며 붙인 값이며, 아래 예시는 문서용으로 두 칸 들여썼습니다.

```text
  <<<<<<< 33ecd38 (docs: 충돌 실습 1 참여자 B 변경)
  practice_1 = use_option_b
  =======
  practice_1 = use_option_a
  >>>>>>> 8213827 (docs: 충돌 실습 1 참여자 A 변경)
```

참여자가 제공한 명령 기록은 `git fetch origin`, `git merge --no-ff origin/feature/cerhovah-mission-completion`, `git status`, `git diff -- docs/conflict-practice.txt` 순서입니다. 터미널 출력 전체는 보존되지 않았지만, Git 이력에서 같은 줄 충돌과 해결 결과를 독립적으로 확인했습니다. 두 선택의 의미를 함께 보존하기 위해 `practice_1 = combine_both_options`로 정리했습니다.

이준혁은 같은 시작점에서 같은 줄을 다르게 수정하면 Git이 자동으로 선택할 수 없음을 확인했고, 최건영은 마커 양쪽을 확인해 합의한 값으로 정리한 뒤 병합 커밋을 남기는 과정을 수행했습니다. 충돌을 재현하려면 먼저 push된 변경을 다른 참가자가 자신의 커밋 전에 pull하지 않아야 합니다.

## 의도적 충돌 실습 2 시도 — 계획과 이력이 다름

- 계획: 실습 1 해결 커밋 `4d112a4`에서 두 사람이 시작해 `practice_2`를 서로 다르게 수정하고, 이준혁이 충돌을 해결
- 확인된 A 변경 커밋: `19cd9f4758859beabcf536a6413efb0428481267` — `practice_2 = document_results_first`
- 확인된 병합 커밋: `2ae0b6c5e2ba26938bd5e76108c817b63c049f8d` — 최종 파일은 `practice_2 = document_commands_and_results`
- B의 `practice_2 = document_commands_first` 변경 커밋: 이 병합 이력에서 확인되지 않음

`19cd9f4`의 부모는 실습 1 해결 커밋이 아닌 `8213827`입니다. `2ae0b6c`의 다른 부모는 실습 1 해결 커밋 `4d112a4`이고, 이쪽의 `practice_2` 값은 아직 `undecided`입니다. 따라서 두 사람이 실습 1 해결 결과에서 같은 줄을 각각 수정했다는 설명은 이 Git 이력과 맞지 않습니다.

`git show --remerge-diff 2ae0b6c`에는 실제 content conflict가 표시됩니다. 다만 그 충돌에는 실습 1의 `practice_1` 값 차이가 포함되며, `practice_2`는 A 쪽에서만 변경됐습니다.

```text
  <<<<<<< 19cd9f4 (docs: 충돌 실습 2 참여자 A 변경)
  practice_1 = use_option_a
  practice_2 = document_results_first
  =======
  practice_1 = combine_both_options
  practice_2 = undecided
  >>>>>>> 4d112a4 (docs: 충돌 실습 1 해결)
```

병합 결과 파일의 `practice_1 = combine_both_options`와 `practice_2 = document_commands_and_results`는 확인됐습니다. 그러나 계획한 **두 사람의 `practice_2` 동일 줄 충돌**은 확인되지 않아 실습 2 완료 증빙으로 세지 않습니다. 두 참가자가 현재 공유 브랜치의 같은 커밋에서 다시 시작해 각자 `practice_2`를 수정하고, 변경 커밋 2개와 해결 병합 커밋을 남겨야 합니다. 진행 내용은 [Issue #33](https://github.com/c-b2-2/make-program-with-friends/issues/33), 절차는 [최종 마무리 실행표](human-actions.md)에 있습니다.

## 검증 방법

```bash
git show --remerge-diff 2507c00
git show --remerge-diff fd980f2
git show --remerge-diff bad04f8
git show --remerge-diff 4d112a4
git show --remerge-diff 2ae0b6c
git rev-list --parents -n 1 19cd9f4
git rev-list --parents -n 1 2ae0b6c
```
