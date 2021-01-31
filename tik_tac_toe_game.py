#!/usr/bin/env python
# coding: utf-8

# In[1]:


# have to check whether any player-1 has won

# possible combinations

# 123
# 147
# 159
# 258
# 369
# 357
# 456
# 789

def combination_check_player1(a=[]):
    """ 
    This function will check whether
    any of the player has entered a 
    successful combination
    """
    
    # will check combination 123
    
    if 1 in a:
        if 2 in a:
            if 3 in a:
                result = 'Player-1 has won the game'
                return result
                                
        # will check combination 147
        
        elif 4 in a:
            if 7 in a:
                result = 'Player-1 has won the game'
                return result
                
        # will check combination 159
        
        elif 5 in a:
            if 9 in a:
                result = 'Player-1 has won the game'
                return result
                
    # will check combination 258
    
    elif 2 in a:
        if 5 in a:
            if 8 in a:
                result = 'Player-1 has won the game'
                return result
                
    # will check combination 369
    
    elif 3 in a:
        if 6 in a:
            if 9 in a:
                result = 'Player-1 has won the game'
                return result
                
        # will check combination 357
        
        elif 5 in a:
            if 7 in a:
                result = 'Player-1 has won the game'
                return result
                
    # will check combination 456
    
    elif 4 in a:
        if 5 in a:
            if 6 in a:
                result = 'Player-1 has won the game'
                return result
                
    # will check combination 789
    
    elif 7 in a:
        if 8 in a:
            if 9 in a:
                result = 'Player-1 has won the game'
                return result
    


# In[2]:


# have to check whether any player-1 has won

# possible combinations

# 123
# 147
# 159
# 258
# 369
# 357
# 456
# 789

def combination_check_player2(a=[]):
    """ 
    This function will check whether
    any of the player has entered a 
    successful combination
    """
    # will check combination 123
    
    if 1 in a:
        if 2 in a:
            if 3 in a:
                result = 'Player-2 has won the game'
                return result
                
        # will check combination 147
        
        elif 4 in a:
            if 7 in a:
                result = 'Player-2 has won the game'
                return result
                
        # will check combination 159
        
        elif 5 in a:
            if 9 in a:
                result = 'Player-2 has won the game'
                return result
                
    # will check combination 258
    
    elif 2 in a:
        if 5 in a:
            if 8 in a:
                result = 'Player-2 has won the game'
                return result
                
    # will check combination 369
    
    elif 3 in a:
        if 6 in a:
            if 9 in a:
                result = 'Player-2 has won the game'
                return result
                
        # will check combination 357
        
        elif 5 in a:
            if 7 in a:
                result = 'Player-2 has won the game'
                return result
                
    # will check combination 456
    
    elif 4 in a:
        if 5 in a:
            if 6 in a:
                result = 'Player-2 has won the game'
                return result
                
    # will check combination 789
    
    elif 7 in a:
        if 8 in a:
            if 9 in a:
                result = 'Player-2 has won the game'
                return result


# In[3]:


