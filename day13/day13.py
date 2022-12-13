import sys
from enum import Enum
from functools import cmp_to_key

class Order(Enum):
    RIGHT = 1
    WRONG = 2
    SAME = 3

def get_order(l, r):
    if type(l) is list and type(r) is list:
        for l_val, r_val in zip(l, r):
            check = get_order(l_val, r_val)
            if check is not Order.SAME:
                return check
        if len(l) > len(r):
            return Order.WRONG
        elif len(l) < len(r):
            return Order.RIGHT
        return Order.SAME
    elif type(l) is int and type(r) is int:
        if l < r:
            return Order.RIGHT
        elif l > r:
            return Order.WRONG
        else:
            return Order.SAME
    else:
        if type(l) is int:
            return get_order([l], r)
        else:
            return get_order(l, [r])

def order_cmp(l, r):
    order = get_order(l, r)
    if order is Order.RIGHT:
        return -1
    elif order is Order.WRONG:
        return 1
    return 0

def main():
    with open(sys.argv[1]) as f:
        pairs = [list(map(eval, pair.split())) for pair in f.read().split('\n\n')]

        orders = [get_order(l, r) for l, r in pairs]
        print(sum(i + 1 for i in range(len(orders)) if orders[i] is Order.RIGHT))
    
        pairs = [element for pair in pairs for element in pair] + [[[2]]] + [[[6]]]
        pairs.sort(key=cmp_to_key(order_cmp))
        print((pairs.index([[2]]) + 1) * (pairs.index([[6]]) + 1))

if __name__ == '__main__':
    main()