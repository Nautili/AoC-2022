import sys

def is_enclosed(pair):
    r1, r2 = pair
    return (r1[0] <= r2[0] and r1[1] >= r2[1]) or(r1[0] >= r2[0] and r1[1] <= r2[1])

def overlaps(pair):
    r1, r2 = pair
    return max(r1[0], r2[0]) <= min(r1[1], r2[1]) 

def main():
    with open(sys.argv[1]) as f:
        pairs = [[list(map(int, range.split('-'))) for range in line.strip().split(',')] for line in f.readlines()]
        print(sum(map(is_enclosed, pairs)))
        print(sum(map(overlaps, pairs)))

if __name__ == '__main__':
    main()