import sys
from copy import deepcopy

class Monkey:
    def __init__(self, items, update, reduce, test):
        self.items = items
        self.update = update
        self.reduce = reduce
        self.test = test
        self.inspections = 0

def do_round(monkeys):
    for monkey in monkeys:
        for item in monkey.items:
            monkey.inspections += 1
            item = monkey.reduce(monkey.update(item))

            modulus, to_true, to_false = monkey.test
            if item % modulus == 0:
                monkeys[to_true].items.append(item)
            else:
                monkeys[to_false].items.append(item)

        monkey.items = []

def get_inspections(monkeys):
    inspections = [monkey.inspections for monkey in monkeys]
    inspections.sort()
    return inspections[-1] * inspections[-2]

def main():
    with open(sys.argv[1]) as f:
        # add a line to make format uniform
        notes = [[]] + [line.strip().split() for line in f.readlines()]
        notes_iter = iter(notes)

        monkeys = []
        meta_modulus = 1
        while next(notes_iter, None) != None:
            next(notes_iter)
            items = [int(item.strip(',')) for item in next(notes_iter)[2:]]
            update = lambda old, operation=' '.join(next(notes_iter)[3:]): eval(operation)
            reduce = lambda x: x // 3
            modulus = int(next(notes_iter)[-1])
            meta_modulus *= modulus
            to_true = int(next(notes_iter)[-1])
            to_false = int(next(notes_iter)[-1])

            monkeys.append(Monkey(items, update, reduce, (modulus, to_true, to_false)))
        
        monkeys_copy = deepcopy(monkeys)
        for _ in range(20):
            do_round(monkeys_copy)
        print(get_inspections(monkeys_copy))

        for monkey in monkeys:
            monkey.reduce = lambda x: x % meta_modulus
        for _ in range(10000):
            do_round(monkeys)
        print(get_inspections(monkeys))
    
if __name__ == '__main__':
    main()