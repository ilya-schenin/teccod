def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def get_prime_nums(start: int, end: int) -> list[int]:
    if start > end:
        start, end = end, start

    return [num for num in range(start, end + 1) if is_prime(num)]


print(get_prime_nums(1, 20))
