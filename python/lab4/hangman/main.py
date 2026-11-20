import random
import repository

class Hangman:
    def __init__(self):
        self.word = ""
        self.list_of_guessed_words = []
        self.ascii = Ascii_Loader()

    def display_guessed_words(self) -> bool:
        ok = True
        for i in self.word:
            if i in self.list_of_guessed_words:
                print(i, end=" ")
            else:
                ok = False
                print("_", end=" ")

        if ok:
            return 1
        return 0

    def play(self):
        self.select_word()
        tries = 5
        while True:
            print("\n" + self.ascii.get_stage(tries))

            if tries == 0:
                print("Game over!")
                break

            ans = self.display_guessed_words()

            if ans:
                print("Congratz!")
                break

            character = input("Guess: ")  

            if character in self.word and not(character in self.list_of_guessed_words):
                self.list_of_guessed_words.append(character)
            else:
                tries -= 1
                print(f"{tries} more tries")

    def select_word(self):
        list = repository.read_from_json("./words.json")
        index = random.randint(0, len(list) - 1)
        self.word = list[index]

class Ascii_Loader:
    def __init__(self):
        self.filepath = "./ascii.json"
        self.stages = self.load_stages()

    def load_stages(self) -> list[str]:
        raw_stages = repository.read_from_json(self.filepath)
        return ["\n".join(stage) for stage in raw_stages]

    def get_stage(self, tries_left: int) -> str:
        index = (len(self.stages) - 1) - tries_left
        if 0 <= index < len(self.stages):
            return self.stages[index]
        return ""

if __name__ == "__main__":
    test = Hangman()
    test.play()
