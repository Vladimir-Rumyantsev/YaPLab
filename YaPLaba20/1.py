def next_moving_average(numbers):
    acc = 0
    result = 0

    while True:
        result += numbers[acc]
        acc += 1
        yield result / acc


nums = list(map(int, input('\nВведите через пробел последовательность чисел: ').split()))
count = 1
print('\nРезультат:', end=' ')
for num in next_moving_average(nums):
    print(num, end=' ')
    count += 1
    if count > len(nums):
        print()
        break
