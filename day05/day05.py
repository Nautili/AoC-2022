import sys
import copy

def move_lifo_stacks(stacks, instructions):
    for count, from_stack, to_stack in instructions:
        for _ in range(count):
            stacks[to_stack].append(stacks[from_stack].pop())

def move_bunch_stacks(stacks, instructions):
    for count, from_stack, to_stack in instructions:
        stacks[to_stack].extend(stacks[from_stack][-count:])
        del stacks[from_stack][-count:]

def main():
    with open(sys.argv[1]) as f:
        lines = f.readlines()
        stacks = [[] for _ in range(len(lines[0]) // 4)]

        # parse stacks
        cur_index = 0
        while len(lines[cur_index]) > 1:
            cur_line = lines[cur_index]
            for i in range(len(stacks)):
                cur_char = cur_line[(i * 4) + 1]
                if cur_char != ' ':
                    stacks[i].append(cur_char)
            cur_index += 1
        stacks = [stack[-2::-1] for stack in stacks]

        # parse instructions
        instructions = []
        for line in lines[cur_index + 1:]:
            step = line.strip().split()
            # (count, from, to)
            instructions.append((int(step[1]), int(step[3]) - 1, int(step[5]) - 1))

        # execute instructions
        stack_copy1 = copy.deepcopy(stacks)
        move_lifo_stacks(stack_copy1, instructions)
        print(''.join([stack[-1] for stack in stack_copy1]))

        stack_copy2 = copy.deepcopy(stacks)
        move_bunch_stacks(stack_copy2, instructions)
        print(''.join([stack[-1] for stack in stack_copy2]))

if __name__ == '__main__':
    main()