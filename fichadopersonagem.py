#ficha do personagem

class Character:
    def __init__(self, character_class, race, name, ability_scores):
        self.character_class = character_class
        self.race = race
        self.name = name
        self.ability_scores = self.__arrange_ability_scores__(ability_scores)

    def __arrange_ability_scores__(self, scores):
        arranged_scores = {
            'Frontend': 0,
            'Backend': 0,

        }

        if self.character_class == "Fullstack":
            arranged_scores["Frontend"] = scores[4]
            arranged_scores["Backend"] = scores[4]

        elif self.character_class == "Backend":
            arranged_scores["Frontend"] = scores[2]
            arranged_scores["Backend"] = scores[6]

        elif self.character_class == "Frontend":
            arranged_scores["Frontend"] = scores[6]
            arranged_scores["Backend"] = scores[2]

        return arranged_scores

def get_ability_scores():
    scores = []
    print("Insira suas habilidades (2 valores):")
    for ability in ["Frontend", "Backend"]:
        score = int(input(f"{ability}: "))
        scores.append(score)
    return scores

# Coleta de dados do personagem
name = input("Qual seu nome? ")
character_class = input("Escolha uma classe (Fullstack, Frontend, Backend): ")
character_race = input("Escolha uma raça (Human): ")

ability_scores = get_ability_scores()

character = Character(character_class, character_race, name, ability_scores)

print(f"{character.name} - {character.race} {character.character_class} Ability Scores:", character.ability_scores)
