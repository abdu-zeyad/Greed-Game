import collections
from random import randint
class GameLogic():
    # numberOfDice=6
    # bank=0
    # totalscore=0

    def __init__(self):
        pass 
    
    def calculate_score(self,x )->int:
        score = 0
        pairs_double =0 
        pairs_trible=0
        num = collections.Counter(x)
        
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

    

    def roll_dice(x=6):
        dice=[]
        for i in range(x):
            dice.append(randint(1,6))
            roll = tuple(dice)
        return roll

    # def keeper(self,roll_dice):
    #     keeper=[]
    #     for dice in roll_dice:
    #         pick = input(f'type yes if you want to keep  {dice}  ')
    #         if pick == 'yes':
    #             keeper.append(dice)
    #             self.numberOfDice -=1
    #     score = self.calculate_score(tuple(keeper))
    #     self.bank +=score
    #     self.again_roll()
    #     return tuple(keeper)
    
    # def again_roll(self):
    #     again_roll=input('roll again')
    #     if again_roll== 'yes':
    #         roll = self.roll_dice()
    #         result = self.calculate_score(roll)
    #         if result == 0:
    #             print('you lost')
                
    #             self.bank = 0
    #         else:
    #             self.keeper(roll)
    #     elif again_roll  == 'n':
    #         self.totalscore +=self.bank
    
    # def show_results(self):
    #     print(f'{self.totalscore}')


        



if __name__ == "__main__":

    # values = GameLogic.roll_dice(1)
    # print(values)
   new_game= GameLogic()
# #    roll= new_game.roll_dice()
# #    keeper = new_game.keeper(roll)
# #    result=new_game.show_results()
    
# #    print(result)
#    print(new_game.calculate_score((1,1))) 
#    x=(new_game.roll_dice()) 
#    print(x) 
#    print(new_game.keeper(x)) 
#    print(new_game.show_results())