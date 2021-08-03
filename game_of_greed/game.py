import random
from collections import Counter


class CheatingScoundrelError(ValueError):
    pass


class Game:

    def __init__(self, print_func=print, input_func=input):
        self._print = print_func
        self._input = input_func
        self.score = 0
        self.num_rounds = 10


    def play(self, num_rounds=10):

        self.num_rounds = num_rounds

        self._print("""Welcome to Game of Greed
        (y)es to play or (n)o to decline""")

        response = self._input('>')

        if response == 'y':
            self._start()
        elif response == 'n':
            self._print('OK. Maybe later')

    def _start(self):

        self.score = 0

        round_num = 1

        for i in range(1, self.num_rounds + 1):
            self._print(f'Starting round {round_num}')

            round_score = self._do_round()

            self._print(f'You banked {round_score} points in round {round_num}')

            self.score += round_score

            round_num += 1

            self._print(f'You have {self.score} points total')


        self._print('Thanks for playing!')

    def _do_round(self):
        num_dice = 6

        score = 0
        while(True):
            self._print(f'Rolling {num_dice} dice..')

            roll = self.roll_dice(num_dice)

            score = self.calculate_score(roll)

            self._print(f'***{roll}***')

            keepers = self.validate_roll(roll)

            # TODO: handle non scoring but mysteriously used dice
            num_dice -= len(keepers)

            score += self.calculate_score(keepers)

            self._print(f'You have {score} unbanked points and {num_dice} dice remaining')

            if num_dice == 0:
                num_dice = 6
            self._print('(r)oll again, (b)ank your points or (q)uit:')
            
            roll_again_response = self._input('>')

            if  roll_again_response == 'r':
                continue

            if roll_again_response =='q':
                print('Thanks for playing. You earned 500 points')
                break


        return score

    def validate_roll(self, roll):

        while True:

            keep_response = self._input('Enter dice to keep, or (q)uit:')

            keepers = tuple(int(char) for char in keep_response)

            if self.validate(roll, keepers):
                return keepers
            else:
                self._print('No way pal')
                self._print(roll)

    def validate(self, roll, keepers):

        roll_counter = Counter(roll)
        keepers_counter = Counter(keepers)
        return len(keepers_counter - roll_counter) == 0

    def calculate_score(self,m ):
        score = 0
        pairs_double =0 
        pairs_trible=0
        num = Counter(m)
        
        """ myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
          Counter({2: '4', 3: '4', 1: '3', 4: '2', 5: '1'})
    
            >>> print Counter(myList).keys()
            i=[1, 2, 3, 4, 5]
            >>> 
            >>> print Counter(myList).values()
            num[i]=[3, 4, 4, 2, 1]
        """

        if len(num) == 6 :
            
            score+=1500
            return score
        
    

        for i in num:

            if num[i] == 2:
                pairs_double += 1
                if pairs_double == 3:
                    score+=1500

            if num[i] == 3  :
                pairs_trible+=1
                if pairs_trible==3:
                    score+=1200
                
            if i == 5 and num[i] < 3:
                score = score + (num[i]*50)


            if i == 1 and num[i] < 3:
                score = score + (num[i]*100)
             
            if num[i] >= 3 and i == 1:
                score = score + 1000*(num[i]-2)

            if num[i] >= 3   and i != 1:
                score = score + ((i)*100*(num[i]-2))

        print(num)
        return score

    def roll_dice(self,x):
        dice=[]
        for i in range(x):
            dice.append(random.randint(1,6))
            roll = tuple(dice)
        return roll


if __name__ == "__main__":
    game = Game()
    game.play()
    # x =game._start()
    
    # y =game._do_round()

    # print(x)
    # print(y)
