#  3 ways to make a pascal's triangle

# 1. Factorials

from math import factorial

n = int(input('Number of Rows: '))
for i in range(n):
    for j in range(n - i + 1):
        # for left spacing
        print(end=" ")

    for j in range(i + 1):
        # nCr = n!/((n-r)!*r!)
        print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")

    # for new line
    print()


# 2. Simplified nCr

n = int(input('Number of Rows: '))
for i in range(n + 1):
    for j in range(n - i):
        print(' ', end='')

    C = 1
    for j in range(1, i + 1):
        print(C, ' ', sep='', end='')
        C = C * (i - j) // j
    print()


# 3. Disecting the pattern with no factorials

n = int(input('Number of Rows: '))
final = []
for row in range(n):
    temp = []
    for col in range(row + 1):  # when  i = 3, we want 4 j values >> 1 3 3 1
        if col == 0 or col == row:  # col==row is the last column
            temp.append(1)
        else:  # adding the values above the current value
            temp.append(final[row - 1][col - 1] + final[row - 1][col])
    final.append(temp)

for row in range(n):
    for col in range(n - row - 1):
        print(format(' ', '<2'), end='')
    for col in range(row + 1):
        print(format(final[row][col], '<4'), end='')  # adds a spce after very number

    print()