class Weapon:
    def __init__(self, name):
        self.weapon_name = name


weapon_type = None
weapon_rarity = None
weapon_description = None
weapon_ability = None
weapon_damage = None
weapon_attack_speed = None

# Attack Speed works as a marker which decreases weapon cool down


def tostring(self):
    output = self.weapon_name, weapon_rarity, weapon_type, weapon_description, weapon_damage, weapon_attack_speed
    return output


class Testing:

    s1 = Weapon("Blood")
    print(s1)