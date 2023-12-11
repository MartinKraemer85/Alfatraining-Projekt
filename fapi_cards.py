from dataclasses import dataclass
from enum import Enum
import itertools


class CardName(Enum):
    attack_hp = 1
    potato = 2
    class_exp = 3
    skull = 4
    whack = 5
    poop = 6
    confection = 7
    worm = 8
    larvaq = 9
    larvae = 10
    milk = 11
    brew = 12
    calcium = 13
    fergementing = 14
    residue = 15
    items = 16
    reincarnation = 17
    pet_level = 18
    pet_damage = 19
    pet_rank = 20


@dataclass()
class Expedition:
    exp_name: str
    cards_found: list[CardName]


@dataclass()
class ExpeditionCombination:
    expedition_names: list[str]
    card_list: list[CardName]

    def _join_names(self):
        return ', '.join(self.expedition_names)

    def _join_cards(self):
        return ', '.join([card.name for card in self.card_list])

    def print(self):
        print(f"Expeditions: {self._join_names()} \n\r Cards found: {self._join_cards()} \n\r Cards amount: {self.card_length()}")

    def card_length(self):
        return len(self.card_list)


expeditions = [Expedition(exp_name="butternut forest", cards_found=[CardName.attack_hp, CardName.potato, CardName.residue]),
               Expedition(exp_name="cheddar plain", cards_found=[CardName.class_exp, CardName.worm, CardName.whack]),
               Expedition(exp_name="Guacamole", cards_found=[CardName.skull, CardName.pet_damage, CardName.brew]),
               Expedition(exp_name="Orange Mountain", cards_found=[CardName.larvaq, CardName.pet_level, CardName.calcium]),
               Expedition(exp_name="Avocado", cards_found=[CardName.poop, CardName.milk, CardName.confection]),
               Expedition(exp_name="Zucchini", cards_found=[CardName.reincarnation, CardName.larvae, CardName.fergementing]),
               Expedition(exp_name="Munster", cards_found=[CardName.worm, CardName.class_exp, CardName.potato]),
               Expedition(exp_name="Pancake", cards_found=[CardName.attack_hp, CardName.milk, CardName.pet_damage]),
               Expedition(exp_name="Salmon", cards_found=[CardName.skull, CardName.brew, CardName.confection]),
               Expedition(exp_name="Garlic", cards_found=[CardName.pet_level, CardName.calcium, CardName.whack]),
               Expedition(exp_name="Banana", cards_found=[CardName.poop, CardName.attack_hp, CardName.potato]),
               Expedition(exp_name="Cinnamon", cards_found=[CardName.items, CardName.fergementing, CardName.larvae]),
               Expedition(exp_name="Apple", cards_found=[CardName.confection, CardName.pet_rank, CardName.residue]),
               Expedition(exp_name="Donut", cards_found=[CardName.larvae, CardName.calcium, CardName.reincarnation]),
               ]


def combine(expeditions, cxp_count=7):
    return itertools.combinations(expeditions, cxp_count)


combinations = combine(expeditions)
expeditionCombination = []
for combination in combinations:
    card_list = []
    expedition_names = []

    for expedition in combination:
        card_list += expedition.cards_found
        expedition_names.append(expedition.exp_name)
    card_list = list(set(card_list))
    expeditionCombination.append(ExpeditionCombination(expedition_names=expedition_names, card_list=card_list))


best_combination = ExpeditionCombination([], [])
for combination in expeditionCombination:
    best_combination = combination if combination.card_length() > best_combination.card_length() else best_combination

best_combination.print()
