import sys

def max_elf_sum(l):
    return max([sum(block) for block in l])

def top_elves_sum(l):
    sums = [sum(block) for block in l]
    sums.sort()
    return sum(sums[-3:])

def main():
    with open(sys.argv[1]) as f:
        blocks = f.read().split('\n\n')
        block_list = [[int(val) for val in block.split('\n')] for block in blocks]
        print(max_elf_sum(block_list))

        print(top_elves_sum(block_list))

if __name__ == '__main__':
    main()