from elfy.rucksack import Rucksack, get_item_priority
from elfy.elf import Elf, ElvenGroup

rucksacks = []
elves = []
total_priorities = 0
for line in open("input.txt", "r"):
    rucksacks.append(Rucksack(line))
    total_priorities = total_priorities + get_item_priority(rucksacks[-1].find_compartment_similarity())
    elves.append(Elf(rucksack=rucksacks[-1]))

print(total_priorities)

identification_total = 0
for pos in range(0, len(rucksacks), 3):
    elven_group = ElvenGroup(elves[pos:pos + 3])
    group_id = elven_group.find_identification_badge()

    identification_total = identification_total + get_item_priority(group_id)

print(identification_total)
