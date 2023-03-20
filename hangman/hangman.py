from random import choice


class Word:
    def __init__(self):
        self.word = choice(['python', 'java', 'kotlin', 'javascript'])
        self.hidden = '-' * len(self.word)
        self.guesses = set()
        self.lives = 8

    def guess(self, letter):
        if letter in self.word:
            self.hidden = ''.join([letter if self.word[i] == letter else self.hidden[i] for i in range(len(self.word))])
        else:
            self.lives -= 1
            print('You have {} lives left'.format(self.lives))
        self.guesses.add(letter)


class Hangman:
    def __init__(self):
        self.word = Word()

    def play(self):
        while self.word.lives > 0:
            print(self.word.hidden)
            letter = input('Input a letter: ')
            if len(letter) != 1:
                print('You should input a single letter')
            elif not letter.islower():
                print('It is not an ASCII lowercase letter')
            elif letter in self.word.guesses:
                print('You already typed this letter')
            else:
                self.word.guess(letter)
                if self.word.hidden == self.word.word:
                    print('You guessed the word!')
                    return
        print('You are hanged!')


if __name__ == '__main__':
    game = Hangman()
    game.play()
