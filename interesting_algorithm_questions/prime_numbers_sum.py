def find_all_prime_numbers(n):
    prime_numbers = []
    for i in range(2, n):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            prime_numbers.append(i)
    return prime_numbers


n = 200
prime_numbers_list = find_all_prime_numbers(n)
count = 0
for i in prime_numbers_list:
    if n - i in prime_numbers_list:
        count += 1
print count / 2
