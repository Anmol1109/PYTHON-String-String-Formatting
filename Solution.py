def print_formatted(number):
    spacing = len(bin(number)[2:])
    for i in range(1,number+1):
        print(str(i).rjust(spacing,' '), str(oct(i)[2:]).rjust(spacing,' '), str(hex(i)[2:].upper().rjust(spacing,' ')), str(bin(i)[2:]).rjust(spacing,' '))
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
