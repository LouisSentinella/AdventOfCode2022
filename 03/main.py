from elfy.rucksack import get_item_priority
from elfy.elf import Elf, ElvenGroup

elves = []
total_priorities = 0
for line in open("input.txt", "r"):
    elves.append(Elf())
    elves[-1].pack_rucksack(rucksack_contents=line)
    total_priorities = total_priorities + get_item_priority(elves[-1].get_rucksack().find_compartment_similarity())

print(total_priorities)

identification_total = 0
for pos in range(0, len(elves), 3):
    elven_group = ElvenGroup(elves[pos:pos + 3])
    group_id = elven_group.find_identification_badge()

    identification_total = identification_total + get_item_priority(group_id)

print(identification_total)
