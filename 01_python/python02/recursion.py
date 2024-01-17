def factorial(n):
#    종료 조건:    n이 0이면 1을 반환
    if n == 0:
        return 1
#    재귀 호출:    n과 n-1의 팩토리얼을 곱한 결과를 반환
    return n * factorial(n - 1)
#    팩토리얼 계산 예시
    # 함수 호출 : 표현식 -> 평가에 의해 값이 정해짐 : 정해진 값 하나
result = factorial(5)