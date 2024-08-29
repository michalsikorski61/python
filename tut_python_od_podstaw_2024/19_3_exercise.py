import random 
# nums = [i* random(1,100) for i in range(1, 11)]
nums = [random.randint(1, 100) for i in range(1, 11)]
print(nums)
print('The largest number is:', max(nums))
print('The smallest number is:', min(nums))