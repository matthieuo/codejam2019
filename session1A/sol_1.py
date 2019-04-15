from random import shuffle


class State:
    def __init__(self, rows_, cols_):
        self.rows = rows_
        self.cols = cols_
        self.visited = set()

    def mark_visited(self, r, c):
        self.visited.add((r, c))

    def un_visit(self, r, c):
        self.visited.remove((r, c))

    def get_possible_move(self, prev_r, prev_c):
        move_l = []
        for r in range(1, self.rows + 1):
            for c in range(1, self.cols + 1):
                if not prev_r and not prev_c:
                    move_l.append((r, c))
                    continue
                if (r, c) in self.visited:
                    continue
                if r == prev_r or c == prev_c:
                    continue
                if r - c == prev_r - prev_c or r + c == prev_r + prev_c:
                    continue
                if prev_r and prev_c:
                    move_l.append((r, c))

        return move_l

    def search(self, prev_r, prev_c):
        if len(self.visited) == self.rows*self.cols:
            return (True, [])

        p_l = self.get_possible_move(prev_r, prev_c)
        if not p_l:
            return (False, [])

        shuffle(p_l)
        for rp, cp in p_l:
            self.mark_visited(rp, cp)
            ret_b, l_ret = self.search(rp, cp)
            self.un_visit(rp, cp)

            if ret_b:
                return (True, [(rp, cp)] + l_ret)

        return (False, [])


nt = int(input())
test_cases = []

for t in range(nt):
    r, c = input().split(" ")
    test_cases.append((int(r), int(c)))

for idx, (r, c) in enumerate(test_cases):
    st = State(r, c)
    val, o_l = st.search(None, None)
    if val:
        print("Case #" + str(idx + 1) + ": POSSIBLE")
        for r, c in o_l:
            print(str(r) + " " + str(c))
    else:
        print("Case #" + str(idx + 1) + ": IMPOSSIBLE")
