MISSING_FEST_TROPHY = "Follow the trail. The trophy is safe, but you’ll need to think before you can reach it."
ENTER_TREASURE_HUNT = "Welcome to the treasure hunt! "


#Target place class.
class TargetPlace:
    def __init__(self, placename, description):
        self.placename = placename
        self.description = description

    def visitedplace(self):
        return f"You are at the {self.placename}. {self.description}"  #Mention place name and explanation about place

# classes for Canteen, ComputerLab, and MainStage
class Canteen(TargetPlace): #Inherite from TargetPlace class
    def __init__(self):       
            super().__init__("Canteen", "Chech your key hidden under a table") #Super method is used to call the __init__ constructor of the parent class TargetPlace
    # I want to collect the key into bag
    def collect_in_bag(self, bag):  #Polymorphism
        if "YourKey" not in bag:
            bag.append("YourKey")
            return "You found the key, kept in bag, now go to next step."
        else:
            return "The key is already in bag now go to next step."

        
class ComputerLab(TargetPlace): #Inherite from TargetPlace class
    def __init__(self):        
            super().__init__("Computer Lab", "The door is locked !. \nYou need a key to open the door.") #Super method is used to call the __init__ constructor of the parent class TargetPlace
    # I want to collect the key into bag
    def enter_to_lab(self, bag):
        if "YourKey" not in bag:            
            return "The door is locked. You need a key to enter to lab."
        else:
            return "Bravo ! Use th key and get in the lab."

    #collect the chest code from computer lab
    def collect_in_bag(self, bag):  #Polymorphism
        if "YourCode" not in bag:
            bag.append("YourCode")
            return "You found the cdoe, kept in bag, now go to next step."
        else:
            return "The code is  already in baag now go to next step."

class MainStage(TargetPlace):
    def __init__(self):
        super().__init__("Main Stage", "Enter code to get trophy from chest.") #Super method is used to call the __init__ constructor of the parent class TargetPlace

    def entercode_open_chest(self, bag):
            if"YourCode" in bag:
                return "Code accepted !. CONGRATULATIONS! You found the TROPHY!."
            else:
                return "No code or Wrong Code, Enter the code to open the chest!"

class GamePlayer:
    def __init__(self):
        self.bag=[]

    def check_bag(self):
            if self.bag:
                return f"Your bag has: {(self.bag)}"
            else:
                return "Your bag is empty."
            
# I took help of AI here to create MyGame class I was not able to think how to proceed, I was thinking to create the class objects inside the star method.
class MyGame:
     def __init__(self):  
            self.GamePlayer = GamePlayer()
            self.canteen = Canteen()
            self.computer_lab = ComputerLab()
            self.main_stage = MainStage()
    
     def startGame(self):
            print(ENTER_TREASURE_HUNT)
            while True:
                print("\nSelect your first option?")
                print("1. Canteen")
                print("2. Computer Lab")
                print("3. Main Stage")
                print("4. Check Bag")
                print("5. Exit Game")
                choice = input("Enter the number of your choice: ")
    
                if choice == "1":
                    print(self.canteen.visitedplace())
                    print(self.canteen.collect_in_bag(self.GamePlayer.bag))
                elif choice == "2":
                    print(self.computer_lab.visitedplace())
                    enter_response = self.computer_lab.enter_to_lab(self.GamePlayer.bag)
                    print(enter_response)
                    if "Bravo" in enter_response:
                        print(self.computer_lab.collect_in_bag(self.GamePlayer.bag))
                elif choice == "3":
                    print(self.main_stage.visitedplace())
                    print(self.main_stage.entercode_open_chest(self.GamePlayer.bag))
                elif choice == "4":
                    print(self.GamePlayer.check_bag())
                elif choice == "5":
                    print("Exiting the game. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")


if __name__ == "__main__":
    UserChoice = input(MISSING_FEST_TROPHY + "Would you like to play the game? (yes/no): ")
    if UserChoice.lower() == "yes":       
        game = MyGame()
        game.startGame() 
    else:
        print("You quit! Goodbye!") 