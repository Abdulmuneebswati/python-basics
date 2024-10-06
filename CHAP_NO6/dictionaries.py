# band = {
#     "vocals": "Plant",
#     "guitar": "Page"
# }

# band2 = dict(vocals="Plant", guitar="Page")

# print(band2)
# print(type(band))
# print(len(band))

# print(band["vocals"])
# print(band.get("guitar"))
# print(band2["vocals"])
# print(band2.get("guitar"))

# print(band.keys())
# print(band2.keys())

# print(band.values())
# print(band2.values())

# print(band.items())
# print(band2.items())

# print("guitar" in band)
# print("triangle" in band)

# band["vocals"] = "Coverdale"
# band.update({"bass": "JPJ"})

# print(band.pop("bass"))
# print(band)


# band["drums"] = "Bonham"
# print(band)

# print(band.popitem())  # tuple
# print(band)

# band["drums"] = "Bonham"
# del band["drums"]
# print(band)


# band2.clear()
# del band2
# band2 = band  # create a reference
# print("Bad copy!")
# print(band2)
# print(band)

# band2 = band.copy()
# band2["drums"] = "Dave"
# print("Good copy!")
# print(band)
# print(band2)


# band3 = dict(band)
# print("Good copy!")
# print(band3)

# member1 = {
#     "name": "Plant",
#     "instrument": "vocals"
# }
# member2 = {
#     "name": "Page",
#     "instrument": "guitar"
# }
# band = {
#     "member1": member1,
#     "member2": member2
# }

# print(band)
# print(band["member1"]["name"])
# print(band["member1"])

# nums = {1, 2, 3, 4}

# nums2 = set((1, 2, 3, 4))

# print(nums)
# print(nums2)
# print(type(nums))
# print(len(nums))

# nums = {1, 2, 2, 3}
# print(nums)


# nums = {1, True, 2, False, 3, 4, 0}
# print(nums)
# print(2 in nums)
# print(False in nums)

# nums.add(8)
# print(nums)
# morenums = {5, 6, 7}
# nums.update(morenums)
# print(nums)

# one = {1, 2, 3}
# two = {3,5, 6, 7}

# mynewset = one.union(two)
# print(mynewset)

# one.intersection_update(two)
# print(one)

one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)