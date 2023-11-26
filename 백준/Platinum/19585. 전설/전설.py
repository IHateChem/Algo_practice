import sys
input = sys.stdin.readline
class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}
class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current_node = self.head

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = string
C,N = map(int,input().split())    
colors = Trie()
nicks = set()

for _ in range(C):
    colors.insert(input().strip())

for _ in range(N):
    nicks.add(input().strip())

Q = int(input())

for _ in range(Q):
    team = input().strip()
    current_node = colors.head
    for i, t in enumerate(team):
        if current_node and current_node.children.get(t):
            current_node = current_node.children[t]
            if current_node.data:
                if team[i+1:] in nicks:
                    print("Yes")
                    break
        else:
            current_node = None
    else:
        print("No")