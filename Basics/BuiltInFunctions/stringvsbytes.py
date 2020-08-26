def main():
    b = bytes([0x41,0x42,0x43,0x44])
    print(b)

    s = "This is a string"
    print(s)
    
    print(s+b.decode("utf-8"))
    print(s.encode("utf-8")+b)

if __name__=="__main__":main()