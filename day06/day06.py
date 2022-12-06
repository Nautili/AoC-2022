import sys

def get_start(line, chars):
    for i in range(len(line) - chars):
        if len(set(line[i:i+chars])) == chars:
            return i + chars

def main():
    with open(sys.argv[1]) as f:
        line = f.readline().strip()

        print(get_start(line, 4))
        print(get_start(line, 14))

if __name__ == '__main__':
    main()