from random import randint


class Dices():

    def __init__(self) -> None:
        pass

    dice_value_1 = '''
     ________
    | .   .  |
    |   .    |
    | .   .  |
    ----------
    '''
    dice_value_2 = '''
     ________
    |        |
    | .   .  |
    |        |
    ----------
    '''
    dice_value_3 = '''
     ________
    | .      |
    |   .    |
    |    .   |
    ----------
    '''
    dice_value_4 = '''
     ________
    | .   .  |
    |        |
    | .   .  |
    ----------
    '''
    dice_value_5 = '''
     ________
    | .   .  |
    |   .    |
    | .   .  |
    ----------
    '''
    dice_value_6 = '''
     ________
    | .   .  |
    | .   .  |
    | .   .  |
    ----------
    '''

    dices = {1: dice_value_1, 2: dice_value_2,
             3: dice_value_3, 4: dice_value_4, 5: dice_value_5, 6: dice_value_6}


# def rollDice(self, xyz):
#     print(dices.dices[xyz])


# value = randint(1, 6)
# rollDice(value)
