#9-laboratoriya
#1-misol
# s = str(input('s = '))
# for i in range(len(s)):
#     if s[i]=='b':
#         print(i+1)
#         break

#2-misol
#funksiyasiz
# from functools import reduce
# from operator import mul
# a = list(map(int, input().split()))
# print(sum(a), reduce(mul,a))

#funksiya bilan
# a = list(map(int, input().split()))
# def sum_kop(a):
#     s=0
#     k=1
#     for i in a:
#         s += i
#         k *= i
#     return s, k
# print(sum_kop(a))