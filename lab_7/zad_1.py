def acronyms(xs: list[str]):
    head, *tail = xs
    fst_letter, *_ = head
    return fst_letter + ("" if tail == [] else acronyms(tail))


print(acronyms(["Zakład", "Ubezpieczeń", "Społecznych"]))


def median(xs: list[int]):
    def get_median(xs, idx, length):
        head, *tail = xs
        snd_head, *snd_tail = tail
        return (
            (
                (head + snd_head) / 2
                if idx == (length - 1) // 2
                else get_median(tail, idx + 1, length)
            )
            if length % 2 == 0
            else (head if idx == length // 2 else get_median(tail, idx + 1, length))
        )

    length = len(xs)
    return get_median(sorted(xs), 0, length) if length > 1 else xs[0]


print(median([1, 2, 3, 4, 5, 6]))
print(median([321, 32, 1, 0, 4, 5, 6]))


def pierwiastek(x: float, epsilon: float):
    def newton(answ: float) -> float:
        return answ if abs(answ**2 - x) < epsilon else newton((answ + x / answ) / 2)

    return newton(x / 2 if x > 1 else 1.0)


print(pierwiastek(3, 0.1))

from functools import reduce


def make_alpha_dict(x: str):
    words = x.split()
    letters = sorted(set(filter(str.isalpha, x)))

    def add_to_dict(alpha_dict, char):
        alpha_dict[char] = list(filter(lambda word: char in word, words))
        return alpha_dict

    # reduce - apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along
    return reduce(add_to_dict, letters, {})


print(make_alpha_dict("on i ona"))


def flatten(x):
    if isinstance(x, (list, tuple)):
        # sum does the flattening
        return sum(map(flatten, x), [])
    else:
        return [x]


print(flatten([1, [2, 3], [[4, 5], 6]]))
