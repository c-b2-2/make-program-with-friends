# Conflict Resolution Log

2026-09-19 기준 Git 객체로 확인한 충돌 기록입니다. 과거 명령 전문이 없는 경우에는 실제 실행 기록과 이력에서 재구성한 절차를 구분합니다.

## 우발적으로 발생한 충돌

| 해결 커밋 | 파일과 원인 | 해결 결과 |
| --- | --- | --- |
| [`2507c00`](https://github.com/c-b2-2/make-program-with-friends/commit/2507c00cd475a452bbe8abf8003efd7851cd518a) | `src/main.py`: 곱셈과 덧셈 구현이 같은 부분을 수정 | 김보민이 두 함수를 유지 |
| [`fd980f2`](https://github.com/c-b2-2/make-program-with-friends/commit/fd980f2b4b6320e4407d85660b6ad52c9470950c) | `src/main.py`: 거듭제곱과 덧셈 구현이 같은 부분을 수정 | 김강현이 두 함수를 유지 |
| [`bad04f8`](https://github.com/c-b2-2/make-program-with-friends/commit/bad04f8b09c587af60a9e6ffd92b494cfac33c04) | `docs/CONTRIBUTING.md`: 협업 규칙 두 섹션이 같은 끝부분에 추가 | 김보민이 두 섹션을 유지 |

세 건은 `git show --remerge-diff <해결 커밋>`으로 충돌을 확인할 수 있습니다. 당시 터미널 명령 전문은 보존되지 않아 특정 실행 순서를 완료 사실로 주장하지 않습니다. 의도적 충돌 실습 횟수에도 포함하지 않습니다.

## 의도적 실습 1 — 같은 줄 충돌 확인

- 참여자: 이준혁 (`Cerhovah`, A), 최건영 (`00skgun`, B)
- 대상: `docs/conflict-practice.txt`의 `practice_1`
- 공통 시작 커밋: `32f1d9199c51e22de159bbd629b6ce693fe1792c`
- A 변경: `8213827284e6d7c37b1d4583e73246fc575d023a` — `use_option_a`
- B 변경: `33ecd38c09eb6e2158cba019c7d57d031d276dd9` — `use_option_b`
- B의 해결 병합: `4d112a4eeceb952ad9ef136097824b6290a983a4`

두 변경 커밋은 같은 부모에서 시작했습니다. `git show --remerge-diff 4d112a4`의 충돌 부분을 문서 표시용으로 두 칸 들여썼습니다.

```text
  <<<<<<< 33ecd38 (docs: 충돌 실습 1 참여자 B 변경)
  practice_1 = use_option_b
  =======
  practice_1 = use_option_a
  >>>>>>> 8213827 (docs: 충돌 실습 1 참여자 A 변경)
```

참여자가 제공한 명령 기록은 `git fetch origin` → `git merge --no-ff origin/feature/cerhovah-mission-completion` → `git status` → `git diff -- docs/conflict-practice.txt`입니다. 터미널 출력 전체는 남아 있지 않지만, 병합 커밋과 위 충돌은 Git 이력으로 확인됩니다. 두 선택을 함께 보존한다는 합의에 따라 최종 값을 `practice_1 = combine_both_options`로 정했습니다.

이준혁은 같은 시작점에서 같은 줄을 다르게 수정하면 자동 병합할 수 없음을 확인했고, 최건영은 양쪽 변경을 보고 마커를 제거한 뒤 합의한 값으로 병합했습니다. 상대 변경을 먼저 pull하면 이 실습에서 의도한 독립 분기가 사라질 수 있습니다.

## 실습 2 시도 — 동일 줄 충돌 증빙 미확인

- 이준혁의 변경 커밋 `19cd9f4758859beabcf536a6413efb0428481267`은 `practice_2 = document_results_first`를 기록했으나, 부모는 실습 1 해결 커밋 `4d112a4`가 아닌 `8213827`입니다.
- 병합 커밋 `2ae0b6c5e2ba26938bd5e76108c817b63c049f8d`의 부모는 `19cd9f4`와 `4d112a4`입니다. `git show --remerge-diff 2ae0b6c`에는 서로 인접한 `practice_1`·`practice_2` 변경이 한 부분에 묶인 충돌이 보이고, 다른 부모의 `practice_2`는 `undecided`입니다.
- 현재 접근 가능한 Git ref에서는 최건영의 `practice_2 = document_commands_first` 변경 커밋을 찾지 못했습니다. 최종 병합 파일에는 `practice_1 = combine_both_options`와 `practice_2 = document_commands_and_results`가 남아 있습니다.

따라서 병합 중 충돌 자체는 있었지만, **두 참가자가 `practice_2` 같은 줄을 각각 변경했다는 2회차 증빙은 확인되지 않습니다.** 실제 완료로 표시하려면 두 참가자가 같은 새 시작 커밋에서 `practice_2`를 서로 다르게 수정한 각자의 커밋과 해결 병합 커밋을 남기고, `git show --remerge-diff <해결 커밋>`에서 두 값을 확인해야 합니다. 확인 전에는 커밋 해시나 개인 학습 결과를 만들어 적지 않습니다.

## 검증 명령

```bash
git show --remerge-diff 4d112a4
git show --remerge-diff 2ae0b6c
git rev-list --parents -n 1 19cd9f4
git rev-list --parents -n 1 2ae0b6c
git log --all -- docs/conflict-practice.txt
```
