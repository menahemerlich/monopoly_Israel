from abc import ABC, abstractmethod

class TaxTile(ABC):
    @abstractmethod
    def tax(self, player, location):
        player.money -= location["amount"]





