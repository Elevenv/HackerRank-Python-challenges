# https://www.hackerrank.com/challenges/word-order/problem

# n = 4
# s = ["bcdef","abcdefg","bcde","bcdef"]

n = int(input())
s = []

for _ in range(n):
    s.append(input())
    
unique = len(set(s))
print(unique)

d = {}

for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i] = 1

for i in d.values():
    print(i,end=' ')
