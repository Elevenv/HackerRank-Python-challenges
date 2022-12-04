# Given an integer, n, print the following values for each integer i from 1 to n:

# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary



# def print_formatted(n):
#     for i in range(1,n+1):
#         binary = bin(i)
#         octal = oct(i)
#         hexa = hex(i)
#         print(i,'\t',str(octal[2:]),'\t',str(hexa[2:]),'\t',str(binary[2:]))
        
# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)


def print_formatted(number):
    
    l1 = len(bin(number)[2:])
   
    for i in range(1,number+1):
        print(str(i).rjust(l1,' '),end=" ")
        print(oct(i)[2:].rjust(l1,' '),end=" ")
        print(((hex(i)[2:]).upper()).rjust(l1,' '),end=" ")
        print(bin(i)[2:].rjust(l1,' '),end=" ")
        print("")
        

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)