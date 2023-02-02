import glob
import os
import pickle
# import keyboard
import matplotlib.pyplot as plt
import game as gm
import player as pl
from sys import getsizeof
import sys


def save_data(filename, data):
    try:
        file = open(filename, "wb")
        pickle.dump(data, file)
        file.close()
        return True
    except Exception as err:
        print(err.args)
        return False


def load_data(filename):
    res = []
    try:
        open_file = open(filename, "rb")
        res = pickle.load(open_file)
        open_file.close()
        return res
    except Exception as err:
        print(err.args)
        return "error"


def entry_validation(quote, validation: list):
    while True:
        user_input = input(quote)
        if user_input in validation:
            return user_input
        else:
            print("Invalid entry, try again")


def bar_plot(data, title="bar_plot", xlabel="x-axis", ylabel="y-axis"):
    left = []
    height = []
    tick_label = []
    legends = []
    colors = []
    count = 1
    for player in data:
        color = data[player]["color"]
        del data[player]["color"]
        legends.append(player)
        for i in data[player]:
            left.append(count)
            colors.append(color)
            height.append(int(data[player][i]))
            tick_label.append(i)
            count += 1

    plt.bar(left, height, tick_label=tick_label,
            width=0.8, color=colors)

    plt.legend(legends)
    # naming the x-axis
    plt.xlabel(xlabel)
    # naming the y-axis
    plt.ylabel(ylabel)
    # plot title
    plt.title(title)

    # function to show the plot
    plt.show()


def clear():
    # for windows the name is 'nt'
    if os.name == 'nt':
        _ = os.system('cls')

    # and for mac and linux, the os.name is 'posix'
    else:
        _ = os.system('clear')


def chart_plot(data):
    x = data.pop("games")
    for chart in data:
        plt.title(chart + " chart after " + str(x[-1]) + " games")
        plt.xlabel("Games")
        for player in data[chart]:
            y = data[chart][player]
            plt.plot(x, y, label=player)
        plt.legend()
        plt.show()


