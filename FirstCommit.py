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
    elif fishy == "Eel":
        print("What a funky choice.")
    else:
        print(fishy + "? That sounds disgusting!")
    return


TopFishes = ["Salmon", "Bass", "Dolphin", "Trout", "Catfish", "Eel"]


def guessgame(fishlist:list, sample_size:int = 3):

    if len(fishlist) >= sample_size:
        fishpick = sample(fishlist, k=sample_size)
    else:
        raise ValueError(f"The length of the input list ({len(fishlist)}) cannot be smaller than the chosen sample size ({sample_size}).")

    favorite = choice(fishpick)
    print(f"Can you also guess my favorite fish?\nIt's one of these: {fishpick}")
    fishguess = input("Insert your choice here: ")
    if fishguess == favorite:
        print("That's correct! Have you been through my personal stuff?")
    else:
        print(f"No, why would I even remotely like {fishguess}?!")
    return


fish()
guessgame(TopFishes)

# test of the new functionality of guessgame() --> it will raise a ValueError with the defined error message
guessgame(["Shark", "Trout", "Salmon"], sample_size=4)
