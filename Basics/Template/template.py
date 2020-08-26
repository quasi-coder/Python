from string import Template

def main():
    str1 = "You are watching {0} by {1}".format("Advanced Python","Quasi-coder")
    print(str1)
    templ = Template("You are watching ${title} by ${author}")
    str2 = templ.substitute(title="Advanced Python", author="Quasi-coder")
    print(str2)
    data = {
        "author": "Quasi-coder",
        "title" : "Advanced Python"
    }
    str3 = templ.substitute(data)
    print(str3)
    
if __name__=="__main__":main()
