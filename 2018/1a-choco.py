class Board:
    def __init__(self, board_l, r, c, h, v):
        self.board_l = board_l
        self.r = r
        self.c = c
        self.h = h
        self.v = v

    def cut_one(self, ph, pv):
        # compute the number of chocolates for the four quarters
        fq = 0
        for l in self.board_l[0:pv]:
            fq += l[0:ph].count('@')

        sq = 0
        for l in self.board_l[0:pv]:
            sq += l[ph:].count('@')

        tq = 0
        for l in self.board_l[pv:]:
            tq += l[ph:].count('@')

        qq = 0
        for l in self.board_l[pv:]:
            qq += l[0:ph].count('@')

        return fq, sq, tq, qq

    def check_possible(self):
        for ph in range(1, self.r):
            for pv in range(1, self.c):
                fq, sq, tq, qq = self.cut_one(pv, ph)
                if fq == sq and sq == tq and tq == qq:
                    return True

        return False


def main():
    tt = int(input())
    l_cases = []
    for _ in range(tt):
        board_l = []
        r, c, h, v = (int(x) for x in input().split(' '))
        for _ in range(r):
            board_l.append(list(input()))

        board = Board(board_l, r, c, h, v)
        l_cases.append(board)

    for idx, b in enumerate(l_cases):
        if b.check_possible():
            print("Case #" + str(idx+1)+": POSSIBLE")
        else:
            print("Case #" + str(idx+1)+": IMPOSSIBLE")


main()
