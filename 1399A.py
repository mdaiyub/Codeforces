n = int(input())

for i in range(n):
    leng = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    mark = 0
    for j in range(len(nums) - 1):
        if abs(nums[j + 1] - nums[j]) > 1:
            mark = 1
            break
    if mark == 0:
        print('YES')
    else:
        print('NO')


