
class Board:
    def __init__(self, tiles_data: list[dict]):
        self.tiles_data = tiles_data

    def movement(self, player, dice):
        if (player.location + dice) > len(self.tiles_data):
            player.location = dice - (len(self.tiles_data) - player.location)
            print("Moving the Start slot.")
            player.money += 200







