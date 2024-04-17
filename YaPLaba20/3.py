def leonardo():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b + 1


line = '\n'
fib_gen = leonardo()

for i in range(20):
    line = f'{line}{next(fib_gen)}, '

if line != '\n':
    print(f'{line[:-2]}')
