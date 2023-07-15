def solution(numbers):
    answer = 0
    e = sorted(numbers,reverse=True)
    answer = e[0] * e[1]
    return answer