def table(a=[], b=[]):
    
    # creating each element in the board row by row
    # r1 is 'row 1' and r2 is 'row 2' and so on...

    x_r1 = 'xx    xx'
    x_r2 = ' xx  xx '
    x_r3 = '  xxxx  '
    x_r4 = '   xx   '
    x_r5 = '  xxxx  '
    x_r6 = ' xx  xx '
    x_r7 = 'xx    xx'

    o_r1 = '   OO   '
    o_r2 = ' OO  OO '
    o_r3 = 'OO    OO'
    o_r4 = 'OO    OO'
    o_r5 = 'OO    OO'
    o_r6 = ' OO  OO '
    o_r7 = '   OO   '


    one_r1 = ' 11111111'
    one_r2 = ' 11111111'
    one_r3 = ' 11111111'
    one_r4 = ' 11111111'
    one_r5 = ' 11111111'
    one_r6 = ' 11111111'
    one_r7 = ' 11111111'
    one_r8 = '         '

    two_r1 = ' 22222222'
    two_r2 = ' 22222222'
    two_r3 = ' 22222222'
    two_r4 = ' 22222222'
    two_r5 = ' 22222222'
    two_r6 = ' 22222222'
    two_r7 = ' 22222222'
    two_r8 = '         '

    three_r1 = ' 33333333'
    three_r2 = ' 33333333'
    three_r3 = ' 33333333'
    three_r4 = ' 33333333'
    three_r5 = ' 33333333'
    three_r6 = ' 33333333'
    three_r7 = ' 33333333'
    three_r8 = '         '

    four_r1 = ' 44444444'
    four_r2 = ' 44444444'
    four_r3 = ' 44444444'
    four_r4 = ' 44444444'
    four_r5 = ' 44444444'
    four_r6 = ' 44444444'
    four_r7 = ' 44444444'
    four_r8 = '         '

    five_r1 = ' 55555555'
    five_r2 = ' 55555555'
    five_r3 = ' 55555555'
    five_r4 = ' 55555555'
    five_r5 = ' 55555555'
    five_r6 = ' 55555555'
    five_r7 = ' 55555555'
    five_r8 = '         '

    six_r1 = ' 66666666'
    six_r2 = ' 66666666'
    six_r3 = ' 66666666'
    six_r4 = ' 66666666'
    six_r5 = ' 66666666'
    six_r6 = ' 66666666'
    six_r7 = ' 66666666'
    six_r8 = '         '

    seven_r1 = ' 77777777'
    seven_r2 = ' 77777777'
    seven_r3 = ' 77777777'
    seven_r4 = ' 77777777'
    seven_r5 = ' 77777777'
    seven_r6 = ' 77777777'
    seven_r7 = ' 77777777'
    seven_r8 = '         '

    eight_r1 = ' 88888888'
    eight_r2 = ' 88888888'
    eight_r3 = ' 88888888'
    eight_r4 = ' 88888888'
    eight_r5 = ' 88888888'
    eight_r6 = ' 88888888'
    eight_r7 = ' 88888888'
    eight_r8 = '         '

    nine_r1 = ' 99999999'
    nine_r2 = ' 99999999'
    nine_r3 = ' 99999999'
    nine_r4 = ' 99999999'
    nine_r5 = ' 99999999'
    nine_r6 = ' 99999999'
    nine_r7 = ' 99999999'
    nine_r8 = '         '
    
    # placing x or o on the basis of user input on the table
    # by replacing row by row

    if 1 in a:
        one_r1 = x_r1
        one_r2 = x_r2
        one_r3 = x_r3
        one_r4 = x_r4
        one_r5 = x_r5
        one_r6 = x_r6
        one_r7 = x_r7
        
    if 1 in b:
        one_r1 = o_r1
        one_r2 = o_r2
        one_r3 = o_r3
        one_r4 = o_r4
        one_r5 = o_r5
        one_r6 = o_r6
        one_r7 = o_r7
        
    if 2 in a:
        two_r1 = x_r1
        two_r2 = x_r2
        two_r3 = x_r3
        two_r4 = x_r4
        two_r5 = x_r5
        two_r6 = x_r6
        two_r7 = x_r7
        
    if 2 in b:
        two_r1 = o_r1
        two_r2 = o_r2
        two_r3 = o_r3
        two_r4 = o_r4
        two_r5 = o_r5
        two_r6 = o_r6
        two_r7 = o_r7
        
    if 3 in a:
        three_r1 = x_r1
        three_r2 = x_r2
        three_r3 = x_r3
        three_r4 = x_r4
        three_r5 = x_r5
        three_r6 = x_r6
        three_r7 = x_r7
        
    if 3 in b:
        three_r1 = o_r1
        three_r2 = o_r2
        three_r3 = o_r3
        three_r4 = o_r4
        three_r5 = o_r5
        three_r6 = o_r6
        three_r7 = o_r7
        
    if 4 in a:
        four_r1 = x_r1
        four_r2 = x_r2
        four_r3 = x_r3
        four_r4 = x_r4
        four_r5 = x_r5
        four_r6 = x_r6
        four_r7 = x_r7
        
    if 4 in b:
        four_r1 = o_r1
        four_r2 = o_r2
        four_r3 = o_r3
        four_r4 = o_r4
        four_r5 = o_r5
        four_r6 = o_r6
        four_r7 = o_r7
        
    if 5 in a:
        five_r1 = x_r1
        five_r2 = x_r2
        five_r3 = x_r3
        five_r4 = x_r4
        five_r5 = x_r5
        five_r6 = x_r6
        five_r7 = x_r7
        
    if 5 in b:
        five_r1 = o_r1
        five_r2 = o_r2
        five_r3 = o_r3
        five_r4 = o_r4
        five_r5 = o_r5
        five_r6 = o_r6
        five_r7 = o_r7
        
    if 6 in a:
        six_r1 = x_r1
        six_r2 = x_r2
        six_r3 = x_r3
        six_r4 = x_r4
        six_r5 = x_r5
        six_r6 = x_r6
        six_r7 = x_r7
        
    if 6 in b:
        six_r1 = o_r1
        six_r2 = o_r2
        six_r3 = o_r3
        six_r4 = o_r4
        six_r5 = o_r5
        six_r6 = o_r6
        six_r7 = o_r7
        
    if 7 in a:
        seven_r1 = x_r1
        seven_r2 = x_r2
        seven_r3 = x_r3
        seven_r4 = x_r4
        seven_r5 = x_r5
        seven_r6 = x_r6
        seven_r7 = x_r7
        
    if 7 in b:
        seven_r1 = o_r1
        seven_r2 = o_r2
        seven_r3 = o_r3
        seven_r4 = o_r4
        seven_r5 = o_r5
        seven_r6 = o_r6
        seven_r7 = o_r7
        
    if 8 in a:
        eight_r1 = x_r1
        eight_r2 = x_r2
        eight_r3 = x_r3
        eight_r4 = x_r4
        eight_r5 = x_r5
        eight_r6 = x_r6
        eight_r7 = x_r7
        
    if 8 in b:
        eight_r1 = o_r1
        eight_r2 = o_r2
        eight_r3 = o_r3
        eight_r4 = o_r4
        eight_r5 = o_r5
        eight_r6 = o_r6
        eight_r7 = o_r7
        
    if 9 in a:
        nine_r1 = x_r1
        nine_r2 = x_r2
        nine_r3 = x_r3
        nine_r4 = x_r4
        nine_r5 = x_r5
        nine_r6 = x_r6
        nine_r7 = x_r7
        
    if 9 in b:
        nine_r1 = o_r1
        nine_r2 = o_r2
        nine_r3 = o_r3
        nine_r4 = o_r4
        nine_r5 = o_r5
        nine_r6 = o_r6
        nine_r7 = o_r7
        
    # displaying the table
    
    print(one_r1 + two_r1 + three_r1)
    print(one_r2 + two_r2 + three_r2)
    print(one_r3 + two_r3 + three_r3)
    print(one_r4 + two_r4 + three_r4)
    print(one_r5 + two_r5 + three_r5)
    print(one_r6 + two_r6 + three_r6)
    print(one_r7 + two_r7 + three_r7)
    print(one_r8 + two_r8 + three_r8)

    print(four_r1 + five_r1 + six_r1)
    print(four_r2 + five_r2 + six_r2)
    print(four_r3 + five_r3 + six_r3)
    print(four_r4 + five_r4 + six_r4)
    print(four_r5 + five_r5 + six_r5)
    print(four_r6 + five_r6 + six_r6)
    print(four_r7 + five_r7 + six_r7)
    print(four_r8 + five_r8 + six_r8)

    print(seven_r1 + eight_r1 + nine_r1)
    print(seven_r2 + eight_r2 + nine_r2)
    print(seven_r3 + eight_r3 + nine_r3)
    print(seven_r4 + eight_r4 + nine_r4)
    print(seven_r5 + eight_r5 + nine_r5)
    print(seven_r6 + eight_r6 + nine_r6)
    print(seven_r7 + eight_r7 + nine_r7)
    print(seven_r8 + eight_r8 + nine_r8)


