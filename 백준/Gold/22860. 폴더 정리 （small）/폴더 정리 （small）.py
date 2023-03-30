import sys
class Folder:
    def __init__(self, parent):
        self.parent = parent
        self.files = {}
        self.child = []
    def add_files(self, file):
        if self.files.get(file):
            self.files[file] += 1
        else:
            self.files[file] = 1
    def get_file(self):
        return self.files
    def get_parent(self):
        return self.parent
    def add_child(self, p):
        self.child.append(p)
input = sys.stdin.readline
N, M = map(int, input().split())
folder = {}
for _ in range(N+M):
    P, F, C = input().strip().split()
    if not folder.get(P):
        folder[P] = Folder(P)
    if C == "1":
        if folder.get(F) and folder[F].parent != P:
            folder[F].parent = P
            folder[P].add_child(folder[F])
            continue
        folder[F] = Folder(F)
        folder[P].add_child(folder[F])
    else:
        folder[P].add_files(F)
Q = int(input())
for i in range(Q):
    sequence = input().strip().split("/")
    stack = [folder[sequence[-1]]]
    tot_file = {}
    while stack:
        P = stack.pop()
        for k, v in P.files.items():
            if tot_file.get(k):
                tot_file[k] +=v
            else:
                tot_file[k] = v
        for c in P.child:
            stack.append(c)
    answer = [0,0]
    for k, v in tot_file.items():
        answer[0] += 1
        answer[1] += v
    print(*answer)