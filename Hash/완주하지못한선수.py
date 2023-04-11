import collections
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    res = collections.Counter(participant) - collections.Counter(completion)
    answer = list(res)[0]
    return answer