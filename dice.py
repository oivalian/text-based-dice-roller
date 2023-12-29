import random as r

while True:
    try:
        die_count = int(input("How many dice will you roll? >>> "))
        for _ in range(die_count):
            dice = ("⚀", "⚁", "⚂", "⚃", "⚄", "⚅")
            print(r.choice(dice), end='')
        print('\n')
    except ValueError:
        print('')
