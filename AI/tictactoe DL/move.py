class Move:
    def __init__(self, coordinate: []):
        self.coordinate = coordinate
        self.games_wined = 0
        self.games_lost = 0
        self.games_tied = 0
        self.avg_game_length = 0

    def __str__(self):
        res = "Move: %s\n\r" \
              "Games: %s; Avg game length %s;\r\n" \
              "Win rate: %s; " \
              "Tie rate: %s; Lose rate: %s" \
              "" % (self.coordinate, self.games_played(), self.avg_game_length,
                    self.win_rate(), self.tie_rate(), self.lose_rate())
        return res

    def in_win(self, num=1, game_length=1):
        if self.avg_game_length != 0:
            self.avg_game_length *= self.games_wined
        self.games_wined += num
        self.avg_game_length = (self.avg_game_length + game_length)/self.games_wined
        return self

    def in_lose(self, num=1):
        self.games_lost += num
        return self

    def in_tie(self, num=1):
        self.games_tied += num
        return self

    def win_rate(self):
        return (self.games_wined/self.games_played()) * 100

    def lose_rate(self):
        return (self.games_lost/self.games_played()) * 100

    def tie_rate(self):
        return (self.games_tied/self.games_played()) * 100

    def games_played(self):
        return self.games_wined + self.games_lost + self.games_tied
