"""
Kingdom dataclass
"""
from dataclasses import dataclass, field

@dataclass
class Kingdom:
    day: int = 0
    treasury: int = 500
    population: int = 100
    happiness: float = 50.0
    grain: int = 300
    wood: int = 100
    iron: int = 500

    pending_consequences: list = field(default_factory=list)

    def __str__(self):
        return (
            f"====================================================\n"
            f"Day: {self.day}\n"
            f"Treasury: {self.treasury}, "
            f"Population: {self.population}, "
            f"Happiness: {self.happiness}\n"
            f"Grain: {self.grain}, "
            f"Wood: {self.wood}, "
            f"Iron: {self.iron}\n"
            f"===================================================="
        )

    def kingdom_state(self):
        return {
        "day": self.day,
        "treasury": self.treasury,
        "population": self.population,
        "happiness": self.happiness,
        "grain":  self.grain,
        "wood": self.wood,
        "iron": self.iron
        }