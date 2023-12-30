import os
import random
import ast
import file_operations
from faker import Faker


def replace_letters_in_skillnames_to_runic():
    with open("letters_mapping.txt") as file:
        data = file.read()
    letters_mapping = ast.literal_eval(data)
    with open("skills.txt", 'r') as file:
        list_of_skills = file.readlines()
        for index in range(len(list_of_skills)):
            for key in letters_mapping.keys():
                list_of_skills[index] = list_of_skills[index].replace(key, letters_mapping[key])
    return list_of_skills


def randomize_npc():
    fake = Faker("ru_RU")
    first_name = fake.first_name()
    last_name = fake.last_name()
    job = fake.job()
    town = fake.city()
    strength = random.randint(3, 18)
    agility = random.randint(3, 18)
    endurance = random.randint(3, 18)
    intelligence = random.randint(3, 18)
    luck = random.randint(3, 18)
    skills = random.sample(replace_letters_in_skillnames_to_runic(), 3)
    return first_name, last_name, job, town, strength, agility, endurance, intelligence, luck, skills


def main():
    if not os.path.isdir("NPC_Cards"):
        os.mkdir("NPC_Cards")
    for i in range(10):
        i = i + 1
        context = {
            "first_name": randomize_npc()[0],
            "last_name": randomize_npc()[1],
            "job": randomize_npc()[2],
            "town": randomize_npc()[3],
            "strength": randomize_npc()[4],
            "agility": randomize_npc()[5],
            "endurance": randomize_npc()[6],
            "intelligence": randomize_npc()[7],
            "luck": randomize_npc()[8],
            "skill_1": randomize_npc()[9][0],
            "skill_2": randomize_npc()[9][1],
            "skill_3": randomize_npc()[9][2]
        }
        card_name = f"NPC_card_{i}.svg"
        file_operations.render_template("charsheet.svg", f"NPC_Cards/{card_name}", context)


if __name__ == "__main__":
    main()
