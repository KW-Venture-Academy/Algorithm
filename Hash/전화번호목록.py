def solution(phone_book):
    answer = True
    hash = {}
    for i in phone_book:
        hash[i] = 1
    for i in phone_book:
        prefix=''
        for j in i:
            prefix+=j
            if prefix in hash and prefix != i:
                answer = False
    return answer