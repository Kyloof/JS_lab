def make_generator(f):
    def generator():
        x = 1
        while True:
            yield f(x)
            x+=1
    return generator

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    res = [1,1]
    for i in range(2, n):
        res.append(res[i - 1] + res[i - 2])
    return res[i]


x = make_generator(fibonacci)
gen = x()

for i in range(10):
    print(next(gen))


print("-------------------------")

y = make_generator(lambda x: 2*x + 2)
gen2 = y()

for i in range(10):
    print(next(gen2))

print("-------------------------")

z = make_generator(lambda x: x**3 + 2)
gen3 = z()

for i in range(10):
    print(next(gen3))
