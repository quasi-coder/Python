def main():
    infile = open('Files/lines.txt', 'rt')
    outfile = open ('Files/lines-copy.txt','wt')
    for line in infile:
        #outfile.writelines(line)

        #The difference is is that with the print function, I'm able to strip these line endings, and rewrite the line #endings with the default line endings for this operating system, which print does by default, and that way, if #my input file is from another operating system with different line endings, I'm actually serving to translate #those line endings into the correct one for this operating system, so it's important to know that distinction.
        
        print(line.rstrip(), file=outfile)
        print('.',end=' ',flush=True)
    outfile.close()
    print('\ndone.')

if __name__=='__main__':main()
