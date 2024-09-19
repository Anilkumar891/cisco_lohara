from functools import reduce
nums=[10,20,30,40]
nums_sum=reduce(lambda s,num:s+num,nums,0)
nums_prod=reduce(lambda p,num:p*num,nums,1)
print(nums_sum,nums_sum)

import sys
nums_min=reduce(lambda m,num:min(m,num),nums,sys.maxsize)
nums_max=reduce(lambda m,num:max(m,num),nums,-sys.maxsize)
print(nums_min,nums_max)


nums_min = reduce(min,nums)
nums_max=reduce(max,nums)
print(nums_max,nums_min)
