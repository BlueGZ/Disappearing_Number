nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
x = len(nums) + 1
y = len(nums)
k = []
count = [0 for i in range(x)]
for i in range(x):
    for j in range(y):
        if i == nums[j]:
            count[i] = 1
for i in range(x):
    if count[i] != 1:
        if i != 0:
            k.insert(i, i)
print(k)
