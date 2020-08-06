# A list is an ordered collection, it's sequential and it's interval, mutable
def main():
    game = ["Rock", "Paper", "Scissor", "Lizard","Spock"]
    print(len(game))
    print(",".join(game))
    game.append("Computer")
    game.insert(0,"StarWars")
    game.remove("Rock")
    x = game.pop()# Remove item from end of list
    print(f"Popped item is {x}")
    game.pop(3)  # Remove ar index
    del game[0]
    #del game[1:5:2]
    print(game[1:5:2])#[beginingOfSlice:endOfSlice:Step]
    i = game.index("Paper")
    print(game[i])
    print_list(game)

def print_list(o):
    for i in o:
        print(i, end=" ", flush=True)
    print()

if __name__ == "__main__": main()
