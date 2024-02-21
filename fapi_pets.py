import itertools

# List of items with their types and bonuses
import os

items = [
    # level pets
    # --------------------------------------------------------------
    # row 1
    ("Strawberry", "Ground", ["Potato earned", "Class exp earned", "Skulls earned"]),
    ("Cocorice", "Ground", ["Potato earned"]),
    ("Rico", "Air", ["Class exp earned"]),
    ("Trevor", "Ground", ["Skulls earned"]),
    ("Bingo", "Air", ["Confection exp earned"]),

    # row 2
    ("Vidar", "Ground", ["Potato earned", "Poop created"]),
    ("Primfeet", "Ground", ["Healthy potato", "Reincarnation exp earned"]),
    ("Hiko", "Air", ["Skulls earned", "Milk created"]),
    ("Murphy", "Ground", ["Confection exp earned", "Whack score bonus"]),
    ("Aphrodite", "Air", ["Poop created", "Residue created"]),

    # row 3
    ("Nidhogg", "Air", ["Grasshopper damage", "Item rating bonus"]),
    ("Nuts", "Ground", ["Calcium exp earned", "Item rating bonus"]),
    ("Cid", "Air", ["Whack score bonus", "Worm quantity found"]),
    ("Flash", "Ground", ["Class exp earned", "Brewing exp earned"]),
    ("Tango", "Ground", ["Larva quantity found", "Reincarnation exp earned"]),

    # row 4
    ("Darti", "Air", ["Brewing exp earned", "Larva efficiency bonus"]),
    ("Alvin", "Air", ["Poop created", "Milk created"]),
    ("Johny Be Good", "Ground", ["Larva quantity found", "Larva efficiency bonus"]),
    ("Arizona", "Ground", ["Calcium exp earned", "Residue created", "Protein"]),
    ("Suijin", "Air", ["Fermenting exp earned", "Worm quantity found"]),

    # row 5
    ("Nucifera", "Air", ["Potato earned", "Class exp earned", "Skulls earned"]),
    ("Barney", "Ground", ["Poop created", "Whack score bonus", "Larva quantity found"]),
    ("Seth", "Air", ["Class exp earned", "Confection exp earned", "Fermenting exp earned"]),
    ("Plyne", "Ground", ["Skulls earned", "Calcium exp earned", "Residue created"]),
    ("Zac", "Air", ["Potato earned", "Milk created", "Worm quantity found"]),

    # row 6
    ("Tock", "Ground", ["Class exp earned", "Fermenting exp earned", "Grasshopper damage", "Item rating bonus"]),
    ("The Governess", "Air", ["Poop created", "Brewing exp earned", "Larva quantity found", "Protein"]),
    ("Swamp King", "Ground", ["Skulls earned", "Residue created", "Larva efficiency bonus", "Reincarnation exp earned"]),
    ("Itzamna", "Air", ["Potato earned", "Confection exp earned", "Whack score bonus", "Worm quantity found"]),
    ("Julian", "Ground", ["Fermenting exp earned", "Residue created", "Reincarnation exp earned", "Item rating bonus"]),

    # row 7
    ("Yuhuang", "Air", ["Class exp earned", "Skulls earned", "Milk created", "Brewing exp earned"]),
    ("Wako", "Ground", ["Poop created", "Calcium exp earned", "Fermenting exp earned", "Larva efficiency bonus"]),
    ("Papyru", "Air", ["Whack score bonus", "Residue created", "Larva quantity found", "Card exp"]),
    ("Sigma", "Ground", ["Class exp earned", "Calcium exp earned", "Worm quantity found", "Larva efficiency bonus"]),
    ("Louna", "Air", ["Confection exp earned", "Poop created", "Card power", "Reincarnation exp earned"]),

    # row 8
    ("Babou", "Ground", ["Potato earned", "Milk created", "Fermenting exp earned", "Residue created"]),
    ("Niord", "Air", ["Skulls earned", "Card power", "Card exp", "Item rating bonus"]),
    ("Mous", "Ground", ["Potato earned", "Class exp earned", "Milk created", "Calcium exp earned"]),
    ("Flafy", "Air", ["Skulls earned", "Calcium exp earned", "Fermenting exp earned", "Residue created", "Healthy potato"]),
    ("Nick", "Ground", ["Potato earned", "Brewing exp earned", "Fermenting exp earned", "Worm quantity found", "Card power"]),

    # row 9
    ("Cherry", "Air", ["Class exp earned", "Skulls earned", "Larva quantity found", "Reincarnation exp earned", "Item rating bonus"]),

    # row 10
    ("Neptune", "Ground", ["Reincarnation exp earned", "Card power", "Card exp", "Protein", "Grasshopper damage"]),

    # expedition
    # --------------------------------------------------------------
    ("Serket", "Ground", ["Whack score bonus", "Larva quantity found"]),
    ("Fujin", "Air", ["Potato earned", "Reincarnation exp earned"]),
    ("Ulrich", "Ground", ["Confection exp earned", "Calcium exp earned"]),
    ("Huginn", "Air", ["Skulls earned", "Worm quantity found", "Grasshopper damage"]),
    ("Esus", "Ground", ["Poop created", "Milk created"]),

    ("Hera", "Air", ["Brewing exp earned", "Larva efficiency bonus", "Protein"]),
    ("Asterios", "Ground", ["Class exp earned", "Larva quantity found"]),
    ("Odile", "Air", ["Milk created", "Fermenting exp earned"]),
    ("Froz", "Ground", ["Skulls earned", "Healthy potato"]),
    ("Beelzebub", "Air", ["Confection exp earned", "Grasshopper damage"]),

    ("Anubis", "Ground", ["Confection exp earned", "Brewing exp earned", "Item rating bonus"]),
    ("Garuda", "Air", ["Whack score bonus", "Residue created", "Worm quantity found"]),
    ("Tsukuyomi", "Air", ["Potato earned", "Poop created", "Calcium exp earned"]),
    ("Nanbozo", "Ground", ["Skulls earned", "Brewing exp earned", "Larva quantity found"]),
    ("Ra", "Air", ["Class exp earned", "Fermenting exp earned", "Worm quantity found"]),

    ("Vishnou", "Ground", ["Larva efficiency bonus", "Reincarnation exp earned", "Item rating bonus"]),
    ("Icare", "Air", ["Confection exp earned", "Milk created", "Whack score bonus", "Healthy potato"]),
    ("Olaf", "Ground", ["Fermenting exp earned", "Residue created", "Item rating bonus"]),
    ("Fafnir", "Air", ["Potato earned", "Calcium exp earned", "Larva quantity found"]),
    ("Quetzalcoatl", "Ground", ["Residue created", "Larva efficiency bonus", "Reincarnation exp earned"]),

    ("Nasr", "Air", ["Skulls earned", "Healthy potato", "Grasshopper damage"]),
    ("Bump", "Ground", ["Potato earned", "Healthy potato", "Protein"]),
    ("Professor Inderwind", "Air", ["Brewing exp earned", "Calcium exp earned", "Worm quantity found"]),
    ("Dangun", "Ground", ["Milk created", "Item rating bonus"]),
    ("Abby", "Air", ["Potato earned", "Skulls earned", "Confection exp earned", "Fermenting exp earned"]),

    ("Noop", "Ground", ["Confection exp earned", "Whack score bonus", "Brewing exp earned", "Reincarnation exp earned"]),
    ("Juba", "Ground", ["Class exp earned", "Poop created", "Whack score bonus", "Brewing exp earned", "Grasshopper damage"]),
    ("David", "Air", ["Calcium exp earned", "Residue created", "Card exp"]),
    ("Viktor", "Air", ["Skulls earned", "Milk created", "Worm quantity found", "Item rating bonus"]),
    ("Darko", "Ground", ["Fermenting exp earned", "Residue created", "Card power", "Item rating bonus"]),

    ("Ubel", "Ground", ["Potato earned", "Poop created", "Worm quantity found", "Larva efficiency bonus"]),
    ("Than", "Air", ["Skulls earned", "Whack score bonus", "Larva quantity found", "Card exp"]),
    ("Nyx", "Air", ["Milk created", "Card exp", "Healthy potato", "Protein"]),
    ("Neith", "Ground", ["Card power", "Protein", "Grasshopper damage", "Reincarnation exp earned"]),
    ("Hirma", "Air", ["Confection exp earned", "Poop created", "Milk created", "Brewing exp earned", "Larva efficiency bonus"]),

    # ("Darko", "Ground", ["Fermenting exp earned", "Residue created", "Card power"])
    ("Jack Ballon", "Air", ["Class exp earned", "Skulls earned", "Larva quantity found", "Healthy potato", "Reincarnation exp earned"]),
    ("Zack Cannon", "Ground", ["Potato earned", "Whack score bonus", "Calcium exp earned", "Worm quantity found", "Grasshopper damage"])
]


