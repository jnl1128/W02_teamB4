from curses import pair_content
import sys
import itertools
sys.stdin = open('B2470/input_lwh.txt', 'r')
input = sys.stdin.readline

# 이분탐색 !!


# def nCr(N):
#     return N*(N-1)//2
nCr = itertools.combinations

def find_pair():
    min = 0
    max = len(cases) - 1
    while True:
        mid = (min + max) // 2
        value = sum(cases[mid])
        if value == 0:
          return cases[mid]
        elif value < 0:
          min = mid + 1
          low_ans = mid
        else:
          max = mid - 1
          high_ans = mid
        if min > max:
          break
    
    if abs(sum(cases[low_ans])) > abs(sum(cases[high_ans])):
        return cases[high_ans]
    else:
        return cases[low_ans]

N = int(input())
attr_list = list(map(int, input().split()))
attr_list = sorted(attr_list)
# cases_amount = nCr(N*(N-1)//2)
cases = list(nCr(attr_list, 2))
print(cases)
print(find_pair())
