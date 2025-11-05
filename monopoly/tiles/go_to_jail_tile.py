from monopoly.data import tiles_data
class GoToJailTile:
    def __init__(self, location):
        self.location = location

    def visit_jail(self, data):
        if data[self.location]["name"] == "Go To Jail":
            for i, j in enumerate(data):
                if j["name"] == "Jail":
                    self.location = i







