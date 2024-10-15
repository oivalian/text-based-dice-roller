from random import choice

while True:
    try:
        dice = ("⚀", "⚁", "⚂", "⚃", "⚄", "⚅")
        die_count = int(input("\nHow many dice will you roll? >>> "))
        [print(choice(dice), end='') for _ in range(die_count)]
    except ValueError:
        print('')
