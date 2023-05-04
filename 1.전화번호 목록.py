#1.전화번호 목록
def solution(phone_book):
   Hash_phone_book = set()
   for _ in phone_book:
       Hash_phone_book.add(_)
   for phone_number in Hash_phone_book :
       pre_number= ''
       for number in phone_number:
           pre_number += number
           if pre_number in Hash_phone_book and pre_number != phone_number:
               return False
   return True