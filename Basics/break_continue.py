secret = "swordfish"
pw = " "
count = 0
auth = False
max_attempt = 5 

while pw != secret:
    count+=1
    if count>max_attempt: break # it will break all the way out of the loop skip the else block
    if count == 3 :continue # It just goes up at line 7 and checks the condition so instead of 5 trials only 4 trials 
    pw = input(f"{count} What's the secret word? ")
else:
    auth = True

print("Authorized" if auth else "Calling the FBI ...")

animals = ("bear","bunny","dog","cat","velociraptor")
for pet in animals:
    if pet == "dog" :continue # shortcuts the loop to top 
    if pet == "velociraptor" : break
    print(pet)
else:
    print("that is all of the animals")