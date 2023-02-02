import player as pl
import manager as ma
import glob


if __name__ == '__main__':

    while True:
        while True:
            ma.clear()
            user_input = ma.entry_validation("1)Create new player \r\n2)Use existing player \r\n answer: ", ["1", "2"])
            if user_input == "1":
                while True:
                    name = input("Player name: ")
                    player = pl.Player(name)
                    if ma.load_data("players\\%s_mind.txt" % player.name) == "error":
                        if input("Set hyper parameters or use default?[s/d]") == "s":
                            player.set_hyper_parameters()
                        ma.save_data("players\\%s_mind.txt" % player.name, player)
                        break
                    else:
                        print("Name already taken :(")
                break
            elif user_input == "2":
                print("\r\nChoose player:")
                players_names = [f.replace("players\\", "").replace("_mind.txt", "") for f in glob.glob("players\\*_mind.txt")]
                count = 1
                for i in players_names:
                    print(str(count) + ")" + i)
                    count += 1
                while True:
                    user_choice = input("Choose player number: ")
                    if int(user_choice) <= count:
                        player = ma.load_data("players\\{0}_mind.txt".format(players_names[int(user_choice)-1]))
                        if player == "error":
                            print("cant load player")
                            continue
                        break
                    else:
                        print("Invalid entry")
                break
        manager = ma.Manager(player)
        manager.manage()
