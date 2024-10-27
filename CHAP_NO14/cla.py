
def hello(name,lang):
    greeting={
        "English":"Hello",
        "French":"Holla",
        "German":"Holla",
    }
    print(f"{greeting[lang]} {name}!")

if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(
        description = "provides a person greeting"
    )
    parser.add_argument(
        "-n", "--name" , metavar="name" , required=True, help="The name of the person to greet."
    )

    parser.add_argument(
        "-l", "--lang" , metavar="language" , required=True, choices=["English","French","German"],
        help="The language of the greeting"
    )
    args = parser.parse_args()
    hello(args.name,args.lang)