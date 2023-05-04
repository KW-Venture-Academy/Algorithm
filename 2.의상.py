#2.의상
def solution(clothes):
   Hash_clothes = {}
   for item in clothes:
       Hash_clothes[item[1]] = 0
   for cloth in clothes :
       if cloth[1] in Hash_clothes :
           Hash_clothes[cloth[1]] +=1
   number = 1
   for x in Hash_clothes.values():
       number *= x+1
   answer = number - 1
   return answer

