import random as rn
import copy
import sys

import move as mv
import manager as ma
import hyperparameter as hp


def sort_moves(moves: [mv.Move]):
    def sort_func(e):
        return -e.win_rate(), -e.avg_game_length

    return sorted(moves, key=sort_func)


class Player:

    def __init__(self, name):
        self.name = name
        self.team = None
        self.game_moves = []
        self.knowledge = {}
        self.num_of_ties = 0
        self.num_of_wins = 0
        self.num_of_loses = 0
        self.hyper_parameters = {"minimum_win_rate_tolerance": hp.HyperParameter("minimum_win_rate_tolerance",
                                                                                 value=80,
                                                                                 start=0,
                                                                                 stop=100,
                                                                                 step=0.001,
                                                                                 update_rate=50,
                                                                                 chart=True),
                                 "start_hyping_value": hp.HyperParameter("start_hyping_value",
                                                                         value=80,
                                                                         start=0,
                                                                         stop=9999999,
                                                                         step=1),
                                 "slope_past_value": hp.HyperParameter("slope_past_value",
                                                                       value=5,
                                                                       start=1,
                                                                       stop=999999,
                                                                       step=1),
                                 "random_moves_index": hp.HyperParameter("random_moves_index",
                                                                         value=20,
                                                                         start=0,
                                                                         stop=100,
                                                                         step=0.001,
                                                                         chart=True),
                                 "minimum_good_moves_rate": hp.HyperParameter("minimum_good_moves_rate",
                                                                              value=40,
                                                                              start=0,
                                                                              stop=100,
                                                                              step=0.001,
                                                                              chart=False)
                                 }
        self.practice_stats = None
        self.reset_practice_stats()

    def __str__(self):
        total_games = self.num_of_ties + self.num_of_wins + self.num_of_loses
        res = "name: " + self.name + "\r\n" \
              + "games: " + str(total_games) + "\r\n" \
              + "wins: " + str(self.num_of_wins) + "\r\n" \
              + "winning rate: "
        if total_games != 0:
            res += str(float((self.num_of_wins / total_games)) * 100) + "\r\n"
        else:
            res += "0 \r\n"

        return res

    def won_game(self):
        self.num_of_wins += 1
        self.practice_stats["num_of_win_games"] += 1
        temp = {
            "result": 1,
            "smart_moves_rate": self.game_smart_moves_rate()
        }
        self.practice_stats["last_100_games"].append(temp)
        self.practice_stats["game_smart_moves"] = 0
        self.practice_stats["game_dumb_moves"] = 0
        if len(self.practice_stats["last_100_games"]) > 100:
            self.practice_stats["last_100_games"].pop(0)

    def lost_game(self):
        self.num_of_loses += 1
        self.practice_stats["num_of_lose_games"] += 1
        temp = {
            "result": 2,
            "smart_moves_rate": self.game_smart_moves_rate()
        }
        self.practice_stats["last_100_games"].append(temp)
        self.practice_stats["game_smart_moves"] = 0
        self.practice_stats["game_dumb_moves"] = 0
        if len(self.practice_stats["last_100_games"]) > 100:
            self.practice_stats["last_100_games"].pop(0)

    def tie_game(self):
        self.num_of_ties += 1
        self.practice_stats["num_of_tie_games"] += 1
        temp = {
            "result": 0,
            "smart_moves_rate": self.game_smart_moves_rate()
        }
        self.practice_stats["last_100_games"].append(temp)
        self.practice_stats["game_smart_moves"] = 0
        self.practice_stats["game_dumb_moves"] = 0
        if len(self.practice_stats["last_100_games"]) > 100:
            self.practice_stats["last_100_games"].pop(0)

    def print_moves(self):
        res = "winning moves:\r\n"
        for board in self.knowledge:
            res += "moves for: " + board + "\r\n"
            for move in sort_moves(self.knowledge[board].values()):
                res += str(move) + "\r\n"
            res += "\r\n"
        return res

    def print_hyper_parameters(self):
        res = "Hyper parameters:\r\n"
        for parameter in self.hyper_parameters.values():
            res += str(parameter.to_str())
        return res

    def save_self(self):

        return ma.save_data("players\\%s_mind.txt" % self.name, self)

    def make_action(self, game, moves_not_to_do=None):

        moves_options = game.get_game_options()
        if moves_not_to_do:
            temp = copy.deepcopy(game.get_game_options())
            for x in moves_not_to_do:
                temp.remove(x)
            if temp:
                moves_options = temp

        if not moves_options:
            x = 2

        board = game.board
        option_num = rn.choice(range(len(moves_options)))
        option = moves_options[option_num]
        action = {
            "board": copy.deepcopy(board),
            "move": option
        }
        game.mark_place(action["move"], self.team)
        self.practice_stats["game_dumb_moves"] += 1
        print(self.name + " made a dumb move")

        self.game_moves.append(copy.deepcopy(action))
        return action

    def make_smart_action_vs_human(self, game):
        board = game.board
        best_moves = []
        if self.knowledge.get(str(board)):
            def sort_func(e):
                return -e.win_rate()

            curn_situation = copy.deepcopy(sorted(self.knowledge.get(str(board)).values(), key=sort_func))

            # choose the move
            # if none are good
            if curn_situation[0].win_rate() < self.hyper_parameters["minimum_win_rate_tolerance"].get_value():
                # try to get a tie
                for x in curn_situation:
                    if x.tie_rate() != 0:
                        best_moves.append(x)

                if best_moves:
                    def sort_func(e):
                        return -e.tie_rate()

                    best_moves.sort(key=sort_func)
                else:
                    moves_not_to_do = [x.coordinate for x in curn_situation]
                    action = self.make_action(game, moves_not_to_do)
                    return action

            else:

                # if one is the best
                if curn_situation[0].win_rate() == 100:

                    for move in curn_situation:
                        if move.win_rate() == 100:
                            best_moves.append(move)

                # normal event
                else:

                    for move in curn_situation:
                        if move.win_rate() >= self.hyper_parameters["minimum_win_rate_tolerance"].get_value():
                            best_moves.append(move)

                def sort_func(e):
                    return e.avg_game_length

                best_moves.sort(key=sort_func)

                # find best move

            row = best_moves[0].coordinate[0]
            col = best_moves[0].coordinate[1]

            # make the move

            action = {
                "board": copy.deepcopy(board),
                "move": [row, col]
            }
            game.mark_place(action["move"], self.team)
            self.game_moves.append(copy.deepcopy(action))
            self.practice_stats["game_smart_moves"] += 1
            print(self.name + " made a smart move")
        else:
            action = self.make_action(game)

        return action

    def make_smart_action(self, game):

        if self.get_total_practice_games() > 0:
            if rn.choice(list(range(1, 100))) < self.hyper_parameters["random_moves_index"].get_value():
                return self.make_action(game)

        board = game.board
        if self.knowledge.get(str(board)):
            def sort_func(e):
                return -e.win_rate()

            curn_situation = copy.deepcopy(sorted(self.knowledge.get(str(board)).values(), key=sort_func))

            # choose the move

            # if none are good
            if curn_situation[0].win_rate() < self.hyper_parameters["minimum_win_rate_tolerance"].get_value():
                moves_not_to_do = [x.coordinate for x in curn_situation]
                action = self.make_action(game, moves_not_to_do)
                return action

            else:

                # if one is the best
                if curn_situation[0].win_rate() == 100:
                    best_moves = []
                    for move in curn_situation:
                        if move.win_rate() == 100:
                            best_moves.append(move)

                # normal event
                else:
                    best_moves = []
                    for move in curn_situation:
                        if move.win_rate() >= self.hyper_parameters["minimum_win_rate_tolerance"].get_value():
                            best_moves.append(move)

                # find best move
                def sort_func(e):
                    return e.avg_game_length

                best_moves.sort(key=sort_func)
                row = best_moves[0].coordinate[0]
                col = best_moves[0].coordinate[1]

            # temp_compromise = self.hyper_parameters["compromise_value"].get_value()
            #     temp_moves = []
            #     for move in curn_situation:
            #         if move.win_rate() >= (100 - temp_compromise):
            #             temp_moves.append(move)
            #
            #     if not temp_moves:
            #         if curn_situation[0].win_rate() >= self.hyper_parameters["minimum_win_rate_tolerance"].get_value():
            #             row = curn_situation[0].coordinate[0]
            #             col = curn_situation[0].coordinate[1]
            #         else:
            #             return self.make_action(game, moves_not_to_do=[x.coordinate for x in curn_situation])
            #     else:
            #         def sort_func(e):
            #             return e.avg_game_length
            #
            #         temp_moves.sort(key=sort_func, reverse=False)
            #         row = temp_moves[0].coordinate[0]
            #         col = temp_moves[0].coordinate[1]

            # make the move

            action = {
                "board": copy.deepcopy(board),
                "move": [row, col]
            }
            game.mark_place(action["move"], self.team)
            self.game_moves.append(copy.deepcopy(action))
            self.practice_stats["game_smart_moves"] += 1
            print(self.name + " made a smart move")
        else:
            action = self.make_action(game)

        return action

    def learn_game(self, good_moves=None, bad_moves=None, tie_moves=None):
        if tie_moves is None:
            tie_moves = []
        if bad_moves is None:
            bad_moves = []
        if good_moves is None:
            good_moves = []
        total_moves = len(good_moves) + len(bad_moves) + len(tie_moves)
        count = 1
        for action in good_moves:
            if str(action["board"]) in self.knowledge:
                if str(action["move"]) in self.knowledge[str(action["board"])]:
                    self.knowledge.get(str(action["board"])).get(str(action["move"])).in_win(
                        game_length=(len(good_moves) + len(bad_moves)))
                else:
                    self.knowledge[str(action["board"])][str(action["move"])] = mv.Move(action["move"]).in_win(
                        game_length=(len(good_moves) + len(bad_moves)))
            else:
                self.knowledge[str(action["board"])] = {}
                self.knowledge[str(action["board"])][str(action["move"])] = mv.Move(action["move"]).in_win(
                    game_length=(len(good_moves) + len(bad_moves)))
            count += 1

        for action in bad_moves:
            if str(action["board"]) in self.knowledge:
                if str(action["move"]) in self.knowledge[str(action["board"])]:
                    self.knowledge.get(str(action["board"])).get(str(action["move"])).in_lose()
                else:
                    self.knowledge[str(action["board"])][str(action["move"])] = mv.Move(action["move"]).in_lose()
            else:
                self.knowledge[str(action["board"])] = {}
                self.knowledge[str(action["board"])][str(action["move"])] = mv.Move(action["move"]).in_lose()
            count += 1

        for action in tie_moves:
            if str(action["board"]) in self.knowledge:
                if str(action["move"]) in self.knowledge[str(action["board"])]:
                    self.knowledge.get(str(action["board"])).get(str(action["move"])).in_tie()
                else:
                    self.knowledge[str(action["board"])][str(action["move"])] = mv.Move(action["move"]).in_tie()
            else:
                self.knowledge[str(action["board"])] = {}
                self.knowledge[str(action["board"])][str(action["move"])] = mv.Move(action["move"]).in_tie()
            count += 1

        self.optimize_hyper_parameters()

        return self.save_self()

    def optimize_hyper_parameters(self):

        if self.get_total_practice_games() > self.hyper_parameters["start_hyping_value"].get_value():
            win_rate = self.practice_stats["win_rate"]
            smart_moves = self.practice_stats["smart_moves"]
            knowledge_size = self.practice_stats["knowledge_size"]
            temp_slope_value = int(-self.hyper_parameters["slope_past_value"].get_value())

            move_count = 0
            good_moves_rate = 0

            for x in self.knowledge.values():
                for move in x.values():
                    move_count += 1
                    if move.win_rate() >= self.hyper_parameters["minimum_win_rate_tolerance"].get_value():
                        good_moves_rate += 1

            good_moves_rate /= move_count
            good_moves_rate *= 100

            smart_moves_slope = 0
            win_slope = 0
            for x in range(temp_slope_value, -2, 2):
                smart_moves_slope += (smart_moves[x + 1] - smart_moves[x]) / 2
                win_slope += (win_rate[x + 1] - win_rate[x]) / 2

            smart_moves_slope /= len(range(temp_slope_value, -2, 2))
            win_slope /= len(range(temp_slope_value, -2, 2))

            if win_slope < 0 or good_moves_rate > self.hyper_parameters["minimum_good_moves_rate"].get_value():
                self.hyper_parameters["minimum_win_rate_tolerance"].increase()
            else:
                self.hyper_parameters["minimum_win_rate_tolerance"].decrease()

            if smart_moves_slope <= 0:
                pass
            else:
                pass

    def practice_l1g_win_rate(self):
        win = 0
        lose = 0
        tie = 0
        for x in self.practice_stats["last_100_games"]:
            if x["result"] == 1:
                win += 1
            elif x["result"] == 2:
                lose += 1
            elif x["result"] == 0:
                tie += 1
        return (win / (win + tie + lose)) * 100

    def practice_l1g_lose_rate(self):
        win = 0
        lose = 0
        tie = 0
        for x in self.practice_stats["last_100_games"]:
            if x["result"] == 1:
                win += 1
            elif x["result"] == 2:
                lose += 1
            elif x["result"] == 0:
                tie += 1
        return (lose / (win + tie + lose)) * 100

    def practice_l1g_tie_rate(self):
        win = 0
        lose = 0
        tie = 0
        for x in self.practice_stats["last_100_games"]:
            if x["result"] == 1:
                win += 1
            elif x["result"] == 2:
                lose += 1
            elif x["result"] == 0:
                tie += 1
        return (tie / (win + tie + lose)) * 100

    def get_total_practice_games(self):
        return self.practice_stats["num_of_win_games"] + \
               self.practice_stats["num_of_lose_games"] + \
               self.practice_stats["num_of_tie_games"]

    def game_smart_moves_rate(self):
        return (self.practice_stats["game_smart_moves"] / (
                self.practice_stats["game_dumb_moves"] + self.practice_stats["game_smart_moves"])) * 100

    def practice_l1g_smart_moves(self):
        avg = 0
        count = len(self.practice_stats["last_100_games"])
        for x in self.practice_stats["last_100_games"]:
            avg += x["smart_moves_rate"]
        return avg / count

    def reset_practice_stats(self):
        self.practice_stats = {"game_smart_moves": 0,
                               "game_dumb_moves": 0,
                               "num_of_win_games": 0,
                               "num_of_lose_games": 0,
                               "num_of_tie_games": 0,
                               "win_rate": [0],
                               "last_100_games": [{"result": 0, "smart_moves_rate": 0.0}],
                               "smart_moves": [0],
                               "knowledge_size": [sys.getsizeof(self.knowledge)]
                               }
        self.practice_stats.update({hyper.name: [hyper.get_value()] for hyper in
                                    self.hyper_parameters.values()})

    def set_hyper_parameters(self):
        print("Set hyper parameters for {0}, 'n' to keep last value:\r\n".format(self.name))

        for hyperparameter in self.hyper_parameters.values():
            while True:
                user_input = input("Edit " + hyperparameter.name + "?[y/n]")
                if user_input == "y":
                    hyperparameter.set_parameter()
                    break
                elif user_input == "n":
                    break
        while True:
            if self.hyper_parameters["slope_past_value"].get_value() > self.hyper_parameters[
                "start_hyping_value"].get_value():
                print("Problem!, slope_past_value > start_hyping_value"
                      "\r\nchange that!")
                self.hyper_parameters["slope_past_value"].set_parameter()
                self.hyper_parameters["start_hyping_value"].set_parameter()
            else:
                break
