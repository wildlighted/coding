nums = [[1,2,3,4]]*5
'''
for i in range(len(nums)):
    if i % 2 != 0:
        nums[i]= nums[i][::-1]
print(nums)
'''

for row in nums:
    print(row)
    row.reverse()