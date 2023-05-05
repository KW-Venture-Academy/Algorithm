def solution(clothes):
    answer = 1
    hash = {}
    for i in clothes:
        hash[i[1]] = hash.get(i[1], 0) + 1
    for i in hash:
        answer *= (hash[i] +1)
    return answer-1