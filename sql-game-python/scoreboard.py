class Scoreboard:
    def __init__(self) -> None:
        self.level = 1
        self.score = 20

    def reset(self):
        self.score = 20
        self.level = 1

    def level_up(self):
        self.level += 1
        self.score += 100

    def wrong_answer(self):
        self.score -= 20

    def asked_hint(self):
        self.score -= 10