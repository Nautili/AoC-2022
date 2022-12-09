import sys

def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0

def count_tail_steps(steps, knots):
    cur_pos = [(0, 0) for _ in range(knots)]
    tail_positions = {cur_pos[0]}

    for (dir, count) in steps:
        for _ in range(count):
            # move head
            cur_pos[0] = (cur_pos[0][0] + dir[0], cur_pos[0][1] + dir[1])

            # move tail
            for k, next_knot in enumerate(cur_pos[1:], start=1):   
                last_pos = cur_pos[k - 1]
                x_delta = last_pos[0] - next_knot[0]
                y_delta = last_pos[1] - next_knot[1]        
                if abs(x_delta) > 1 or abs(y_delta) > 1:
                    cur_pos[k] = (next_knot[0] + sign(x_delta), next_knot[1] + sign(y_delta))
            tail_positions.add(cur_pos[-1])
    
    return len(tail_positions)
            

def main():
    dir_map = {
        'U': (0, -1),
        'R': (1, 0),
        'D': (0, 1),
        'L': (-1, 0)}

    with open(sys.argv[1]) as f:
        steps = []
        for line in f.readlines():
            dir, count = line.strip().split()
            steps.append((dir_map[dir], int(count)))

        print(count_tail_steps(steps, 2))
        print(count_tail_steps(steps, 10))

if __name__ == '__main__':
    main()