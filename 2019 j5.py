''' Input
    AA AB
    AB BB
    B AA
    4 AB AAAB

    Output
    2 1 BB
    3 1 AAB
    3 3 AAAA
    1 3 AAAB

    Alternative Output:
    2 1 BB
    3 2 BAA
    1 2 BAB
    3 1 AAAB

    input details
    - first 3 lines are sub. rules
    - 4th line: s - # of steps, 
    i - initial sequence, f - finished sequence
    output details
    - r - sub rule #
    - p - position of starting index
    - w - sequence that results'''

rulekey = []
rulevalue = []

for i in range(3):
    rules = input().split()
    rulekey.append(rules[0])
    rulevalue.append(rules[1])

s, i, f = input().split()

# rulekey = ['AA', 'AB', 'B']
# rulevalue = ['AB', 'BB', 'AA']

# AA - AB - BB - AAB - AAAA

# s, i, f = ['4', 'AA', 'AAAA']

class Variation():
    def __init__(self, dstr, location = None, rule = None, parent=None):
        self.rule = rule
        self.location = location
        self.dstr = dstr
        self.step = 0
        self.record=[(rule, location, dstr)]
        if parent:
            self.step = parent.step + 1
            self.record=parent.record+self.record


Stack = [Variation(i)]
visited=[]


def replace(rulenumber, string):
    output = []
    previous = -1
    for i in range(len(string)):
        a = string.find(rulekey[rulenumber], i)
        if a != -1 and a != previous:
            previous = a
            output.append([string[:i] + string[i:].replace(rulekey[rulenumber], rulevalue[rulenumber], 1), a, rulenumber])
    return output


while Stack:
    P = Stack.pop()
    if P.dstr in visited:
        continue
    if P.step == int(s):
        if P.dstr == str(f):
            for i in P.record[1:]:
                print(f'{i[0]+1} {i[1]+1} {i[2]}')
            break
        continue
    visited.append(P.dstr)
    for i in range(3):
        a = replace(i, str(P.dstr))
        for j in a:
            Stack.append(Variation(j[0], j[1], j[2], P))


# print(P.step, 'p.step')
# print(P.record, 'p.record')
# print(visited, 'visited')

