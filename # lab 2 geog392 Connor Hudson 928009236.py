# lab 2 geog392 Connor Hudson 928009236
import math

if __name__ == "__main__":

    # Q1
    lst1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    result1 = 1

    # Multiply all list items together
    for num in lst1:
        result1 *= num

    print(f"Results of Q1:")
    print(f"result1 = {result1}")

    # Q2
    lst2 = [-1, 23, 483, 8573, -1384, -381569, 1652337, 718522177]
    result2 = 0

    # Add all list items together
    for num in lst2:
        result2 += num

    print(f"Results of Q2:")
    print(f"result2 = {result2}")

    # Q3
    lst3 = [146, 875, 911, 83, 81, 439, 44, 5, 46, 76, 61, 68, 1, 14, 38, 26, 21]
    result3 = 0

    # Add only even numbers
    for num in lst3:
        if num % 2 == 0:
            result3 += num

    print(f"Results of Q3:")
    print(f"result3 = {result3}")