import sys
from collections import namedtuple

Pair = namedtuple("Pair", "x y")

def cmp(a, b):
    return int(a > b) - int(a < b)

class Cave:
    def __init__(self, paths, is_big_cave):
        x_list = [pair.x for path in paths for pair in path]
        y_list = [pair.y for path in paths for pair in path]

        # no offset to include source
        y_len = max(y_list) + 1
        x_len = max(x_list) - min(x_list) + 1

        self.x_offset = min(x_list)
        self.y_offset = 0

        # adjust lengths to include full triangle down sides
        if is_big_cave:
            x_len += 2 * (y_len + 2)
            self.x_offset -= (y_len + 2)

        self.cave = [['.' for _ in range(x_len)] for _ in range(y_len)]

        if is_big_cave:
            self.add_floor()

        for path in paths:
            cur_pair = self.get_pos(path[0])
            self.cave[cur_pair.y][cur_pair.x] = '#'

            for next_pair in path[1:]:
                next_pos = self.get_pos(next_pair)
                while cur_pair != next_pos:
                    cur_pair = Pair(cur_pair.x + cmp(next_pos.x, cur_pair.x),
                                    cur_pair.y + cmp(next_pos.y, cur_pair.y))
                    self.cave[cur_pair.y][cur_pair.x] = '#'

    def add_floor(self):
        self.cave.append(['.' for _ in range(len(self.cave[0]))])
        self.cave.append(['#' for _ in range(len(self.cave[0]))])

    def get_pos(self, pair):
        return Pair(pair.x - self.x_offset, pair.y - self.y_offset)

    def drop_sand(self):
        while True:
            cur_pos = self.get_pos(Pair(500, 0))
            if self.cave[cur_pos.y][cur_pos.x] == 'o':
                return

            while True:
                if cur_pos.y + 1 == len(self.cave):
                    return
                if self.cave[cur_pos.y + 1][cur_pos.x] == '.':
                    cur_pos = Pair(cur_pos.x, cur_pos.y + 1)
                    continue

                if cur_pos.x == 0:
                    return
                if self.cave[cur_pos.y + 1][cur_pos.x - 1] == '.':
                    cur_pos = Pair(cur_pos.x - 1, cur_pos.y + 1)
                    continue

                if cur_pos.x + 1 == len(self.cave[cur_pos.y]):
                    return
                if self.cave[cur_pos.y + 1][cur_pos.x + 1] == '.':
                    cur_pos = Pair(cur_pos.x + 1, cur_pos.y + 1)
                    continue
                    
                # fail-through to the sand just stopping there
                self.cave[cur_pos.y][cur_pos.x] = 'o'
                break

    def print(self):
        for row in self.cave:
            print(''.join(row))

def main():
    with open(sys.argv[1]) as f:
        paths = [[Pair(*map(int, pair.split(','))) for pair in line.strip().split(" -> ")] for line in f.readlines()]

        cave = Cave(paths, is_big_cave=False)
        cave.drop_sand()
        # cave.print()
        print(len([cell for row in cave.cave for cell in row if cell == 'o']))

        big_cave = Cave(paths, is_big_cave=True)
        big_cave.drop_sand()
        # big_cave.print()
        print(len([cell for row in big_cave.cave for cell in row if cell == 'o']))
    
if __name__ == '__main__':
    main()