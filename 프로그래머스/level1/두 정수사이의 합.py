def solution(a, b):
    if a > b:
        a, b = b, a
    answer = []
    for i in range(a, b+1):
        answer.append(i)
        
    return sum(answer)