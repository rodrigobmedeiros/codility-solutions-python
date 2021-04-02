# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # write your code in Python 3.6
    total_distance = Y - X

    rounded_number_of_jumps = total_distance // D
    division_rest = total_distance % D

    return rounded_number_of_jumps if division_rest == 0 else rounded_number_of_jumps + 1