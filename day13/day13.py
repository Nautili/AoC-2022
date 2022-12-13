import sys
from functools import cmp_to_key

def get_order(l, r):
    if type(l) is list and type(r) is list:
        for check in map(get_order, l, r):
            if check: return check
        return get_order(len(l), len(r))
    elif type(l) is int and type(r) is int:
        if l < r: return -1
        elif l > r: return 1
        else: return 0
    else:
        if type(l) is int:
            return get_order([l], r)
        else:
            return get_order(l, [r])

def main():
    with open(sys.argv[1]) as f:
        pairs = [list(map(eval, pair.split())) for pair in f.read().split('\n\n')]

        orders = [get_order(l, r) for l, r in pairs]
        print(sum(i + 1 for i in range(len(orders)) if orders[i] is -1))
    
        pairs = [element for pair in pairs for element in pair] + [[[2]]] + [[[6]]]
        pairs.sort(key=cmp_to_key(get_order))
        print((pairs.index([[2]]) + 1) * (pairs.index([[6]]) + 1))

if __name__ == '__main__':
    main()