# -*- coding: utf-8 -*-
def fbuzz( number ) :    
    if number % 3 == 0 and number % 5 == 0 :
        return "fizzbuzz"
    elif number % 3 == 0 :
        return "fizz"
    elif number % 5 == 0 : 
        return "buzz"
    else :
        return 0

