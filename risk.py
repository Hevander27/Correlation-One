
# coding: utf-8

# In[1]:


from numpy import random as np_r

def rollDice(player_array): 
    
    if len(player_array)==4:
        limit = min(3, player_array[0])
    else:
        limit = min(2, player_array[0])
    
    for i in range(limit):
        player_array[i+1] = np_r.randint(1,6)
    
    return player_array
    


# In[2]:


import math
def  playGame(atk_array, def_array):
    
    atk_max = max(atk_array[1:])
    def_max = max(def_array[1:])
    unit_atk = atk_array[0]
    unit_def = def_array[0]

    if atk_max > def_max:
        def_array[0] = unit_def - 1
        if (unit_def <= 2):
            def_array[unit_def-3] = -1
    
    elif def_max > atk_max or def_max == atk_max:
        atk_array[0] = unit_atk - 1
        if (unit_atk <= 3):    
            atk_array[unit_atk-4] = -1
            



# In[4]:


import numpy as np       
input_atk_units = int(input('Enter total number of offensive units: '))
input_def_units = int(input('Enter total number of defensive units: '))



while True:
    actv_atk_units = int(input("Enter numbers of active attacking units: "))
    actv_def_units = int(input("Enter number of active defending units: "))
    if actv_atk_units <= input_atk_units and actv_def_units <= input_def_units:
        print(f"Attacker  Total Units: {input_def_units}", f"Active Units: {actv_atk_units}")
        print(f"Defender  Total Units: {input_def_units}", f"Active Units: {actv_def_units}")
        break
    else:
        print("ERRROR: Active units are more than total units")
        exit()

atk_array = [input_atk_units,None,None,None]
def_array = [input_def_units,None,None]

while True:
    
    stay_in_game = input('Continue Attack (Y/N):')
    if str.lower(stay_in_game) != 'y':
        print("\033[1m" + "Attacker Forfeited\nGame Ended")
        break
    else: 
        # Roll Dice 
        atk_array = np.array(rollDice(atk_array))
        def_array = np.array(rollDice(def_array))
     
        print("-------------------------------")
        print("Attacker:\nDice-> " f"|{atk_array[1]}|{atk_array[2]}|{atk_array[3]}|")
        print("Max-> ", max(atk_array[1:]))
        print("Defender:\nDice-> " f"|{def_array[1]}|{def_array[2]}|")
        print("Max-> ", max(def_array[1:]))
        
        # Play Game
        playGame(atk_array,def_array)
        print("-------------------------------")
        print(f"Attacker Units: {atk_array[0]}")
        print(f"Defender Units: {def_array[0]}")
        print("*******************************")
        if atk_array[0] == 0:
            print("\033[1m" + "Defender Wins\nGame Ended")
            break
        elif def_array[0] == 0:
            print("\033[1m" + "Attacker Wins\nGame Ended")
            break
        
        elif actv_atk_units >= atk_array[0]:
              break
    
    


# In[ ]:




