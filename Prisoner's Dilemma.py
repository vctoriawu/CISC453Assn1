
# Prisoner's Dilemma

import random
def dilemma():
    # initialization
    # first is not selling out, second is selling out
    p1 = [0.5, 0.5]
    p2 = [0.5, 0.5]

    # evaluation
    a = 0.001
    reward1 = [[5,0], # stays loyal
          [10,1]] # sells out

    reward2 = [[5,10],
          [0,1]]

    # not sure about updating? doesn't seem right for updating policy
    for i in range(50000):
        action1 = random.random()
        if action1 < p1[0]:
            a1 = 0 # cooperate
        else:
            a1 = 1
        action2 = random.random()
        if action2 < p2[0]:
            a2 = 0
        else:
            a2 = 1
        r1 = reward1[a1][a2]
        r2 = reward2[a1][a2]
        
        p1[a1] = p1[a1] + a*r1*(1-p1[a1])
        # because of the way indexing works, I can do this
        p1[a1-1] = p1[a1-1] - a*r1*p1[a1-1]

        
        p2[a2] = p2[a2] + a*r2*(1-p2[a2])    
        p2[a2-1] = p2[a2-1] - a*r2*p2[a2-1]
        # must normalize to make sure add to one
        
    p1Sum = p1[0] + p1[1]
    p2Sum = p2[0] + p2[1]
    p1[0] = p1[0]/p1Sum
    p1[1] = p1[1]/p1Sum
    p2[0] = p2[0]/p2Sum
    p2[1] = p2[1]/p2Sum
    print(p1)
    print(p2)

for i in range(1):
    dilemma()
