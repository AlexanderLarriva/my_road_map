def is_perfect(num):
    sum_div = 0
    # if num == 0:
    #     return False
    for i in range(1, num):
        if num%i == 0:
            sum_div += i
    if sum_div == num:
        return True
    return False

print(is_perfect(6))


def is_perfect2(number):
    if number < 6:
        return False

    limit = number // 2 + 1
    sum = 0
    for divisor in range(1, limit):
        if number % divisor == 0:
            sum += divisor

    return sum == number

print(is_perfect2(6))