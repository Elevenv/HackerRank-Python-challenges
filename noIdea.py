# There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers. 
# You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0. 
# For each  integer in the array, if i belongs to A , you add 1 to your happiness. If i belongs to B, you add -1 to your happiness.
# Otherwise, your happiness does not change. Output your final happiness at the end.

# Input
# 3 2
# 1 5 3
# 3 1
# 5 7

# Output : 
# 1

n,m = map(int,input().split())
l1 = list(map(int,input().split()))
s1 = set(map(int,input().split()))
s2 = set(map(int,input().split()))
hap = 0
for l in l1:
    if l in s1:
        hap+=1
    elif l in s2:
        hap-=1
    else:
        pass
print(hap)