from monopoly.data import tiles_data
class GoToJailTile:
    def visit_jail(self, data, player):
        for i, j in enumerate(data):
            if j["name"] == "Jail":
                player.location = i







