import random
import copy

# instantiates the X and O array
moves = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
# instantiates the starting player
player = 'P1'
# instantiates all previous moves made array
prev_moves = []

# maps a string title of a move to a position in the move array
move_conversion = {
    'TL': (0, 0),
    'TM': (0, 1),
    'TR': (0, 2),
    'ML': (1, 0),
    'MM': (1, 1),
    'MR': (1, 2),
    'BL': (2, 0),
    'BM': (2, 1),
    'BR': (2, 2)
}


class Board:
    def __init__(self, prev, moves, player):
        self.moves = moves
        self.prev = prev
        self.player = player

    def toggle_player(self):
        if self.player == 'P1':
            self.player = 'P2'
        else:
            self.player = 'P1'

    def reset(self):
        self.moves = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.prev = []
        self.player = 'P1'

    def check_win(self):
        """Checks if there is a win, if so returns X or Y"""
        # checks cols and rows
        for i in range(3):
            if self.moves[i][0] == self.moves[i][1] == self.moves[i][2] and self.moves[i][0] != ' ':
                return self.moves[i][0]
            if self.moves[0][i] == self.moves[1][i] == self.moves[2][i] and self.moves[0][i] != ' ':
                return self.moves[0][i]
        # checks left right diagonal
        if self.moves[0][0] == self.moves[1][1] == self.moves[2][2] and self.moves[0][0] != ' ':
            return self.moves[0][0]
        # checks right left diagonal
        if self.moves[0][2] == self.moves[1][1] == self.moves[2][0] and self.moves[0][2] != ' ':
            return self.moves[0][2]
        if len(self.prev) == 9:
            return 'Tie'
        # if there is no win return None
        return None

    def empty(self):
        """Returns a list of the tuples of where there are empty squares on the board"""
        empty_sqrs = []
        # checks for empty squares
        for row in range(len(self.moves)):
            for col in range(len(self.moves[0])):
                if self.moves[row][col] == " ":
                    empty_sqrs.append((row, col))
        return empty_sqrs

    def print_gameboard(self):
        """prints out the gameboard to the screen"""
        print()
        for i in range(3):
            print(f"{self.moves[i][0]} | {self.moves[i][1]} | {self.moves[i][2]}", end='')
            if i < 2 and self.moves[0][0] != 'TL':
                print('\n_________')
            elif i < 2:
                # just keeps formatting correct whether it prints words or Xs/Os
                print('\n____________')
        print()
        print()

    def add_mark(self, position, player):
        """adds an X or an O onto the board, and returns the new player's turn"""
        row, col = position
        if player == 'P1':
            self.moves[row][col] = 'X'
        else:
            self.moves[row][col] = 'Y'
        spot = ''.join([key for key, val in move_conversion.items() if val == position])
        self.prev.append(spot)


class AI:
    def __init__(self, level=1, player='P2'):
        # if level = 0, it is a random game, if level=0 it is an AI game
        self.level = level
        self.player = player

    def rnd_choice(self, board):
        """of the empty squares chooses a random square"""
        empty_sqrs = board.empty()
        idx = random.randrange(0, len(empty_sqrs))
        return empty_sqrs[idx]

    def minmax(self, board, maximizing=False):
        """holds the minimizing function and the maximizing AI functions"""
        case = board.check_win()
        # check for a win/loss/tie condition
        if case == 'X':
            return 1, None
        if case == 'Y':
            return -1, None
        elif case == 'Tie':
            return 0, None

        # maximizing function
        if maximizing:
            max_eval = -10
            best_move = None
            empty_squares = board.empty()

            # follow each path in the empty squares and find the best position
            for (row, col) in empty_squares:
                print("MAx")
                # make a copy board to tamper with
                temp_board = copy.deepcopy(board)
                temp_board.add_mark((row, col), 'P1')

                # recur with this new board until win condition
                eval = self.minmax(temp_board, False)[0]
                # find a new max eval
                if eval > max_eval:
                    max_eval = eval
                    best_move = (row, col)
            # returns the -1, 1, 0 as the eval code and the move itself
            return max_eval, best_move

        # minimizing function
        elif not maximizing:
            min_eval = 10
            best_move = None
            empty_squares = board.empty()

            # iterates through the empty squares and tries each possible combination
            for (row, col) in empty_squares:
                temp_board = copy.deepcopy(board)
                print(temp_board.print_gameboard())
                temp_board.add_mark((row, col), self.player)

                # recurs with copied board
                eval = self.minmax(temp_board, True)[0]
                # finds the minimum evaluation possible in all recurred pieces
                if eval < min_eval:
                    min_eval = eval
                    best_move = (row, col)
            # returns the eval code and the move of the best move
            return min_eval, best_move

    def eval(self, main_board):
        """evaluation function for AI"""

        # if the level is 0 it means we are working with the random AI
        if self.level == 0:
            eval = 'random'
            move = self.rnd_choice(main_board)
        # otherwise we are working with the other AI
        else:
            # min max
            eval, move = self.minmax(main_board, False)
        print(f'AI: {move}  eval: {eval}')
        return move


