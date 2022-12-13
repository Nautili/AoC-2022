import sys
from collections import deque

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def get_path_len(map, start, end=None):
    to_visit = deque()
    to_visit.append((start, 0))
    visited = set(start)

    while to_visit:
        cur_node, path_len = to_visit.popleft()
        for dir in dirs:
            visited.add(cur_node)
            next_node = tuple(i + j for i, j in  zip(dir, cur_node))
            cur_row, cur_col = cur_node
            next_row, next_col = next_node

            # out of bounds check
            if next_row < 0 or next_row >= len(map) \
                or next_col < 0 or next_col >= len(map[next_row]):
                continue

            # reversing this check should give the same result
            if not next_node in visited and map[next_row][next_col] >= map[cur_row][cur_col] - 1:
                if (end and next_node == end) or \
                    (not end and map[next_node[0]][next_node[1]] == 0):
                    return path_len + 1
                to_visit.append((next_node, path_len + 1))
                visited.add(next_node)
    return -1

def main():
    with open(sys.argv[1]) as f:
        map = []
        for row, line in enumerate(f.readlines()):
            map_row = []
            for col, c in enumerate(line.strip()):
                if c == 'S':
                    start = (row, col)
                    c = 'a'
                elif c == 'E':
                    end = (row, col)
                    c = 'z'
                map_row.append(ord(c) - ord('a'))
            map.append(map_row)

        print(get_path_len(map, end, start))
        print(get_path_len(map, end)) 
    
if __name__ == '__main__':
    main()