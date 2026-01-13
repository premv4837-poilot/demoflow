# # # # # # light = input("Enter traffic light")
# # # # #
# # # # # if light =="green":
# # # # #     print("Go")
# # # # # elif light == "yellow":
# # # # #     print("Ready")
# # # # # elif light == "Red":
# # # # #     print("Stop")
# # # # # else:
# # # # #     print("LIGHT BROKEN")
# # # #
# # # # # age = int(input("Enter age"))
# # # # #
# # # # # if (age >= 18):
# # # # #     print("can vote")
# # # # # else:
# # # # #     print("Cannot vote")
# # # # #
# # # # # a = 10
# # # # # b = 20
# # # # # c = 30
# # # # #
# # # # # if a>=b and a>=c:
# # # # #     print("A is greater")
# # # # # elif b>c:
# # # # #     print("B is greater")
# # # # # else:
# # # # #     print("C is greater :",c)
# # # #
# # # # # num = int(input("Enter number"))
# # # # #
# # # # # if (num%2 == 0):
# # # # #     print("Prime")
# # # # # else:
# # # # #     print("ODD")
# # # # #
# # # # # str = "I'am a codder"
# # # # # rev_str = ""
# # # # #
# # # # # for i in str:
# # # # #     rev_str=i+rev_str
# # # # # print(rev_str)
# # # #
# # # # # i = 1
# # # # #
# # # # # while (i<=10):
# # # # #     print(i)
# # # # #     i+=1
# # # # #
# # # #
# # # # # num = int(input("Enter num"))
# # # # # i = 1
# # # # #
# # # # # while i<=10:
# # # # #     print(i*num)
# # # # #     i+=1
# # # #
# # # # # li = [1,2,3,4,5,6,6]
# # # # # x = 3
# # # # # i = 0
# # # # #
# # # # # while i<len(li):
# # # # #     if i ==x:
# # # # #         print("found")
# # # # #         break
# # # # #     else:
# # # # #         print("searching")
# # # # #     i+=1
# # # #
# # # # # set1 = {1,2,3,3,4,5,5}
# # # # #
# # # # # print(set1)
# # # # # pal = "madam"
# # # # # rev_str=""
# # # # # for i in pal:
# # # # #     rev_str = i + rev_str
# # # # #
# # # # # if rev_str == pal:
# # # # #     print("palindrome")
# # # # # else:
# # # # #     print("not palindrome")
# # # # #
# # # # # print(rev_str)
# # # #
# # # # # nums = [1,2,3,3,4]
# # # # # unique = []
# # # # #
# # # # # for i in nums:
# # # # #     if i not in unique:
# # # # #         unique.append(i)
# # # # # print(unique)
# # # #
# # # # #
# # # # # def cal (a,b):
# # # # #     print(a*b)
# # # # #     return a*b
# # # # #
# # # # # cal(2,9)
# # # #
# # # # class Student:
# # # #
# # # #     def __init__(self,name,per):
# # # #         self.name = name
# # # #         self.per = per
# # # #
# # # # s1 = Student("prem",20)
# # # # print(s1.name, s1.per)
# # # #
# # # # s2 = Student("rahul",30)
# # # # print(s2.name, s2.per)
# # #
# # # class parent:
# # #     a,b = 10,20
# # #     def add (Self):
# # #         print(Self.a+Self.b)
# # # class B (parent):
# # #     i,j=2,2
# # #     def multi (Self):
# # #         print(Self.i*Self.j)
# # #
# # #
# # # class C (B):
# # #     def div(Self,p,q):
# # #         Self.p=p
# # #         Self.q=q
# # #         print(Self.p/Self.q)
# # #
# # # c1 = C()
# # # c1.add()
# # # c1.multi()
# # # c1.div(10,20)
# #
# #
# # try :
# #     i = int(input("enter a num"))
# #     j = int(input("enter a num"))
# #     k = i/j
# #     print(k)
# # except ZeroDivisionError:
# #     print("Enter second no greater  than zero")
# #
# #
#
# # nums = [1,2,3,4,5,6,6]
# # unique = []
# #
# # for i in nums:
# #     if i not in unique:
# #         unique.append(i)
# # print(unique)
#
#
# numbers = [10,20,30,40,50]
# largest = numbers[0]
#
# for i in numbers:
#     if i>largest:
#         largest=i
# print(largest)

#
#
#
# nums = [10,20,30,40,50]
# x = 20
# idx = 0
#
# while idx < len(nums):
#     if nums[idx] == x:
#         print("X found at index", idx)
#         break
#     else:
#         print("Searching")
#         idx += 1

# str  = "progamming"
# unique = ""
#
# for i in str:
#     if i not in unique:
#         unique=unique+i
# print(unique)

# li = [10,20,30,40,50,60,70,70]
# unique = []
#
# for i in li:
#     if i not in unique:
#         unique.append(i)
# print(unique)

# str = "Programming"
# unique = ''
#
# for i in str:
#     if i not in unique:
#         unique=unique+i
# print(unique.upper())


# str = 'welcome to 123mphasis@123'
# alpha = ''
# num = ''
#
# for i in str:
#     if i.__contains__("@"):
#         print("true")
#     else:
#         continue
#     #     alpha+=i
#     # elif i.isnumeric():
#     #     num = num+i
    #

#
# print(alpha.upper())
# print(num)




# s = "automation"
# print(s[::-1])

# li = [10,20,30,40,50]
# largest = li[0]
#
# for i in li:
#     if i>=largest:
#         largest = i
#
# print(largest)

# lst = (1, 2, 3, 4, 2, 3)
# # dup = []
# #
# # for i in lst:
# #     if lst.count(i) > 1 and i not in dup:
# #         dup.append(i)
# #
# # print(dup)
# print(lst.count(2))

# str = "programming"
# unique = ''
#
# for i in str:
#     if i not in unique:
#         unique=unique+i
# print(unique)
#
#
# li = [1,2,3,4,4,5]
# uni = []
#
# for i in li:
#     if i not in uni:
#         uni.append(i)
# print(uni)

print(tuple(range(10)))













