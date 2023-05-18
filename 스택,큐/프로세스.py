#프로세스
def solution(priorities, location):
    answer = 0
    li = []
    for i in range(len(priorities)):
        li.append((i,priorities[i]))
    while True:
        element = li.pop(0)
        if any(element[1]< prior[1] for prior in li):
            li.append(element)
        else :
            answer += 1
            if element[0] == location:
                break
    
    return answer