import sys
sys.stdin = open("input.txt","r")
k = int(sys.stdin.readline())
nums = [None]*k
ptr = 0 

for i in range(k):
    num = int(sys.stdin.readline())
    if num != 0 :
        nums[ptr] = num
        ptr += 1
    else :
        del nums[ptr-1]
        ptr -=1

sum_nums =0
for i in range(len(nums)):
    if nums[i] == None:
        break
    sum_nums += nums[i]
print(sum_nums)
        