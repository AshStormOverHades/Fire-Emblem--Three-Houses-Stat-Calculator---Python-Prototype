from operator import add
import numpy as np


class_growths_dic = (
#Beginner Classes
{"Noble":[0,0,0,0,0,0,0,0,0.05], 
"Commoner":[0,0,0,0,0,0,0,0,0], 

#Special Classes
"Dancer":[0.2,-0.05,0,0,0,0,-0.5,-0.5,0.1],
"Enlightened One":[0.2,0.1,0.1,0,0,0,0.5,0,0.1],

#House Leader Classes

"Armored Lord":[0.2,0.05,0.05,0,0,0,0.05,0.05,0.1],
"Emperor":[0.3,0.1,0.1,0,0,0,0.05,0.05,0.1],

"Wyvern Master":[0.2,0.1,0,0,0.05,0,0.05,0,0.1],
"Barbarossa":[0.3,0.15,0,0,0.1,0,0.05,0,0.1],

"High Lord":[0.2,0.05,0,0.05,0,0,0.05,0,0.1],
"Great Lord":[0.3,0.1,0,0.1,0,0,0.05,0,0.1],

#Beginner Classes
"Myrmidon":[0.1,0,0,0,0.05,0,0,-0.05,0.05],
"Soldier":[0.1,0,0,0.05,0,0,0,-0.05,0.05],
"Fighter":[0.1,0.05,0,0,0,0,0,-0.05,0.05],
"Monk":[0.05,0,0,0,0,0,0,0.05,0.05],

#Intermediate Classes
"Lord":[0.2,0,0,0.1,0,0,0,0,0.1],
"Mercenary":[0.2,0.05,0,0,0.05,0,0,-0.05,0.05],
"Thief":[0.2,0,0,0.1,0.1,0,0,0,0.05],
"Armored Knight":[0.2,0,0,0,-0.1,0,0.1,-0.05,0.05],
"Cavalier":[0.2,0.05,0,0.05,-0.1,0,0.05,0,0.05],
"Brigand":[0.3,0.1,0,0,0,0,0,-0.05,0.05],
"Archer":[0.05,0,0,0.1,0,0.05,0,0,0.05],
"Brawler":[0.3,0,-0.1,0.1,0.1,0,0,-0.1,0.05],
"Mage":[0.05,-0.05,0.1,0.05,0,0,-0.05,0.05,0.05],
"Dark Mage":[0.05,-0.05,0.1,0.05,0,0,-0.05,0.05,0],
"Priest":[0.05,-0.05,0.05,0.05,0,0,-0.05,0.1,0.1],
"Pegasus Knight":[0.15,0,0,0,0.1,0,0,0.05,0.1],

#Advanced Classes
"Hero":[0.3,0.1,0,0,0.1,0,0,-0.05,0.05],
"Swordmaster":[0.25,0.1,0,0,0.2,0,0,-0.5,0.05],
"Assassin":[0.2,0,0,0.2,0.2,0,0,0,0,],
"Fortress Knight":[0.3,0.1,0,0,-0.1,0,0.15,0,0.05],
"Paladin":[0.3,0.1,0,0.05,-0.1,0.05,0.05,0.05,0.05],
"Wyvern Rider":[0.3,0.1,-0.05,0,0,0,0.05,-0.05,0.05],
"Warrior":[0.4,0.15,-0.05,0,0,0,0,0,0.05],
"Sniper":[0.1,0.05,0,0.2,0,0.1,0,0,0.05],
"Grappler":[0.4,0.1,0,0.1,0.1,0,0,0,0.05],
"Warlock":[0.1,0,0.1,0,0,0,-0.05,0.05,0.05],
"Dark Bishop":[0.1,0,0.1,0,0,0,-0.05,0.05,0],
"Bishop":[0.1,0,0.1,0,0,0.1,-0.05,0.05,0.1],

#Master
"Falcon Knight":[0.3,0.1,0,0,0.2,0,0,0.05,0.1],
"Wyvern Lord":[0.3,0.15,-0.05,0,0.1,0,0.05,0,0.05],
"Mortal Savant":[0.2,0.1,0.1,0,-0.1,0.1,0,0,0.05],
"Great Knight":[0.3,0.1,0,0,-0.1,0,0.05,-0.05,0.05],
"Bow Knight":[0.1,0,0,0,-0.05,0,0,0,0.05],
"Dark Knight":[0.1,0.05,0.1,0,-0.05,0,0.05,0.1,0.05],
"Holy Knight":[0.1,0,0.1,0,-0.05,0.1,0.05,0.1,0.1],
"War Master":[0.4,0.15,0,0,0.1,0,0,0,0.05],
"Gremory":[0.1,0,0.1,0.1,0,0,0,0.05,0.1],

#DLC (have not introduced wave 4 classes yet as there is no data ***Update needed)
"Death Knight":[0.3,0.1,0.1,0,-0.05,0,0.05,0.05,0]})

Character_Stats_Dic=({
    "Byleth":[0.45,0.45,0.35,0.45,0.45,0.45,0.35,0.3,0.45],
    "Edelgard":[0.4,0.55,0.45,0.45,0.4,0.3,0.35,0.35,0.6]

})



