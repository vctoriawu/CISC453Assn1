
# Prisoner's Dilemma
import time
import random
def dilemma(choice):
    # initialization
    # first is not selling out, second is selling out
    p1 = [0.5, 0.5]
    p2 = [0.5, 0.5]
    p1Bar = [0.5, 0.5]
    p2Bar = [0.5, 0.5]
    # evaluation
    a = 0.001
    reward = [[5,0], # stays loyal
          [10,1]] # sells out

    # not sure about updating? doesn't seem right for updating policy
    for i in range(5000):
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
            
        r1 = reward[a1][a2]
        r2 = reward[a2][a1]

        if choice == 1:
            p1[a1] = p1[a1] + a*r1*(1-p1[a1])
            # because of the way indexing works, I can do this
            p1[a1-1] = p1[a1-1] - a*r1*p1[a1-1]

            
            p2[a2] = p2[a2] + a*r2*(1-p2[a2])    
            p2[a2-1] = p2[a2-1] - a*r2*p2[a2-1]

        else:
            # expected values
            p1Bar[0] = p1Bar[0] + a*(p1[0] - p1Bar[0])
            p1Bar[1] = p1Bar[1] + a*(p1[1] - p1Bar[1])

            p2Bar[0] = p2Bar[0] + a*(p2[0] - p2Bar[0])
            p2Bar[1] = p2Bar[1] + a*(p2[1] - p2Bar[1])

            # policy update
            if i%10 == 0:
                temp = a*(p1Bar[a1] - p1[a1])
                print(temp)
            p1[a1] = p1[a1] + a*r1*(1-p1[a1]) + a*(p1Bar[a1] - p1[a1])
            p1[a1-1] = p1[a1-1] - a*r1*p1[a1-1] + a*(p1Bar[a1-1] - p1[a1-1])
            
            p2[a2] = p2[a2] + a*r2*(1-p2[a2]) + a*(p2Bar[a2] - p2[a2])
            p2[a2-1] = p2[a2-1] - a*r2*(p2[a2-1]) + a*(p2Bar[a2-1] - p2[a2-1])
    # must normalize to make sure add to one
        
        p1Sum = p1[0] + p1[1]
        p2Sum = p2[0] + p2[1]
        p1[0] = p1[0]/p1Sum
        p1[1] = p1[1]/p1Sum
        p2[0] = p2[0]/p2Sum
        p2[1] = p2[1]/p2Sum
    print(p1)
    print(p2)

def main():
    # send in 1 = regular, converges, anything else = expected value
    for i in range(10):
        dilemma(2)
    
main()
