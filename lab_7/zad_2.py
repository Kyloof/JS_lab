from typing import Iterable

def forall(pred, iterable: Iterable) -> bool:
    for i in iterable:
        if not pred(i):
            return False

    return True

def exists(pred, iterable: Iterable) -> bool:
    for i in iterable:
        if pred(i):
            return True

    return False

def atleast(n ,pred, iterable: Iterable) -> bool:

    if n <= 0:
        return True

    for i in iterable:
        if pred(i):
            n -= 1

            if n == 0:
                return True


    return False

def atmost(n, pred, iterable: Iterable) -> bool:

    if n < 0:
        return False

    for i in iterable:
        if pred(i):
            n -= 1

            if n < 0:
                return False


    return True