# In[12]:


game_status = True

while game_status:
    

    # computer must get an input from players

    # each entry of the players will be saved to these lists

    player1_choice_history = []    
    player2_choice_history = []

    result = None    # assigning a variable to break the for loop

    possible_inputs = ['1', '2', '3', '4', '5', '6', '7', '8', '9']    # variable for validating user input 



    # it will take inputs from players alternatively

    for x in range(1,10):
        player_turn = x % 2    # to switch between player 1 and player 2

        player_input_validation = False    # to run and break the while loop

        while player_input_validation == False:
            if player_turn != 0:
                print('Player-1\nPlease choose a colomn number from "1" to "9".')
                player_input1 = input()
                if player_input1 in possible_inputs:
                    player_input1 = int(player_input1)

                    # will check whether the same number has entered previously
                    # if so, it will not accept the entry

                    if (player_input1 in player1_choice_history) or (player_input1 in player2_choice_history):
                        print('This column has already played, choose another one')
                    else:
                        player1_choice = player_input1
                        player_input_validation = True

                else:
                    print('Please enter a valid number from "1" to "9"')

                player1_choice_history.append(player1_choice)
                player1_choice_history.sort()
                result = combination_check_player1(player1_choice_history)
                table(player1_choice_history, player2_choice_history)

            else:
                print('Player-2\nPlease choose a colomn number from "1" to "9".')
                player_input2 = input()
                if player_input2 in possible_inputs:
                    player_input2 = int(player_input2)

                    # will check whether the same number has entered previously
                    # if so, it will not accept the entry

                    if (player_input2 in player1_choice_history) or (player_input2 in player2_choice_history):
                        print('This column has already played, choose another one')
                    else:
                        player2_choice = player_input2
                        player_input_validation = True

                else:
                    print('Please enter a valid number from "1" to "9"')

                player2_choice_history.append(player2_choice)
                player2_choice_history.sort()
                combination_check_player2(player2_choice_history)
                table(player1_choice_history, player2_choice_history)

        if result is not None:
            print(result)
            break

        elif (result is None) and (x == 9):
            print('The game is a draw')
            
    local = True
    while local:
            
        game_termination = input('would you like to play another game?\npress "y"/"n"')
        game_termination.islower()
        if game_termination == 'n':
            local = False
            game_status = False
            break
        elif game_termination == 'y':
            local = False
            game_status = True
            break
        else:
            print('enter a valid input')
            local = True
            
        
    


# In[ ]:




