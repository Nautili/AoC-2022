import sys

def get_visible(forest):
    visibility = [[0 for _ in row] for row in forest]
    size = len(forest)

    for i in range(size):
        down_max = -1
        up_max = -1
        left_max = -1
        right_max = -1
        for j in range(size):
            if forest[i][j] > right_max:
                visibility[i][j] = 1
                right_max = forest[i][j]
            if forest[j][i] > down_max:
                visibility[j][i] = 1
                down_max = forest[j][i]
            if forest[i][size - j - 1] > left_max:
                visibility[i][size - j - 1] = 1
                left_max = forest[i][size - j - 1]
            if forest[size - j - 1][i] > up_max:
                visibility[size - j - 1][i] = 1
                up_max = forest[size - j - 1][i]

    return sum(sum(row) for row in visibility)

def get_scenic_score(forest, row, col):
    size = len(forest)
    height = forest[row][col]
    left = col - 1
    while left > 0 and forest[row][left] < height:
        left -= 1
    left = max(left, 0)

    right = col + 1
    while right < size and forest[row][right] < height:
        right += 1
    right = min(right, size - 1)

    up = row - 1
    while up > 0 and forest[up][col] < height:
        up -= 1
    up = max(up, 0)

    down = row + 1
    while down < size and forest[down][col] < height:
        down += 1
    down = min(down, size - 1)

    return (col - left) * (right - col) * (up - row) * (row - down)

def get_internal_visible(forest):
    max_score = 0
    for row in range(len(forest)):
        for col in range(len(forest)):
            max_score = max(max_score, get_scenic_score(forest, row, col))
    return max_score

def main():
    with open(sys.argv[1]) as f:
        forest = [[int(c) for c in line.strip()] for line in f.readlines()]

        print(get_visible(forest))
        print(get_internal_visible(forest))

if __name__ == '__main__':
    main()