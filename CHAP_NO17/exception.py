class JustNotCoolError(Exception):
    pass


x=1
try:
    raise JustNotCoolError("This Just is not cool")
    # raise Exception("I'm a custom exception")
    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed")
except NameError:
    print(f"NameError means something is probaby")
except ZeroDivisionError:
    print("PLease donot divide by zero")
except Exception as error:
    print(error)
else:
    print("no error!")
finally:
    print(f"x is divided by 1")