n = 42
c = 4
print(f"Hello, this is my commit number {n} of a .py-file in this repo.")
print(f"There are {c} contributors in this file.")

def fish():
    fishy = input("What is your favorite fish? Insert here: ")
    rating = input("How would you rate it from 1 to 10? Insert here: ")
    if int(rating) >= 5:
        print(fishy + "? That sounds delicious!")
    else:
        print(fishy + "? That sounds disgusting!")
    return

fish()
