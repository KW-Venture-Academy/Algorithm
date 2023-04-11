def solution(nums):
    answer = 0
    num = len(nums)
    max = num/2
    dic = {}
    for i in nums:
        if len(dic) == max:
            break
        dic[i] = 'visited'
    answer = len(dic)
    return answer