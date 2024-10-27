# import math

# def title_case(title, minor_words=''):
#     words = title.split()
#     minorWords = minor_words.lower().split()
    
#     result = []

#     result.append(words[0].capitalize())  if words else None
    
#     for word in words[1:]:
#         if word.lower() in minorWords:
#             result.append(word.lower())
#         else:
#             result.append(word.capitalize())
    
#     return (" ").join(result)
# print(title_case('', 'a an the of'))


# def greet(name):
#     return f"Hello, {name} how are you doing today?"
    

# def small_enough(array, limit):
#     y = 78
#     return y in array


# print(small_enough([78, 117, 110, 99, 104, 117, 107, 115] ,100))


# def human_years_cat_years_dog_years(n):
    
#     if (n==1):
#         return [1,15,15]
#     elif (n==2):
#         return [1,24,24]
#     else:
#         return [n,24 + (n-2)*4,24 + (n-2)*5]
# print(human_years_cat_years_dog_years(10))

# def is_anagram(test, original):
#     return "".join(sorted(test.lower())) ==  "".join(sorted(original.lower())) 

# print(is_anagram("foefeta", "toffee"))

# def reverse(st):
#     list = st.split(" ")
#     list.reverse()
#     return (" ").join(list) 

# print(reverse('Hello World'))

def update_light(current):
    return "yellow"  if current == "green" else "red" if current == "yellow" else "yellow" 

print(update_light("green"))