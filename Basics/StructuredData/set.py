def main():
    a = set ("We are gonna need a bigger boat.")
    b = set ("I am sorry. I am afraid I can't do that.")
    invite = set(['Nestor','Amanda','Olivia'])
    print_set(sorted(a)) # sorted
    print_set(b)# unsorted
    print_set(a-b) # members in set a but not in set b
    print_set(a|b) # members in set a or set b
    print_set(a ^ b) # members in set a or set b but not in both
    print_set(a & b)# members in set a and set b
    print('Verne' in invite)
    invite.add('Verne')
    print('Verne' in invite)
    invite.remove('Nestor')
    print(invite.pop())
    print(invite)

def print_set(o):
    print("{",end = " ")
    for x in o:
        print(x, end= " ")
    print("}")

if __name__=="__main__":main()
