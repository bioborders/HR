def print_formatted(number):
    a = len(bin(number)[2:])

    for i in range(1, number + 1):
        print(str(i).rjust(a, ' '), end=" ")
        print(oct(i)[2:].rjust(a, ' '), end=" ")
        print(((hex(i)[2:]).upper()).rjust(a, ' '), end=" ")
        print(bin(i)[2:].rjust(a, ' '), end=" ")
        print("")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
