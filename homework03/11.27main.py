#Mariam Vaid
#1477614

class sports:
    sport_detail = {}

    def players_jersey(self):
        for x in range(1, 6):
            jersey = int(input("Enter player {}'s jersey number:".format(x)))
            rating = int(input("\nEnter player {}'s rating:\n\n".format(x)))
            self.sport_detail[jersey] = rating

    def Roster_Jersey(self):
        sort_jersey = sorted(self.sport_detail.keys())
        print("ROSTER")
        for jersey in sort_jersey:
            print("Jersey number: {}, Rating: {}".format(jersey, self.sport_detail[jersey]))

    def menu(self):
        print("\nMENU")
        print("a - Add player")
        print("d - Remove player")
        print("u - Update player rating")
        print("r - Output players above a rating")
        print("o - Output roster")
        print("q - Quit")
        option = input("\nChoose an option:\n")
        return option

    def Adding_Player(self):
        jersey = int(input("Enter a new player's jersey number: "))
        rating = int(input("Enter the player's rating: "))
        self.sport_detail[jersey] = rating

    def Removing_Player(self):
        jersey = int(input("Enter a jersey number: "))
        del self.sport_detail[jersey]

    def UpdatingPlayer_Rating(self):
        jersey = int(input("Enter a jersey number: "))
        new_rate = int(input("Enter a new rating for player: "))
        self.sport_detail[jersey] = new_rate

    def Above_Rating(self):
        rating = int(input("Enter a rating"))
        sorted_jersey = sorted(self.sport_detail.keys())
        print("ABOVE {}".format(rating))
        for jersey in sorted_jersey:
            if(self.sport_detail[jersey]>rating):
                print("Jersey number: {}, Rating: {}".format(jersey,self.sport_detail[jersey]))


if __name__ == "__main__":
    obj = sports()
    obj.players_jersey()

    while (True):
        option = obj.menu()
        if (option == 'a'):
            obj.Adding_Player()
        elif (option == 'd'):
            obj.Removing_Player()
        elif (option == 'u'):
            obj.UpdatingPlayer_Rating()
        elif (option == 'r'):
            obj.Above_Rating()
        elif (option == 'o'):
            obj.Roster_Jersey()
        elif (option == 'q'):
            exit()
        else:
            print("Invalid option")




