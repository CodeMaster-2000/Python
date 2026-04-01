import random

def point_generator(n):
    q1 =0
    q2 = 0
    for k in range(n):
        print(q1,",", q2)
        i = random.randint(1, 4)
        if (i == 1):
          q1 = q1/4 + (3 * -1)/4
          q2 = q2/4
        elif (i == 2):
            q1 = q1/4 
            q2 = q2/4 + (3 * 1)/4
        elif (i == 3):
            q1 = q1/4 + (3 * 1)/4
            q2 = q2/4
        else:
            q1 = q1/4
            q2 = q2/4 + (3 * -1)/4


point_generator(10000)
