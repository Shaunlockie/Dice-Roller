import random
def d20_roll():
    d20 = random.randint(1,20)
    if d20 == 20:
        print("Critical Hit!")
    if d20 == 1:
        print("Critical Fail!")
    return d20



print(d20_roll())
