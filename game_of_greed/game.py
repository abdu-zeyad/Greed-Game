import random
from collections import Counter
from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker
# from game_logic import GameLogic
# from banker import Banker
# class CheatingScoundrelError(ValueError):
#     pass


class Game(GameLogic, Banker):

    def __init__(self):
        self.shelved = 0
        self.balance = 0

    def play(self, roll_dice=None):
        roll_dice = roll_dice or Game.roll_dice
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        decision = input("> ")

        if decision == "y":
            var1 = True
            round_num = 1
            dice_num = 6
            while var1:
                print(f"Starting round {round_num}")
                print(f"Rolling {dice_num} dice...")
                dice = roll_dice(dice_num)
                sentence = "*** "
                for x in dice:
                    sentence = sentence + str(x) + " "
                sentence = sentence + "***"
                print(sentence)
                print("Enter dice to keep, or (q)uit:")
                dice_to_keep = input("> ")

                if dice_to_keep == "q":
                    var1 = False
                    print(
                        f"Thanks for playing. You earned {self.balance} points")
                else:
                    new_list = []
                    for x in dice_to_keep:
                        new_list.append(int(x))
                    tuple_list = tuple(new_list)
                    shelf_score = self.calculate_score(tuple_list)
                    self.shelf(shelf_score)
                    dice_num = dice_num - len(dice_to_keep)
                    print(
                        f"You have {self.shelved} un banked points and {dice_num} dice remaining")
                    print("(r)oll again, (b)ank your points or (q)uit:")
                    decision2 = input("> ")
                    if decision2 == "r":
                        continue
                    elif decision2 == "b":
                        print(
                            f"You banked {self.shelved} points in round {round_num}")
                        self.bank()
                        round_num += 1
                        print(f"Total score is {self.balance} points")
                        dice_num = 6
                    elif decision2 == "q":
                        print(
                            f"Thanks for playing. You earned {self.balance} points")
                        var1 = False
        else:
            print("OK. Maybe another time")


if __name__ == "__main__":
    game = Game()
    game.play()
    # x =game.keeperFunction()

    # # y =game._do_round()
    # print(x)
    # # print(y)
