#
# Read and write files using the built-in Python file methods
#

def main():  
  # Open a file for writing and create it if it doesn't exist 
  #it empties the file if the file is not empty, and it starts at the beginning and writes over the file.
  f = open("textfile.txt","w+")
  
  # Open the file for appending text to the end
  #f the file doesn't exist, it creates it. A is a pen mode, this is just like write, but if the file already has some #content in it, it starts at the end of the file and it does not empty the file and it does not create the file.
  # f = open("textfile.txt","a+")

  # write some lines of data to the file
  for i in range(10):
    f.write("This is line %d\r\n" % (i+1))
  
  # close the file when done
  f.close()
  
  # Open the file back up and read the contents
  f = open("textfile.txt","r")
  # Open the file read and write the contents with + option
  #f = open("textfile.txt", "r+")
  # Open the file read and write the contents with binary and text option
  #f = open("textfile.txt", "r+b")
  #f = open("textfile.txt", "r+t")
  #f = open("textfile.txt", "r")
  #for line in f:
    #print(line.rstrip())
  if f.mode == 'r': # check to make sure that the file was opened
    # use the read() function to read the entire file
    # contents = f.read()
    # print (contents)
    
    fl = f.readlines() # readlines reads the individual lines into a list
    for x in fl:
      print (x)
  
    
if __name__ == "__main__":
  main()
