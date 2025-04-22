class User:

    def __init__(self,name, wins,losses):
        self.name = name
        self.losses = losses
        self.wins = wins

    def to_dict(self):
        return {'name': self.name, 'wins': self.wins, 'losses': self.losses}

    @classmethod
    def from_dict(cls, d):
        return cls(
            d.get('name', ''),
            d.get('wins', 0),
            d.get('losses', 0)
        )

    def IncrementLosses(self):
        self.losses = self.losses + 1

    def IncrementWins(self):
        self.wins = self.wins + 1