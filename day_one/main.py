from elfy.elf import Elf
current_calories = []
elves = []
for line in open("input.txt", "r"):
    if line != '\n':
        current_calories.append(int(line))
    else:
        elves.append(Elf(current_calories))
        current_calories = []

sorted_elves = sorted(elves, key=lambda x: x.get_calories_total(), reverse=True)

print(sorted_elves[0].get_calories_total())
print(sum([i.get_calories_total() for i in sorted_elves[:3]]))