# Define a function to check if a combination has 19 unique bonuses
def has_19_unique_bonuses(combination):
    unique_bonuses = set()
    air_count = 0
    ground_count = 0

    for item in combination:
        for bonus in item[2]:
            unique_bonuses.add(bonus)
        if item[1] == "Air":
            air_count += 1
        else:
            ground_count += 1
    return len(unique_bonuses) >= 21 and air_count == 3 and ground_count == 3


# Initialize a list to store combinations with 19 unique bonuses
combinations_with_19_bonuses = []

# Generate all combinations of 6 items
combinations = itertools.combinations(items, 6)

for combination in combinations:
    if has_19_unique_bonuses(combination):
        combinations_with_19_bonuses.append(combination)

file = "./res.txt"
if os.path.isfile("./res.txt"):
    os.remove(file)

# Display the combinations with 19 unique bonuses
import json

with open(file, "a") as f:
    for i, combination in enumerate(combinations_with_19_bonuses):
        max_bonus = 0
        for item in combination:
            max_bonus += len(item[2])
        if max_bonus >= 29:
            f.write(f"Combination {i + 1}: \n")
            res = {}
            for item in combination:
                f.write(f"{item[0]} ({item[1]}): {', '.join(item[2])}\n")
            for item in combination:
                print(item[2])
                for bonus in item[2]:
                    if res.get(bonus):
                        res[bonus] += 1
                    else:
                        res[bonus] = 1
            f.write(f"Max Bonus: {max_bonus}\n")
            f.write(f"Bonus: {json.dumps(dict(sorted(res.items())), indent=2)}\n")
            f.write(f"\n")

print(f"Total combinations with 19 unique bonuses: {len(combinations_with_19_bonuses)}")
# 291
