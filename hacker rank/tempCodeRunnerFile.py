def is_sum_of_cubes(x):
    # Start with a = 1
    a = 1
    # Iterate through possible values of a
    while True:
        # Calculate b^3
        b_cube = x - a**3
        # If b^3 is non-negative and a valid cube, return True
        if b_cube >= 0 and int(b_cube ** (1/3)) ** 3 == b_cube:
            return True
        # If a^3 exceeds x, there's no need to continue
        if a**3 > x:
            return False
        # Increment a
        a += 1

# Input number of test cases
t = int(input())

# Iterate through test cases
for _ in range(t):
    # Input value of x
    x = int(input())
    # Check if x can be represented as the sum of cubes of two positive integers
    if is_sum_of_cubes(x):
        print("YES")
    else:
        print("NO")
