import sys

N = int(input())

num = []

for _ in range(N):
    # num.append(int(input))
    num.append(int(sys.stdin.readline()))

sorted_num = sorted(num)

for i in sorted_num:
    print(i)