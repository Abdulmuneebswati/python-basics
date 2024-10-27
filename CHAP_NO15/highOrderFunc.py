# squared_nums = list(map(lambda x : x*x ,numbers))
# odd_nums = list(filter(lambda x : x % 2 != 0 ,numbers))
# print(odd_nums)
from functools import reduce

numbers = [3,4,5,6,7,8,9]
reduce_nums = reduce(lambda x,y: x + y,numbers)

print(reduce_nums)