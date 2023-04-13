"""2. Дано натуральное число A > 1. 
Определите, каким по счету числом Фибоначчи оно является, """

# num = int(input("Input number: "))
# num1 = 1
# num2 = 1
# feb = 0
# count = 0
# while feb < num:
#     feb = num1 + num2
#     num1 = num2
#     num2 = feb
#     count += 1
# print("feb = ",feb,count )
# print(num == feb)
N = int(input())
#your code goes here
nums = list(range(1,N+1))
# print(nums[:-1:1])
res = 0
for i in nums:
    res += i

print(res)