

class Player:

    def __innit__(self, ip, name) -> None:
        self.ip = ip
        self.name = name
        self.score = 0
    
    def __eq__(self, other) -> bool:
        return (isinstance(other, Player)
                and self.ip == other.ip
                and self.name == other.name)
    
    def update_score(self, score):
        """
        Update the score by the score obtained from a round
        """
        self.score += score