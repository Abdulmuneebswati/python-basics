person = "muneeb"
coins = 3

print("\n" + person + " has " + str(coins) + " coins left.")
message = "\n%s has %s coins left." % (person,coins)

print(message)


message1 = "\n{} has {} coins left.".format(person,coins)

print(message1)


message2 = "\n{1} has {0} coins left.".format(coins,person)

print(message2)

message3 = "\n{person} has {coins} coins left.".format(coins=coins,person=person)

print(message3)

player = {"person":"muneeb","coins":3}

message4 = "\n{person} has {coins} coins left.".format(**player)
print(message4)


# f--strings this way


message5 = f"\n{player["person"].upper()} has {coins} coins left"
print(message5)