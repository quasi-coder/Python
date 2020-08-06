def main():
    #animals = dict(kitten = "meow", puppy = "ruff", lion = "grrrr",giraffe = "I am a giraffe", dragon = "rawr")
    animals = {"kitten":"meow", "puppy":"ruff","lion":"grrrr","giraffe":"I am a giraffe","dragon":"rawr"}
    for k in animals.keys():
        print(k)
    for v in animals.values():
        print(v)
    print(animals["lion"])
    animals["kitten"] = "purr"
    animals["monkey"] = "haha"
    print("lion" in animals)
    print("found" if "lion" in animals else "nope!")
    print(animals.get("godzilla"))
    print_dict(animals)

def print_dict(o):
    for k, v in o.items():
        print(f"{k}:{v}")

if __name__=="__main__":main()
