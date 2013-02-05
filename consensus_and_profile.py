lines = [line.strip() for line in open('extra/consensus_and_profile_dataset.txt')]
ccA = 0
ccC = 0
ccG = 0
ccT = 0
a = []
c = []
g = []
t = []
consensus = ''
letters = ['A' , 'C' , 'G' , 'T']
for i in range(0,len(lines[0])):
    for j in range(0,len(lines)):
        l = lines[j][i]
        if l == "A":
            ccA += 1
        elif l == "C":
            ccC += 1
        elif l == "G":
            ccG += 1
        elif l == "T":
            ccT += 1
    a.append(ccA)
    c.append(ccC)
    g.append(ccG)
    t.append(ccT)
    cons = [ccA,ccC,ccG,ccT]
    consensus += letters[cons.index(max(cons))]
    ccA = ccC = ccG = ccT = 0
print consensus
print 'A:' , " ".join(map(str,a))
print 'C:' , " ".join(map(str,c))
print 'G:' , " ".join(map(str,g))
print 'T:' , " ".join(map(str,t))