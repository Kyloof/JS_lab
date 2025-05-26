from functools import cache


def make_generator(f):

    mem = cache(f)

    def generator():
        x = 1
        while True:
            yield mem(x % 5)
            x += 1

    return generator


# doesnt need to calculate the same call twice !
# for reccursive functions it need to be applied directly to the og function
# because cache works based on the args provided so if we cache recursively only here it will work


@cache
def fibonacci(n):
    print(f"licze dla {n}")
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(37))


print("-------------------------")


def seq(x):
    print(f"licze dla {x}")
    return 2 * x + 2


x = make_generator(seq)
gen = x()

for i in range(10):
    print(next(gen))
