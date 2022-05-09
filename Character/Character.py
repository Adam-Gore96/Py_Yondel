from collections import OrderedDict


class Character:
    def __init__(self, name):
        self.character_name = name

    character_level = 1
    character_class = None
    character_health = 100
    character_weapon = "Fist"

    # stats = {"vitality": 10, "strength": 10, "dexterity": 10, "intellect": 10, "spirit": 10}
    stats = OrderedDict()
    stats['strength'] = 10
    stats['vitality'] = 10
    stats["dexterity"] = 10
    stats["intellect"] = 10
    stats["spirit"] = 10

    def add_stats(self, stat, number_of_stats, damage_type):
        stat_type = stat
        stat_change = number_of_stats
        damage_type = damage_type

        if damage_type == 0:
            self.stats[stat_type] -= stat_change
        elif damage_type == 1:
            self.stats[stat_type] += stat_change




    def attack_power_conversion(self):
        count = 0
        strg = self.stats['strength']
        print(strg)
        power = 0
        while strg != 0:
            if strg < 20:
                power += 5
                strg -= 1
            elif strg > 20 & strg < 40:
                power += 1
                strg -= 1
            elif strg == 40:
                power += 100
                strg -= 1

        return power

    # The getters for all the aspects of a character

    def get_character_name(self):
        return self.character_name

    def get_character_level(self):
        return self.character_level

    def get_character_class(self):
        return self.character_class

    def get_character_health(self):
        return self.character_health

    def get_character_weapon(self):
        return self.character_weapon

    # The Setters for all the aspects of a character

    def set_character_name(self, name):
        self.character_name = name

    def set_character_level(self, level):
        self.character_level = level

    def set_character_class(self, name):
        self.character_class = name

    def set_character_health(self, health, type):
        if type == 1:
            self.character_health += health
        elif type == 2:
            self.character_health -= health

    def set_character_weapon(self, name):
        self.character_weapon = name
