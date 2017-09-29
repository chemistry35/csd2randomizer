'''Cook Serve Delicious! 2!! Randomizer'''
import sqlite3
from tkinter import *
sqlite_file = 'CSDTable.sqlite'
table_name = 'csd'
column_1 = 'name'
column_2 = 'type'
column_3 = 'hs'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()


class Gui(Tk):
    def __init__(self):
        Tk.__init__(self)
        numberEntree = StringVar(self)
        numberSides = StringVar(self)
        numberDrinks = StringVar(self)
        limitStatus = StringVar(self)


        labelHeader = Label(self, text = "Cook Serve Delicious! 2!! Randomizer")
        labelEntree = Label(self, text = "Number of entrees:")
        labelSides = Label(self, text = "Number of sides:")
        labelDrinks = Label(self, text = "Number of drinks:")
        labelHS = Label (self, text = "Reasonable holding station limits?")
        labelHSExp = Label(self, text = "(No more than half of menu is HS Required)")
        menuEntree = OptionMenu (self, numberEntree, "1", "2", "3", "4", "5", "6")
        menuSides = OptionMenu (self, numberSides, "0", "1", "2", "3")
        menuDrinks = OptionMenu (self, numberDrinks, "0","1", "2")
        checkLimit = Checkbutton (self, variable=limitStatus)
        labelEntreeMenu = Label(self, text = "")
        labelSideMenu = Label(self, text = "")
        labelDrinkMenu = Label(self, text = "")


       

        labelMenuOutput =  Label(self, text = "")
        labelHeader.grid(row = 1, column = 1, columnspan = 2)
        labelEntree.grid(row = 2, column = 1, columnspan = 1)
        labelSides.grid(row = 3, column = 1, columnspan = 1)
        labelDrinks.grid(row = 4, column = 1, columnspan = 1)
        labelHS.grid (row = 5, column = 1, columnspan = 1)
        labelHSExp.grid (row = 6, column = 1, columnspan = 1)
        menuEntree.grid (row = 2, column = 2, columnspan = 1)
        menuSides.grid (row = 3, column = 2, columnspan = 1)
        menuDrinks.grid(row = 4, column = 2, columnspan = 1)
        checkLimit.grid(row = 5, column = 2, columnspan = 1)
        labelEntreeMenu.grid(row = 8, column = 1, columnspan = 2)
        labelSideMenu.grid(row = 9, column = 1, columnspan = 2)
        labelDrinkMenu.grid(row = 10, column = 1, columnspan = 2)

        def generate(): 
            numberEntreeFixed = numberEntree.get()
            numberEntreeFixed = int(numberEntreeFixed)
            numberSidesFixed = numberSides.get()
            numberSidesFixed = int(numberSidesFixed)
            numberDrinksFixed = numberDrinks.get()
            numberDrinksFixed = int(numberDrinksFixed)
            limitStatusFixed = limitStatus.get()

            
            if limitStatusFixed == 0:
                menuItems = 0
                entrees = "Entrees: "
                sides = "Sides: "
                drinks = "Drinks: "
                numberSidesCurrent = 0
                numberDrinksCurrent = 0
                while menuItems < numberEntreeFixed:
                    c.execute('SELECT * FROM {tn} WHERE {cot} = "Entrée" ORDER BY random() LIMIT 1'.\
                              format(tn=table_name, cot=column_2))
                    for row in c:
                        name = row[0]
                    menuItems = menuItems + 1
                    entrees = entrees + name
                    if menuItems == numberEntreeFixed:
                        pass
                    else:
                        entrees = entrees + " , "
                while numberSidesCurrent < numberSidesFixed:
                    c.execute('SELECT * FROM {tn} WHERE {cot} = "Sides" ORDER BY random() LIMIT 1'.\
                              format(tn=table_name, cot=column_2))
                    for row in c:
                        name = row[0]
                    numberSidesCurrent = numberSidesCurrent + 1
                    sides = sides + name
                    if numberSidesCurrent == numberSidesFixed:
                        pass
                    else:
                        sides = sides + " , "
                while numberDrinksCurrent < numberDrinksFixed:
                    c.execute('SELECT * FROM {tn} WHERE {cot} = "Drink" ORDER BY random() LIMIT 1'.\
                              format(tn = table_name, cot = column_2))
                    for row in c:
                        name = row[0]
                    numberDrinksCurrent = numberDrinksCurrent + 1
                    drinks = drinks + name
                    if numberDrinksCurrent == numberDrinksFixed:
                        pass
                    else:
                        drinks = drinks + " , "

                labelEntreeMenu['text']=entrees
                labelSideMenu['text']=sides
                labelDrinkMenu['text'] = drinks

                if numberSidesCurrent == 0:
                    labelSideMenu['text'] = "No sides."
                else:
                    pass
                if numberDrinksCurrent == 0:
                    labelDrinkMenu['text'] = "No drinks."
                else:
                    pass

            else:
                menuItems = 0
                menuItemsHS = 0
                output = "Entrees: "
                outputSides = "Sides: "
                outputDrinks = "Drinks: "
                numberSidesCurrent = 0
                numberDrinksCurrent = 0
                while menuItems < numberEntreeFixed:
                    c.execute('SELECT * FROM {tn} WHERE {cot} = "Entrée" ORDER BY random() LIMIT 1'.\
                              format(tn=table_name, cot=column_2))
                    for row in c:
                        name = row[0]
                        hs = row [2]
                    if hs == "Required":
                        if menuItemsHS < numberEntreeFixed / 2:
                            pass
                        else:
                            menuItemsHS = menuItemsHS + 1
                            menuItems = menuItems + 1
                            output = output + name
                            if menuItems == numberEntreeFixed:
                                pass
                            else:
                                output = output + " , "
                    else:
                        menuItems = menuItems + 1
                        output = output + name
                        if menuItems == numberEntreeFixed:
                            pass
                        else:
                            output = output + " , "
                labelEntreeMenu['text'] = output
                while numberSidesCurrent < numberSidesFixed:
                    c.execute('SELECT ({coi}) FROM {tn} WHERE {cot} = "Side" ORDER BY random() LIMIT 1'.\
                          format (coi = column_1, tn= table_name, cot = column_2))
                    for row in c:
                        name = row[0]
                    outputSides = outputSides + name
                    numberSidesCurrent = numberSidesCurrent + 1
                    if numberSidesCurrent == numberSidesFixed:
                        pass
                    else:
                        outputSides = outputSides + " , "
                labelSideMenu['text'] = outputSides
                while numberDrinksCurrent < numberDrinksFixed:
                    c.execute('SELECT ({coi}) FROM {tn} WHERE {cot} = "Drink" ORDER BY random() LIMIT 1'.\
                              format(coi = column_1, tn = table_name, cot = column_2))
                    for row in c:
                        name = row[0]
                    outputDrinks = outputDrinks + name
                    numberDrinksCurrent = numberDrinksCurrent + 1
                    if numberDrinksCurrent == numberDrinksFixed:
                        pass
                    else:
                        outputDrinks = outputDrinks + " , "
                labelDrinkMenu['text'] = outputDrinks


                if numberSidesCurrent == 0:
                    labelSideMenu['text'] = "No sides."
                else:
                    pass
                if numberDrinksCurrent == 0:
                    labelDrinkMenu['text'] = "No drinks."
                else:
                    pass
            
                            
        buttonGo = Button(self, text = "Generate menu!",  command = generate)
        buttonGo.grid(row = 7, column = 1, columnspan = 2)
                      
def main():
    workingGui = Gui()
    workingGui.mainloop()

if __name__ == "__main__":
    main()
