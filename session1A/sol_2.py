import sys


def main():
    t, n, max_go = (int(x) for x in input().split(" "))

    for _ in range(t):
        max_val = 0
        for _ in range(n):
            in_list = [18 for _ in range(18)]
            print(" ".join([str(x) for x in in_list]),
                  flush=True)
            output_l = [int(x) for x in input().split(" ")]
            max_val = min(max(sum(output_l), max_val), max_go)

        print(max_val)
        a = int(input())
        if a == -1:
            sys.exit()


if __name__ == "__main__":
    main()
