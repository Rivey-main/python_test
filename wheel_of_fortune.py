class WheelOfFortune:
    def __init__(self, word: str, max_errors: int = 5):
        if not word:
            raise ValueError("Слово не может быть пустым")
        self.word = word.lower()
        self.max_errors = max_errors
        self.guessed_letters = set()
        self.errors = 0

    def guess_letter(self, letter: str) -> bool:
        if len(letter) != 1 or not letter.isalpha():
            raise ValueError("Нужно ввести ровно одну букву")
        
        letter = letter.lower()
        if letter in self.guessed_letters:
            return False
            
        self.guessed_letters.add(letter)
        
        if letter not in self.word:
            self.errors += 1
            return False
        return True

    def get_display_word(self) -> str:
        return "".join([char if char in self.guessed_letters else "*" for char in self.word])

    def is_won(self) -> bool:
        return set(self.word).issubset(self.guessed_letters) and not self.is_game_over()

    def is_game_over(self) -> bool:
        return self.errors >= self.max_errors