class Manager:

    def __init__(self, player1):
        self.player1 = player1

    def manage(self):
        while True:
            print("\r\nNow managing: " + self.player1.name)
            user_input = entry_validation("""1)train player
2)play against player
3)show player stats
4)Save player
5)Delete player
6)Quit player
answer: """, ["1", "2", "3", "4", "5", "6"])

            if user_input == "1":
                self.train_player()
            elif user_input == "2":
                name = input("name:")
                human = pl.Player(name)
                human_game = gm.Game(self.player1, human)
                human_game.play_human()
            elif user_input == "3":
                print(self.player1)
                if entry_validation("Print moves?[y/n]", ["y", "n"]) == "y":
                    print(self.player1.print_moves())
                if entry_validation("Print hyper parameters?[y/n]", ["y", "n"]) == "y":
                    print(self.player1.print_hyper_parameters())
            elif user_input == "4":
                try:
                    self.player1.save_self()
                except:
                    print("Cant save player")
                else:
                    print("Player saved")
            elif user_input == "5":
                if entry_validation("do you want to delete {0}?[y/n]".format(self.player1.name), ["y", "n"]) == "y":
                    os.remove("players\\{0}_mind.txt".format(self.player1.name))
                    break
            elif user_input == "6":
                if entry_validation("do you want to quit?[y/n]", ["y", "n"]) == 'y':
                    self.player1.save_self()
                    break

    def train_player(self):
        # Cycles
        cycles = input("how much cycles do you want to train your player?")

        # player to play against
        print("Choose player to train against:")
        players_names = [f.replace("players\\", "").replace("_mind.txt", "") for f in glob.glob("players\\*_mind.txt")]
        count = 2
        print("1)Random player(dumb)")
        for i in players_names:
            print(str(count) + ")" + i)
            count += 1

        user_choice = entry_validation("Choose player number: ", [str(x + 1) for x in list(range(count - 1))])

        if int(user_choice) == 1:
            player2 = pl.Player("Random player")
        else:
            player2 = load_data("players\\%s_mind.txt" % players_names[int(user_choice) - 2])
            if player2.name == self.player1.name:
                player2.name = player2.name+"(2)"

        # kind of moves
        kind_of_moves = entry_validation("what kind of train?[smart/dumb]", ["smart", "dumb"])

        if entry_validation("Change hyperparameters?[y/n]:", ['y', 'n']) == 'y':
            self.player1.set_hyper_parameters()

        self.player1.reset_practice_stats()
        player2.reset_practice_stats()

        # training
        for i in range(int(cycles)):
            clear()
            good_moves = []
            bad_moves = []
            tie_moves = []
            print("Now playing " + str(i + 1) + " game out of " + str(cycles) + " games")
            game = gm.Game(self.player1, player2)
            winner = game.play_game(kind_of_moves)
            del game
            if isinstance(winner, pl.Player):
                good_moves = winner.game_moves
                if winner is self.player1:
                    self.player1.won_game()
                    player2.lost_game()
                    bad_moves = player2.game_moves
                else:
                    self.player1.lost_game()
                    player2.won_game()
                    bad_moves = self.player1.game_moves
            else:
                tie_moves = self.player1.game_moves + player2.game_moves
                self.player1.tie_game()
                player2.tie_game()

            # data for practice chart
            for player in [self.player1, player2]:
                player.practice_stats["win_rate"].append(player.practice_l1g_win_rate())
                player.practice_stats["smart_moves"].append(player.practice_l1g_smart_moves())
                player.practice_stats["knowledge_size"].append(sys.getsizeof(player.knowledge))
                for x in player.hyper_parameters.values():
                    if x.make_chart():
                        player.practice_stats[x.name].append(x.get_value())

            self.player1.game_moves = []
            player2.game_moves = []
            if not self.player1.learn_game(good_moves, bad_moves, tie_moves):
                if entry_validation("Cant save player, quit training?[y/n]", ["y", "n"]) == "y":
                    break

            if int(user_choice) != 1:
                player2.learn_game(good_moves, bad_moves, tie_moves)
                if player2.name == self.player1.name+"(2)":
                    os.remove("players\\{0}_mind.txt".format(player2.name))

            # or (keyboard.is_pressed("left ctrl") and keyboard.is_pressed("d"))
            if (i + 1) % (int(cycles) / 4) < 1:

                # wins plot
                data = {
                    self.player1.name: {
                        "wins rate": self.player1.practice_l1g_win_rate(),
                        "lose rate": 100 - self.player1.practice_l1g_win_rate() - self.player1.practice_l1g_tie_rate(),
                        "tie rate": self.player1.practice_l1g_tie_rate(),
                        "color": "blue"
                    }
                }
                bar_plot(data, title="after {0} games rate".format(i + 1), xlabel="players", ylabel="percentage")

                chart_data = {}
                for player in [self.player1, player2]:
                    for x in player.practice_stats:
                        if x == "last_100_games":
                            continue
                        if isinstance(player.practice_stats[x], list):
                            if "games" not in chart_data.keys():
                                chart_data["games"] = [y for y in range(len(player.practice_stats[x]))]
                            if len(player.practice_stats[x]) != len(chart_data["games"]):
                                continue
                            if x not in chart_data.keys():
                                chart_data[x] = {}
                            chart_data[x][player.name] = player.practice_stats[x]

                chart_plot(chart_data)

            # if keyboard.is_pressed("left ctrl") and keyboard.is_pressed("q"):
            #     if entry_validation("Quit training?[y/n]", ["y", "n"]) == "y":
            #         break
            #
            # if keyboard.is_pressed("left ctrl") and keyboard.is_pressed("h"):
            #     if entry_validation("Edit hyper parameters?[y/n]", ["y", "n"]) == "y":
            #         if entry_validation("Choose player:\r\n1){0}\r\n2){1}\r\nanswer: "
            #                             .format(self.player1.name, player2.name), ["1", "2"]) == "1":
            #             self.player1.set_hyper_parameters()
            #         else:
            #             player2.set_hyper_parameters()
        self.manage()
