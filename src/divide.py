def divide(a: float, b: float) -> float:
    """a를 b로 나눈 값을 반환합니다. b가 0이면 ValueError가 발생합니다."""
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return a / b
