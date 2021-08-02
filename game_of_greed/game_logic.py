import collections
from itertools import count
from random import randint, sample, random

class GameLogic():
    

    def __init__(self):
        pass 
    
    def calculate_score(test_input):
        score = 0
        pairs_double =0 
        pairs_trible=0
        num = collections.Counter(test_input)
        
        """ myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
          Counter({2: '4', 3: '4', 1: '3', 4: '2', 5: '1'})
    
            >>> print Counter(myList).keys()
            i=[1, 2, 3, 4, 5]
            >>> 
            >>> print Counter(myList).values()
            num[i]=[3, 4, 4, 2, 1]
        """

        if 1 in num and 2 in num and 3 in num and 4 in num and 5 in num and 6 in num:
            
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

        
    def roll_dice(times=6):
        return tuple(randint(1,6) for _ in range(0, times))
    #  return sample(range(1, 6 + 1), times)


if __name__ == "__main__":
    new_game = GameLogic.calculate_score((1, 1, 1, 2, 2, 2))
    print(new_game)
   
