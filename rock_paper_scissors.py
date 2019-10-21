# rock paper scissors

import random
import matplotlib.pyplot as plot

# algorithmChoice can be 1 for the first algorithm described in the assignment
# or 2 to use the expected values algorithm
def rock_paper_scissors(algorithmChoice):

    p1 = [0.6, 0.2, 0.2]
    p2 = [0.6, 0.2, 0.2]
    p1Bar = [0.6, 0.2, 0.2]
    p2Bar = [0.6, 0.2, 0.2]
    a = 0.001
    reward = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]

    # Plot initial policies
    fg, ax = plot.subplots(2)
    ax[0].set_title("Player 1")
    ax[1].set_title("Player 2")
    ax[0].plot([p1[0]], [p1[1]], 'b.')
    ax[1].plot([p2[0]], [p2[1]], 'b.')

    for i in range(50000):
        action1 = random.random()
        action2 = random.random()

        if action1 < p1[0]:  # rock
            a1 = 0
        elif action1 < (1 - p1[2]):  # paper
            a1 = 1
        else:  # scissors
            a1 = 2

        if action2 < p2[0]:  # rock
            a2 = 0
        elif action2 < (1 - p2[2]):  # paper
            a2 = 1
        else:  # scissors
            a2 = 2

        r1 = reward[a1][a2]
        r2 = reward[a2][a1]

        if algorithmChoice == 1:
            p1[a1] = p1[a1] + a * r1 * (1 - p1[a1])
            p1[a1 - 1] = p1[a1 - 1] - a * r1 * (p1[a1 - 1])
            p1[a1 - 2] = p1[a1 - 2] - a * r1 * (p1[a1 - 2])

            p2[a2] = p2[a2] + a * r2 * (1 - p2[a2])
            p2[a2 - 1] = p2[a2 - 1] - a * r2 * (p2[a2 - 1])
            p2[a2 - 2] = p2[a2 - 2] - a * r2 * (p2[a2 - 2])

        else:
            # calculate expected value
            p1Bar[0] = p1Bar[0] + a * (p1[0] - p1Bar[0])
            p1Bar[1] = p1Bar[1] + a * (p1[1] - p1Bar[1])
            p1Bar[2] = p1Bar[2] + a * (p1[2] - p1Bar[2])

            p2Bar[0] = p2Bar[0] + a * (p2[0] - p2Bar[0])
            p2Bar[1] = p2Bar[1] + a * (p2[1] - p2Bar[1])
            p2Bar[2] = p2Bar[2] + a * (p2[2] - p2Bar[2])

            # calculate policy
            p1[a1] = p1[a1] + a * r1 * (1 - p1[a1]) + a * (p1Bar[a1] - p1[a1])
            p1[a1 - 1] = p1[a1 - 1] - a * r1 * (p1[a1 - 1]) + a * (p1Bar[a1 - 1] - p1[a1 - 1])
            p1[a1 - 2] = p1[a1 - 2] - a * r1 * (p1[a1 - 2]) + a * (p1Bar[a1 - 2] - p1[a1 - 2])

            p2[a2] = p2[a2] + a * r2 * (1 - p2[a2]) + a * (p2Bar[a2] - p2[a2])
            p2[a2 - 1] = p2[a2 - 1] - a * r2 * (p2[a2 - 1]) + a * (p2Bar[a2 - 1] - p2[a2 - 1])
            p2[a2 - 2] = p2[a2 - 2] - a * r2 * (p2[a2 - 2]) + a * (p2Bar[a2 - 2] - p2[a2 - 2])

        p1Sum = sum(p1)
        p2Sum = sum(p2)
        p1[0] = p1[0] / p1Sum
        p1[1] = p1[1] / p1Sum
        p1[2] = p1[2] / p1Sum

        p2[0] = p2[0] / p2Sum
        p2[1] = p2[1] / p2Sum
        p2[2] = p2[2] / p2Sum

        if i%100 == 0:
            ax[0].plot([p1[0]], [p1[1]], 'b.')
            ax[1].plot([p2[0]], [p2[1]], 'b.')

    print(p1)
    print(p2)
    print()
    plot.show()

rock_paper_scissors(1)