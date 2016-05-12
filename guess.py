# coding:utf-8

# 猜字谜游戏

import random

result = int(random.randint(0, 100))


while True:
    
    inputNum = raw_input('Please guess a number: ');
    guess = int(inputNum)
    
    if guess > result:
        print 'This number is larger'
        
    if guess < result:
            print 'This number is smaller'
            
    if guess == result:
        print 'It\'s ok'       
        break 
            
