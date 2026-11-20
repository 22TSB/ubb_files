import random
import repository

class Rock_Paper_Scissors:
    def __init__(self):
        self.player_option = None
        self.computer_option = None
        self.rounds_won = 0

    def print_menu(self):
        print("Rock: 1 or rock")
        print("Paper: 2 or paper")
        print("Scissors: 3 or scissors")

    def display_ascii(self, player_option, computer_option):
        ascii_art = repository.read_from_json("./ascii.json")
        if player_option == "rock":
            print(ascii_art["rock"])
        elif player_option == "paper":
            print(ascii_art["paper"])
        elif player_option == "scissors":
            print(ascii_art["scissors"])

        if computer_option == "rock":
            print(ascii_art["rock"])
        elif computer_option == "paper":
            print(ascii_art["paper"])
        elif computer_option == "scissors":
            print(ascii_art["scissors"])

    def display_current_score(self):
        print(f"Your score: {self.rounds_won}")

    def display_high_score_list(self):
        high_score_list = repository.read_from_json("./score.json")
        high_score_list.sort(key=lambda entry: entry["score"], reverse=True)
        print("Leaderboard:")
        for i in high_score_list:
            print(f"{i["name"]}: {i["score"]}")

    def rock_paper_scissors_round(self):
        while True:
            self.print_menu()
            player_option = input("Choose: ")

            player = self.set_player_option(player_option)
            computer = self.set_computer_option()

            if player == computer:
                self.display_ascii(player, computer)
                print("Tie! Choose again!\n")
                continue
            elif player == "rock" and computer == "scissors":
                self.rounds_won += 1
                self.display_ascii(player, computer)
                print("won")
            elif player == "rock" and computer == "paper":
                self.display_ascii(player, computer)
                print("lost")
                break
            elif player == "paper" and computer == "rock":
                self.rounds_won += 1
                self.display_ascii(player, computer)
                print("won")
            elif player == "paper" and computer == "scissors":
                self.display_ascii(player, computer)
                print("lost")
                break
            elif player == "scissors" and computer == "paper":
                self.rounds_won += 1
                self.display_ascii(player, computer)
                print("won")
            elif player == "scissors" and computer == "rock":
                self.display_ascii(player, computer)
                print("lost")
                break

        self.display_current_score()
        if input("Would you like to save your score?: y/n") == "y":
            name = ""
            while name == "": 
                name = input("Enter name: ")

            list = High_score_table()
            list.set_High_Score(name, self.rounds_won)


    def set_computer_option(self):
        list = ["rock", "paper", "scissors"]
        self.computer_option = list[random.randint(0, 2)]
        return self.computer_option
    
    def set_player_option(self, player_option):
        if type(player_option) is int:
            if (player_option < 1 or player_option > 3):
                raise ValueError("error: bad value, try again")
            else:
                list = ["rock", "paper", "scissors"]
                index = player_option
                self.player_option = list[index - 1]

        elif type(player_option) is str: 
            player_option = player_option.lower()

            if (player_option == "1"):
                self.player_option = "rock"
            elif (player_option == "2"):
                self.player_option = "paper"
            elif (player_option == "3"):
                self.player_option = "scissors"
            elif (player_option != "rock" and player_option != "paper" and player_option != "scissors"):
                print("error: bad value, try again")
            else:
                self.player_option = player_option
        else:
            raise ValueError("Invalid type")

        return self.player_option

class High_score_table:
    def get_All_High_Scores(self):
        high_score_list = repository.read_from_json("./score.json")
        high_score_list.sort(key=lambda entry: entry["score"], reverse=True)

        return high_score_list

    def set_High_Score(self, name, score):
        high_score_list = repository.read_from_json("./score.json")
        high_score_list.append({"name": name, "score": score})
        repository.save_to_json(high_score_list, "./score.json")

if __name__ == "__main__":
    game = Rock_Paper_Scissors()
    game.rock_paper_scissors_round()