#Base Stats 
Base_stats = ({
    "Byleth":[27,13,6,9,8,8,6,6,7],

    #Black Eagles
    "Edelgard":[29,13,6,5,8,5,6,4,10],
    "Hubert":[22,6,12,6,7,6,4,7,6],
    "Dorothea":[24,5,11,6,7,6,4,7,8],
    "Ferdinand":[28,8,5,6,8,6,6,2,7],
    "Bernadetta":[25,8,5,7,7,5,4,2,6],
    "Caspar":[26,9,3,5,6,8,6,2,4],
    "Petra":[25,9,3,7,10,7,5,2,6],
    "Linhardt":[24,5,10,6,5,7,5,9,3],

    #Blue Lions
    "Dimitri":[28,12,4,7,7,5,7,4,9],
    "Dedue":[30,12,2,5,7,5,8,1,4],
    "Felix":[26,10,5,6,9,5,5,3,5],
    "Mercedes":[25,6,10,6,8,5,5,9,8],
    "Ashe":[23,8,5,8,9,6,5,6,5],
    "Annette":[23,6,11,7,7,6,5,4,6],
    "Sylvain":[27,9,5,5,8,6,6,2,7],
    "Ingrid":[27,8,6,6,8,6,5,8,8],

    #Golden Dear
    "Claude":[26,11,5,8,8,7,6,4,8],
    "Lorenz":[28,8,7,6,7,5,6,6,3],
    "Hilda":[29,10,5,5,8,6,6,3,7],
    "Raphael":[30,11,3,5,6,6,7,1,4],
    "Lysithea":[24,4,11,7,7,4,3,4,5],
    "Ignatz":[25,8,5,7,8,8,4,6,4],
    "Marianne":[23,5,11,6,7,6,4,8,7],
    "Leonie":[26,9,5,8,9,6,7,2,7],

    #Church Of Seiros
    "Manuela":[26,10,8,6,8,6,5,4,7],
    "Hanneman":[25,6,10,6,6,4,5,7,5],
    "Seteth":[27,9,8,8,5,6,6,4,9],
    "Flayn":[24,6,9,6,5,4,5,10,9],
    "Cyril":[24,7,4,6,6,6,5,2,4],

    #Knights of Seiros
    "Catherine":[27,8,5,6,7,6,5,2,4],
    "Alois":[28,9,4,5,6,5,5,2,7],
    "Gilbert":[30,9,4,6,5,4,5,2,6],
    "Shamir":[26,8,4,7,6,8,5,2,6],

    #DLC
    "Jeritza":[30,8,6,6,8,4,7,5,3],
    "Anna":[26,7,7,7,7,7,5,7,7]









})

Stats_Order = ["HP","Str","Mag","Dex","Spd","Lck","Def","Res","Cha"]





"""Testing Variables and Testing Code

class_select = "War Master"
Character_Select = "Byleth"
class_table = []
Level_Select = 25 
Base_Table=[]



#Searches through class dictionary and finds the stats of the class that ahs been selected
for classes in class_growths_dic:
    class_table = class_growths_dic.get(class_select)
    break


print(class_table)

#Same as above but searches character growths 
for characters in Character_Stats_Dic:
    character_table = Character_Stats_Dic.get(Character_Select)
    break

print(character_table)


#Makes the total growth for the character + class combination
Total_growth_list = [character_table[i]+class_table[i] for i in range(len(character_table))]

print(Total_growth_list)


#Total growth value for this combination 
Sum_growths = sum(Total_growth_list)

print(Sum_growths)

#finds base stats for selected character 
for characters in Base_stats:
    Base_Table = Base_stats.get(Character_Select)
    break



#Calcualtes stats expected after leveling in the selected clas for the selected amount of lvls 
expected_at_lvl = list( map(add,(Level_Select*i for i in Total_growth_list), Base_Table))

print(expected_at_lvl)"""
Expected_list_Total =[]
Base_Table =[]

#Grouping it all into a function #GettingThere
def Calculator(Class, Character, Level):

    
    class_table = class_growths_dic.get(Class)

    print("That class has growths of: ")
    print(class_table)
    print(Stats_Order)
        

    
    character_table = Character_Stats_Dic.get(Character)
    print("This character has growths of: ")
    print(character_table)
    print(Stats_Order)
        

    Total_growth_list = [character_table[i]+class_table[i] for i in range(len(character_table))]
    print("In total (class + character) the growth is:")
    print(Total_growth_list)
    print(Stats_Order)

    Sum_growths = sum(Total_growth_list)
    print("The total value of this combination is:")
    print(Sum_growths)
    

    

    
    Base_Table = Base_stats.get(Character)
    print("This character has base stats of:")
    print(Base_Table)
    print(Stats_Order)
           


    expected_at_lvl = list( map(add,(Level*i for i in Total_growth_list), Base_Table))
    print("At lvl " + str(Level) +", " + str(Character) + ", " "as a " + str(Class) + ", " "will have stats: ")
    print(expected_at_lvl)
    print(Stats_Order)
    Expected_list_Total.append(expected_at_lvl)



class_input = str(input("Enter which class you want to level in: "))
character_input = str(input("Enter which character you want to level: "))
lvl_input = int(input("Enter how many levels you want them to level in that class: "))



Calculator(class_input, character_input, lvl_input)


Cont = str(input("Do you want to enter another class/lvl advancement? Type YES/NO: "))

if Cont == "YES":
    class_input = str(input("Enter which class you want to level in: "))
    character_input = str(input("Enter which character you want to level: "))
    lvl_input = int(input("Enter how many levels you want them to level in that class: "))
    Calculator(class_input, character_input, lvl_input)
else:
    print("Your total expected stats after those transitions are: ")

    ###Needs to be fixed, need to declare new variable and then do the operation for clarity, getting
    #too confusing
    for totals in Expected_list_Total:
        Final_Stats = (list( map(add((sum(lists) for lists in zip(*Expected_list_Total)),
        ((-1*(len(Expected_list_Total)-1))*i for i in Base_Table)))))
        break
        
        
    print(Final_Stats)

    


            
    















