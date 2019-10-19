import random
def MatchingPennies(choice):
    p1 = [0.2, 0.8]
    p2 = [0.2, 0.8]
    p1Bar = [0.2, 0.8]
    p2Bar = [0.2, 0.8]
    a = 0.001
    R1 = [[1, -1], # [p1 and p2 heads, p1 head and p2 tails]
          [-1, 1]] # [p1 tails and p2 heads, p1 and p2 tails]

    R2 = [[-1, 1],
          [1, -1]]

    for i in range(50000):
        action1 = random.random()
        if action1 < p1[0]:
            a1 = 0 # heads
        else:
            a1 = 1
        action2 = random.random()
        if action2 < p2[0]:
            a2 = 0
        else:
            a2 = 1
        r1 = R1[a1][a2]
        r2 = R2[a1][a2]

        if choice == 1:
            p1[a1] = p1[a1] + a * r1 * (1 - p1[a1])
            p1[a1 - 1] = p1[a1 - 1] - a * r1 * p1[a1 - 1]

            p2[a2] = p2[a2] + a * r2 * (1 - p2[a2])    
            p2[a2 - 1] = p2[a2 - 1] - a * r2 * p2[a2 - 1]

        else:
            p1Bar[0] = p1Bar[0] + a * (p1[0] - p1Bar[0])
            p1Bar[1] = p1Bar[1] + a * (p1[1] - p1Bar[1])

            p2Bar[0] = p2Bar[0] + a * (p2[0] - p2Bar[0])
            p2Bar[1] = p2Bar[1] + a * (p2[1] - p2Bar[1])

            p1[a1] = p1[a1] + a * r1 * (1 - p1[a1]) + a * (p1Bar[a1] - p1[a1])
            p1[a1 - 1] = p1[a1 - 1] - a * r1 * p1[a1 - 1] + a * (p1Bar[a1 - 1] - p1[a1 - 1])
            
            p2[a2] = p2[a2] + a * r2 * (1 - p2[a2]) + a * (p2Bar[a2] - p2[a2])
            p2[a2 - 1] = p2[a2 - 1] - a * r2 * (p2[a2 - 1]) + a * (p2Bar[a2 - 1] - p2[a2 - 1])

        p1Sum = p1[0] + p1[1]
        p2Sum = p2[0] + p2[1]
        p1[0] = p1[0] / p1Sum
        p1[1] = p1[1] / p1Sum
        p2[0] = p2[0] / p2Sum
        p2[1] = p2[1] / p2Sum
    print(p1)
    print(p2)
            
MatchingPennies(2)
