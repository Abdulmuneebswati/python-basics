
# def printName():
#         color="red"
#         print(name)

# name = "Muneeb"
# printName()

# color = "blue"

# def parentFunc():
#     color="red"
#     def childFunc():
#         print(color)
#     childFunc()

# parentFunc()



# def parent():
#     count = 2
#     def child():
#         print(count)
#     child()

# parent()


count = 1

# def parent():
#     count += 1 
#     def child():
#         print(count)
#     child()

# parent() #this will show error


# def parent():
#     global count
#     count += 1
#     def child():
#         print(count)
#     child()

# parent() #2


def parent():
    color = "blue"
    def child():
        nonlocal color #reassgning the above variable
        color = "red"
        print(color)
    child()

parent() #2