import sys
input = sys.stdin.readline
n = int(input())
s = [int(input()) for i in range(n)]
u = list(set(s))
u.sort()
print(u[-3], s.count(u[-3]))