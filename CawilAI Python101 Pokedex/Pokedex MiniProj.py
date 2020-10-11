import pandas as pd
import glob

##############################
#     Print Pokemon Data     #
##############################
def pokeData(boolsel):
    print("Pokemon No.: ", boolsel.loc[:,"pokedex_number"].values, "\n"
          "English Name: ", boolsel.loc[:,"name"].values, "\n"
          "Japanese Name: ", boolsel.loc[:,"japanese_name"].values, "\n"
          "Classification: ", boolsel.loc[:,"classfication"].values, "\n"
          "Type(s): ", boolsel.loc[:,"type1"].values, "|",  boolsel.loc[:,"type2"].values,"\n"
          "Height(m): ", boolsel.loc[:,"height_m"].values, "\n"
          "Weight(kg): ", boolsel.loc[:,"weight_kg"].values, "\n")
    
    ##############################
    #       For image index      #
    ##############################
    index = boolsel.index

##############################
#             Main           #
##############################
pokecsv = pd.read_csv('pokemon.csv', index_col=False)

search = ""
print("Hi, this is the ChanDex Pokedex Project")

while search != "Z":
    print("If you want to search a Pokemon by name, type 'A'")
    print("If you want to search a Pokemon by number, type 'B'")
    print("If you want to look at Pokemon with a certain type, type 'C'")
    print("If you want to look at the entire Pokedex, type 'Y'")
    print("To exit, type 'Z'")
    search = str.upper(input("Please select your choice: "))
    
    ##############################
    #       By Pokemon Name      #
    ##############################
    if search == "A":
        name = str.capitalize(input("Please input the Pokemon name: "))

        namelist = pokecsv["name"].values.tolist()
        while (name not in namelist):
            name = str.capitalize(input("Please input a valid Pokemon name: "))

        boolsel = pokecsv[pokecsv['name'] == name]
        pokeData(boolsel)

    ##############################
    #     By Pokemon Number      #
    ##############################    
    elif search == "B":
        num = int(input("Please input the Pokemon number: "))

        while (1 > num or num > 801):
            num = int(input("Pokemon Number out of range, please enter again: "))

        boolsel = pokecsv[pokecsv['pokedex_number'] == num]    
        pokeData(boolsel)

    ##############################
    #      By Pokemon Type       #
    ##############################
    elif search == "C":
        poketype = str.lower(input("Please input the Pokemon type: "))

        type1list = pokecsv["type1"].values.tolist()
        type2list = pokecsv["type2"].values.tolist()
        while (poketype not in type1list or poketype not in type2list):
            poketype = str.lower(input("Please input a valid Pokemon type: "))

        boolsel = pokecsv[(pokecsv['type1'] == poketype) | (pokecsv['type2'] == poketype)]
        print(boolsel.loc[:,["name","type1","type2"]], "\n")

    ##############################
    #       Entire Pokedex       #
    ##############################
    elif search == "Y":
        print(pokecsv.loc[:,["pokedex_number", 
                             "name", 
                             "japanese_name", 
                             "classfication", 
                             "type1", 
                             "type2", 
                             "height_m", 
                             "weight_kg"]])
    
    ##############################
    #            EXIT            #
    ##############################    
    elif search == "Z":
        print("Thank you for using the ChanDex Pokedex Project!")
        break
    
    else:
        print("Please input a valid choice \n")