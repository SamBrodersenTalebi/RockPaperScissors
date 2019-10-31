"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random

moves = ['rock', 'paper', 'scissors']
"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        print("What would you like to play?")
        play = input()
        while play not in moves:
            play = input("Invalid move, try again: ")
        return play


class ReflectPlayer(Player):
    def __init__(self):
        self.reflect = ""

    def move(self):
        if self.reflect == "":
            return moves[0]
        else:
            return self.reflect

    def learn(self, my_move, their_move):
        self.reflect = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.cycle = ""

    def move(self):
        if self.cycle == "rock":
            return "paper"
        elif self.cycle == "paper":
            return "scissors"
        else:
            return "rock"

    def learn(self, my_move, their_move):
        self.cycle = my_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0
        self.game_number = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            self.score1 += 1
            print("Player 1 won the round")
            print(f"Score: Player 1: {self.score1} and Player 2: {self.score2}\n")
        elif beats(move2, move1):
            self.score2 += 1
            print("Player 2 won the round")
            print(f"Score: Player 1: {self.score1} and Player 2: {self.score2}\n")
        else:
            print("Tie round")
            print(f"Score: Player 1: {self.score1} and Player 2: {self.score2}\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(int(number)):
            print(f"Round {round}:")
            self.play_round()
        if self.score1 > self.score2:
            print("Player 1 won the game!")
        elif self.score1 < self.score2:
            print("Player 2 won the game!")
        else:
            print("Tie game!")


if __name__ == '__main__':
    number = input("This program plays a game of Rock, Paper, Scissors between two Players.\nPlease select the number of rounds you wish to play\n")
    while int(number) <= 0:
        number = input("Please enter a positive integer:")

    opponent_dict = {'reflect': ReflectPlayer(), 'circle': CyclePlayer(), 'random': RandomPlayer(), 'repeat': Player()}
    print("You can play against 4 different players: reflect, circle, random and repeat\n")
    list_opponent = ["reflect", "circle", "random", "repeat"]
    opponent = input("Select your opponent\n")
    while opponent not in list_opponent:
        opponent = input(("Invalid opponent, try again: "))

    game = Game(HumanPlayer(), opponent_dict[opponent])
    game.play_game()
