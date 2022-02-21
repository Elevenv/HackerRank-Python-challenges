# Given an integer, , and  space-separated integers as input, create a tuple
# of those  integers. Then compute and print the result of hash(t).

n = int(raw_input())
integer_list = map(int, raw_input().split())
t=tuple(integer_list)
print(hash(t))