#a = [6, 1, 2, 3, 5, 10, 78]
# def maxim(a):
#     max_1 = 0
#     for i in a:
#         if max_1 < i:
#             max_1 = i
#     return max_1

# flag = False
# n = int(input())
# for i in range(n):
#     x = int(input())
#     flag = (x % 10 == 0) or flag
# print(flag)


# f = bin(322) # 2
# print(f[2:])
# oct() # 8
# hex() # 16

# base = 2
# x = int(input())
# while x > 0:
#      digit = x % base
#      digit2 = str(digit)
#      print(digit2[::-1], end='')
#      x //= base


# def max2(x, y):
#     if x > y:
#         return x
#     return y
#
#
# def max3 (x, y ,z):
#     return max2(x, max2(y, z))
# f = max3(4, 100, 1000000)
# print(f)




#class Solution(object):
    # def canAliceWin(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: bool
    #     """
    #     c = 0
    #     b = 0
    #     for i in range(len(nums)):
    #         if nums[i] < 10:
    #             c += nums[i]
    #         else:
    #             b += nums[i]
    #     if c != b:
    #         return True
    #     return False



# def if_simple(x):
#      divisor = 2
#      while divisor < x:
#         if x % divisor == 0:
#             return False
#         divisor += 1
#         return True
#
# d = if_simple(25)
# print(d)



# def fatcor(a):
#     if a <= 1:
#         return 1
#     else:
#         return (a * (a - 1))


# a = [0] * 1000
# top = 0
# x = int(input())
# while x != 0:
#     a[top] = x
#     top += 1
#     x = int(input())
# for k in range(4,-1, -1):
#     print(a[k])




# n = int(input())
# a = [0] * n
# b = [0] * n
# for k in range(n):
#     a[k] = int(input())
# for k in range(n):
#     b[k] = a[k]
#
# c = a
# print(a)
# print(b)
# print(c)




# def array_search(a, n, x):
#        for k in range(n):
#            if a[k] == x:
#                return k
#        return -1
#
#
#
#
#
#
# def test_array_serch():
#     a1 = [1, 2, 3, 4, 5]
#     m = array_search(a1, 5, 8)
#     if m == -1:
#         print('ok')
#     else:
#         print('fail')
#
#
#
#
#
# test_array_serch()
# f = array_search([1, 2, 3, 4, 5, 6, 7], 7, 7)
# print(f)
#
#
# def invert_array(a, n):
#     for k in range(n):
#         a[k] = a[n-1-k]
#


# n = int(input())
# a = [0]*n
# b = [0]*n
# for i in range(n):
#     a[i] = int(input())
# for i in range(n):
#     b[i] = a[n-1-i]
#
#
#
# print(a, b)


# n = 5
# a = [1, 2, 3, 4, 5]
# tmp = a[0]  # Сохраняем последний элемент
# for i in range(n-1):  # Итерируемся в обратном порядке
#     a[i] = a[i+1]
# a[n-1] = tmp  # Первый элемент становится последним
# print(a)
#
#
#
# top = a[n-1]
# for i in range(n-2, -1,-1):
#     a[i+1] = a[i]
# a[0] = top
# print(a)


# n = 10
# a = [True] * n
# a[0] = a[1] = False
# for k in range(2,n):
#     if a[k]:
#         for m in range(2*k,n,k):
#             a[m] = False
# for k in range(n):
#     print(k,"-",'простое' if a[k] else "составное")






# l = 0
# u = 0
# s = str(input())
# for i in range(len(s)):
#     if s[i].islower():
#         l+=1
#     else:
#         u +=1
#
# if l >= u:
#     print(s.lower())
# else:
#     print(s.upper())
# def insert_sort(a):
# #сортировка вставками это алгоритм сортировки, в котором элементы входной последовательности просматриваются по одному,
# #и каждый новый поступивший элемент размещается в подходящее место среди ранее упорядоченных элементов
#     n = len(a)
#     for top in range(1,n):
#         k = top
#         while k > 0 and a[k-1] > a[k]:
#             a[k],a[k-1] = a[k-1], a[k]
#             k -= 1
#     return a
#
#
#
#
# def choose_sort(a):
# #Сортировка выбором — это алгоритм сортировки, который находит наименьший элемент из неотсортированной части массива
# # и меняет его местами с первым элементом этой части. Процесс повторяется для оставшихся элементов, пока весь массив
# # не будет отсортирован.
#     n = len(a)
#     for pos in range(0, n-1):
#         for k in range(pos+1,n):
#             if a[k] < a[pos]:
#                 a[k],a[pos] = a[pos],a[k]
#     return a
#
#
#
#
# def buble_sort(a):
# #Сортировка пузырьком — это простой алгоритм сортировки, который многократно проходит через список, сравнивая соседние
# # элементы и меняя их местами, если они находятся в неправильном порядке
#     n = len(a)
#     for bpass in range(1, n):
#         for k in range(0, n-bpass):
#             if a[k] > a[k+1]:
#                 a[k],a[k+1] = a[k+1],a[k]
#     return a
#
#
#
#
#
#
#
#
#
# a = insert_sort([2, 3, 5, 4, 1])
# n = choose_sort([5, 3, 2, 1, 4])
# v = buble_sort([[2, 3, 5, 4, 1]])
# print(a)
# print(n)
# print(v)
#
#
#
#
#
#
#
#
# def t(nums):
#     a = nums.sorted()
#     if a[0] >= a[1]:
#         v = a[1]
#         return nums.index(v)
#     else:
#         return -1













