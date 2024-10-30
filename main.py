'''
Write a function `print_multiples` with one parameters `n`.

When called, your function should print out ALL of the multiples of `n` between 0 and 100 (including both 0 and 100), and NO OTHER numbers.

Call your function for `n = 2`, `n = 3`, `n = 5`, and `n = 12`.
'''

def print_multiples(n):
    for i in range(101):
        if i%n == 0:
            print(i)

print_multiples(2)
# Tested it and the code works for when n = 2, 3, 5, and 12