# layout prints for directions
print('___________________________________')
print('Welcome To TicTacToe')
print('We all know you know the rules...')
print('___________________________________')
print('Be Wary Commands are Case Sensitive')
print('Here are the commands: ')
print('TL - Top Left Corner')
print('TM - Top Middle')
print('TR - Top Right Corner')
print('ML - Middle Left')
print('MM - Middle Middle')
print('MR - Middle Right')
print('BL - Bottom Left')
print('BM - Bottom Middle')
print('BR - Bottom Right')
# declares what are the moves the user can enter
move_types = ['TL', 'TM', 'TR', 'ML', 'MM', 'MR', 'BL', 'BM', 'BR']
slot_pos = [['TL', 'TM', 'TR'], ['ML', 'MM', 'MR'], ['BL', 'BM', 'BR']]

# actual gameboard that will be played on
gameboard = Board(prev_moves, moves, player)

# prints out a gameboard with the names of each square
display = Board([], slot_pos, None)
display.print_gameboard()

print('___________________________________')
print('Time to start!')
print('___________________________________')

# tracks if there is still a possible game to be played
gameplay = True

while gameplay:
    # to begin type anything and press enter
    print('Type N for a Normal 2 player game')
    print('Type R for a 1 player random game')
    print('Type A for a 1 player AI game')
    style = input('Enter: ')
    while style not in ['A', 'R', 'N']:
        style = input('Please Enter a gameplay style: ')

    # if you typed something it starts

    # Normal 2 Player Game
    if style == 'N':

        # as long as there are valid moves play/no win conditions
        while True:
            print(gameboard.player, "'s Turn")
            move = input('Enter a move: ')

            # if move doesn't exist or has already been made ask the user for another input
            while move not in move_types or move in gameboard.prev:
                move = input('Enter a valid move: ')

            # map user input to a row and column
            position = move_conversion[move]

            # if its player 1 use an X else an O
            gameboard.add_mark(position, gameboard.player)

            # change player
            gameboard.toggle_player()

            # print new board
            gameboard.print_gameboard()

            # check if there are any wins
            wins = gameboard.check_win()

            # if someone wins say who and break out of game
            if wins is not None:
                if wins == 'X':
                    print('P1 Wins')
                elif wins == 'Y':
                    print('P2 Wins')
                elif wins == 'Tie':
                    print('Tie!')
                break

        # ask if user wants a new game of same type
        new_game = input('Want to play again? Y/N: ')
        while new_game not in ['Y', 'N']:
            new_game = input('Want to play again? Y/N: ')

        if new_game == 'Y':
            # if yes reset dependent variables
            # replay the Normal 2 Player Game
            gameboard.reset()
            continue

    # Else if you are playing Random or AI start here
    elif style == 'R' or style == 'A':
        # sets random
        if style == 'R':
            ai = AI(level=0)
        # sets competitive AI
        else:
            ai = AI()

        # while there are still valid moves/no win conditions
        while True:
            # player 1 is human always
            if gameboard.player == 'P1':
                print(gameboard.player, "'s Turn")
                move = input('Enter a move: ')

                # if move doesn't exist or has already been made ask the user for another input
                while move not in move_types and move not in gameboard.prev:
                    move = input('Enter a valid move: ')

                # map user input to a row and column
                row, col = move_conversion[move]
            else:
                # if it's not the player user the AI for an eval
                row, col = ai.eval(gameboard)

            # adds the mark whether it be player or AI
            gameboard.add_mark((row, col), gameboard.player)

            # changes player
            gameboard.toggle_player()

            # print new board
            gameboard.print_gameboard()

            # check if there are any wins
            wins = gameboard.check_win()

            # if someone wins say who and break out of game
            if wins is not None:
                if wins == 'X':
                    print('P1 Wins')
                elif wins == 'Y':
                    print('P2 Wins')
                elif wins == 'Tie':
                    print('Tie!')
                break

        # ask if user wants a new game
        new_game = input('Want to play again? Y/N: ')
        while new_game not in ['Y', 'N']:
            new_game = input('Want to play again? Y/N: ')

        if new_game == 'Y':
            # if yes reset dependent variables and replays the game type
            gameboard.reset()
            continue
    # if the user said no to the new game of same type, ask if they want to play a different type
    diff_game = input('Want to play a different game? Y/N: ')
    while diff_game not in ['Y', 'N']:
        diff_game = input('Want to play a different game? Y/N: ')

    if diff_game == 'Y':
        # if they do want a diff
        gameboard.reset()
        continue

    # exits out of the program
    elif diff_game == 'N':
        gameplay = False
