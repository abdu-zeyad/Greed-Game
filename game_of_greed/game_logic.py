import collections
from itertools import count
from random import randint, sample, random

class GameLogic():
    numberOfDice=6
    bank=0

    def __init__(self):
        pass 
    
    def calculate_score(roll_dice):
        score = 0
        pairs_double =0 
        pairs_trible=0
        num = collections.Counter(roll_dice)
        
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

    # def greeting(self):
    #         play = input('do you want to play ? yes,or no?  ')
    #         if play == 'yes':
    #             print('lets do it ')
    #         elif play == 'no':
    #             print('we will play later')
            
    

    def roll_dice(self):
        roll = tuple(randint(1,6) for _ in range(0, self.numberOfDice))
        return roll

    def keeper(roll_dice):
        keeper=[]
        for x in roll_dice:
            pick = input(f'type yes if you want to keep  {x}  ')
            if pick == 'yes':
                keeper.append(x)

        return keeper
    
    def number_dice(self,keeper,roll_dice):
        self.numberOfDice = -len(roll_dice)+len(keeper)
        
        
class Banker:

    def __init__(self):
        self.shelved = 0
        self.balance= 0
 
    def shelf(self,num):
        self.shelved += num
   
    def bank(self):
        self.balance += self.shelved
        self.shelved = 0
        return self.balance

    def clear_shelf(self):
        self.shelved = 0


if __name__ == "__main__":
    x = GameLogic.roll_dice(GameLogic)
    print(x)
    y = GameLogic.keeper(x)
    game = GameLogic.calculate_score(y)
    print(y)
    print(game)


    x = GameLogic.roll_dice(GameLogic)
    print(x)
    y = GameLogic.keeper(x)
    game = GameLogic.calculate_score(y)
    print(y)
    print(game)

