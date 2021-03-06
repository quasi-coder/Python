#
# Example file for working with loops
#

def main():
  x = 0
  secret = "swordfish"
  pw = " "

  # define a while loop
  while (x < 5):
     print(x)
     x = x + 1
  
  while pw != secret:
    pw = input("What's the secret word? ")

  # define a for loop, 5 being inclusive and 10 being exclusive
  for x in range(5, 10):
    print(x)

  # use a for loop over a collection
  days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
  for d in days:
    print(d)

  # use the break and continue statements
  for x in range(5, 10):
    if (x == 7): break
    if (x % 2 == 0): continue # when the condition is true, it won't execute the print(x)(6,8), only in the case of condition false it will exexute print(x)(5,7,9)
    print(x)

  #using the enumerate() function to get index
  days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
  for i, d in enumerate(days):
    print(i, d)


if __name__ == "__main__":
  main()
