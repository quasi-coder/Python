class RevStr(str):  
    # str is built-in class of pythonand,I'm overwriting the string representation method, to instead of returning the #string itself, to return a slice of the string where the step goes backwards. And so, this will reverse the string.
    def __str__(self):
        return self[::-1]

def main():
    hello = RevStr("Hello, World .")
    print(hello)

if __name__ =='__main__':main()
