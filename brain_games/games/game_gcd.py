import random


def find_gcd(first_number, second_number):
    while first_number != second_number:
        if first_number > second_number:
            first_number = first_number - second_number
        else:
            second_number = second_number - first_number
    return first_number


def game_gcd():
    print('Find the greatest common divisor of given numbers.')

    random_cap = 10
    base_divisor = random.randint(1, random_cap)
    first_number = base_divisor * random.randint(1, random_cap)
    second_number = base_divisor * random.randint(1, random_cap)
    expression = '{0} {1}'.format(first_number, second_number)

    gcd = find_gcd(first_number, second_number)
    correct_answer = str(gcd)

    return expression, correct_answer
