import sys

def draw(screen, reg_x, cycle):
    if abs(reg_x - (cycle % 40)) < 2:
        screen.append("█")
    else:
        screen.append(".")

def run(program):
    cycle = 0
    reg_x = 1

    screen = []
    signal_record = []

    for line in program:
        draw(screen, reg_x, cycle)
        cycle += 1
        signal_record.append(reg_x * cycle)

        if line[0] == "noop":
            pass
        if line[0] == "addx":
            draw(screen, reg_x, cycle)
            cycle += 1
            signal_record.append(reg_x * cycle)
            reg_x += int(line[1])

    return signal_record, screen

def main():
    with open(sys.argv[1]) as f:
        program = [line.strip().split() for line in f.readlines()]
    
    signals, screen = run(program)
    print(sum(signals[19::40]))
    for line in [screen[i:i+40] for i in range(0, len(screen), 40)]:
        print(''.join(line))

if __name__ == '__main__':
    main()