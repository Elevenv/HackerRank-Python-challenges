# # Enter your code here. Read input from STDIN. Print output to STDOUT
i = int(input())
s1 = set(map(int,input().split()))
j = int(input())
s2 = set(map(int,input().split()))
s3 = s1.difference(s2)
print(s3)
print(len(s3))

# eng_num = int(raw_input())
# eng_set = set(map(int, raw_input().split()))
# fren_num = int(raw_input())
# fren_set = set(map(int, raw_input().split()))

# print(len(eng_set.difference(fren_set)))