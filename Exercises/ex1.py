# def row_sum_odd_numbers(n):
#     total = n ** 3
#     return total


# row_sum_odd_numbers(2)


class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def __str__(self):
        return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)

    __repr__ = __str__


def declare_winner(fighter1, fighter2, first_attacker):
    # Determine the attacker and defender
    attacker = fighter1 if fighter1.name == first_attacker else fighter2
    defender = fighter2 if attacker == fighter1 else fighter1

    while attacker.health > 0 and defender.health > 0:
        defender.health -= attacker.damage_per_attack
        if defender.health <= 0:
            return attacker.name  

        attacker, defender = defender, attacker

    return defender.name


winner = declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Harald")
print(winner)  # Output: "Lew"