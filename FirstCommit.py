from random import sample, choice

n = 42
c = 4
print(f"Hello, this is my commit number {n} of a .py-file in this repo.")
print(f"There are {c} contributors in this file.")


def fish():
    fishy = input("What is your favorite fish? Insert here: ")
    if fishy == "Salmon":
        print("You know who also likes Salmon? Grizzly bears!")
    elif fishy == "Bass":
        print("I always suspected it.")
    elif fishy == "Dolphin":
        print("Now that's not even a real fish, is it?")
    elif fishy == "Trout":
        print("Really? I highly TROUT that! See what I did there?")
    elif fishy == "Catfish":
        print("Catfish? Highly suspicious.")
    else:
        print(fishy + "? That sounds disgusting!")
    return


TopFishes = ["Salmon", "Bass", "Dolphin", "Trout", "Catfish"]


def guessgame(fishlist):
    fishpick = sample(fishlist, 3)
    favorite = choice(fishpick)
    print(f"Can you also guess my favorite fish?\nIt's one of these: {fishpick}")
    fishguess = input("Insert your choice here: ")
    if fishguess == favorite:
        print("That's correct! Have you been through my personal stuff?")
    else:
        print(f"No, why would I even remotely like {fishguess}?!")


fish()
guessgame(TopFishes)
