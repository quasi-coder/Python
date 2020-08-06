def main():
    infile = open('Files/berlin.jpeg','rb')
    outfile = open('Files/berlin-copy.jpeg','wb')
    while True:
        buf = infile.read(10240)
        if buf:
            outfile.write(buf)
            print('.',end=' ', flush=True)
        else:
            break
    outfile.close()
    print('\ndone.')

if __name__=='__main__':main()

