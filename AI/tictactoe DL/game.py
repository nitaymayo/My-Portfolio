import move as mv
import random as rn
import manager as ma


class Game:

    def __init__(self, player1, player2):
        self.blue = player1
        self.red = player2
        self.empty_space = "*"
        self.board = [[self.empty_space for i in range(3)] for j in range(3)]
        self.__options = [[i, j] for i in range(3) for j in range(3)]

    def __str__(self):
        res = "\r\n"
        res += str(self.board[0][0]) + "|" + str(self.board[0][1]) + "|" + str(self.board[0][2]) + "\r\n" + \
               str(self.board[1][0]) + "|" + str(self.board[1][1]) + "|" + str(self.board[1][2]) + "\r\n" + \
               str(self.board[2][0]) + "|" + str(self.board[2][1]) + "|" + str(self.board[2][2]) + "\r\n"
        return res

    def check_board(self, player):
        c = player.team

        if self.blue.team == c:
            opo = self.red.team
        else:
            opo = self.blue.team

        # check row
        for i in self.board:
            if i.__contains__(self.empty_space):
                continue
            if i.__contains__(opo):
                continue
            return "1"

        # check column
        for i in range(3):
            if self.board[0][i] == c:
                if self.board[1][i] == c:
                    if self.board[2][i] == c:
                        return "1"

        # check diagonal
        if self.board[1][1] == c:
            if self.board[0][0] == c:
                if self.board[2][2] == c:
                    return "1"
            if self.board[0][2] == c:
                if self.board[2][0] == c:
                    return "1"

        if not self.board[0].__contains__(self.empty_space):
            if not self.board[1].__contains__(self.empty_space):
                if not self.board[2].__contains__(self.empty_space):
                    return "2"

        return "0"

    def play_human(self):
        print(self)
        if rn.choice((0, 1)) == 0:
            turn = self.blue
            self.blue.team = "O"
            self.red.team = "X"
        else:
            turn = self.red
            self.red.team = "O"
            self.blue.team = "X"
        res = "0"
        while res == "0":
            if turn is self.red:
                turn = self.blue
                turn.make_smart_action_vs_human(self)
            else:
                turn = self.red
                while True:
                    row = int(ma.entry_validation("row: ", ["0", "1", "2"]))
                    col = int(ma.entry_validation("col: ", ["0", "1", "2"]))

                    if [row, col] in self.__options:
                        self.mark_place(coordinate=[row, col], mark=turn.team)
                        self.red.game_moves.append(mv.Move([row, col]))
                        break
                    else:
                        print("cant do that")

            print(self)

            res = self.check_board(turn)

        if res == "1":
            print(turn.name + " won!!")
            return turn
        elif res == "2":
            print("its a tie")
            return "tie"
        else:
            print("something went wrong :(")
            return "error"

    def play_game(self, kind_of_moves):
        if rn.choice((0, 1)) == 0:
            turn = self.blue
            self.blue.team = "X"
            self.red.team = "O"
        else:
            turn = self.red
            self.red.team = "X"
            self.blue.team = "O"
        count = 1
        while True:
            if kind_of_moves == "smart":
                turn.make_smart_action(self)
            else:
                turn.make_action(self)
            if count >= 5:
                res = self.check_board(turn)
                if res != "0":
                    break

            if turn is self.red:
                turn = self.blue
            else:
                turn = self.red
            count += 1

        if res == "1":
            print(turn.name + " won!!")
            return turn
        elif res == "2":
            print("its a tie")
            return "tie"
        else:
            print("something went wrong :(")
            return "error"

    def mark_place(self, coordinate: [], mark: ""):
        self.board[coordinate[0]][coordinate[1]] = mark
        self.__options.remove(coordinate)

    def get_game_options(self):
        return self.__options
