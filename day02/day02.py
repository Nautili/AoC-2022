import sys

def score_hand(hand):
    return (hand[1] + 1) + (((hand[1] - hand[0] + 1) % 3) * 3)

def score_guide_hand(hand):
    return (((hand[0] + hand[1] - 1) % 3) + 1) + (hand[1] * 3)

def get_score(hands, f):
    return sum(f(hand) for hand in hands)

def main():
    with open(sys.argv[1]) as f:
        hands = [[int(ord(line[0]) - ord('A')), int(ord(line[2]) - ord('X'))] for line in f.readlines()]
        print(get_score(hands, score_hand))
        print(get_score(hands, score_guide_hand))

if __name__ == '__main__':
    main()