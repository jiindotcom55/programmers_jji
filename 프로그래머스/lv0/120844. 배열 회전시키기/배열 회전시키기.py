def solution(numbers, direction):
    answer = []
    n = len(numbers)
    if direction == "right":
        answer.append(numbers[n-1]) 
        answer = answer + numbers[:n-1]
    else:
        answer = answer + numbers[1:] 
        answer.append(numbers[0])
        
    return answer