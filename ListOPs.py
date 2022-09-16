# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each 
# command will be of the  types listed above. Iterate through each command in order and perform 
# the corresponding operation on your list

n = int(input())
List = []

for i in range(n):
    choice = input().split()
    if choice[0] == 'insert':
        List.insert(int(choice[1]),int(choice[2]))
    elif choice[0] == 'print':
        print(List)
    elif choice[0] == 'remove':
        List.remove(int(choice[1]))
    elif choice[0] == 'append':
        List.append(int(choice[1]))
    elif choice[0] == 'sort':
        List.sort()
    elif choice[0] == 'reverse':
        List.reverse()
    elif choice[0] == 'pop':
        List.pop()
    else:
        pass
