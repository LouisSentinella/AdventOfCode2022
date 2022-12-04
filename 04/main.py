from elfy.elf import Elf, ElvenGroup

elven_groups = []
redundant_cleaning_count = 0

for line in open("input.txt", "r"):
    one_range, two_range = line.split(',')

    elf_one = Elf()
    elf_two = Elf()
    elf_one.assign_cleaning(*[int(i) for i in one_range.split('-')])
    elf_two.assign_cleaning(*[int(i) for i in two_range.split('-')])

    elven_groups.append(ElvenGroup([elf_one, elf_two]))
    redundant_cleaning_count += elven_groups[-1].find_redundant_cleaning()

print(redundant_cleaning_count)

overlap_count = 0

for elven_group in elven_groups:
    overlap_count += elven_group.identify_cleaning_overlap()

print(overlap_count)