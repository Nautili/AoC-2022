import sys

def intersect_all(sacks):
    (val,) = set.intersection(*map(set, sacks))
    return val

def make_half_sacks(sack):
    size = len(sack) // 2
    return [sack[:size], sack[size:]]

def priority(c):
    p = 1
    if c.isupper():
        p += 26
    return ord(c.lower()) - ord('a') + p

def get_priorities(sacks):
    return sum(priority(intersect_all(make_half_sacks(sack))) for sack in sacks)

def get_badge_priorities(sacks):
    groups = [sacks[i:i+3] for i in range(0, len(sacks), 3)]
    return sum(priority(intersect_all(group)) for group in groups)

def main():
    with open(sys.argv[1]) as f:
        sacks = [l.strip() for l in f.readlines()]
        print(get_priorities(sacks))
        print(get_badge_priorities(sacks))

if __name__ == '__main__':
    main()