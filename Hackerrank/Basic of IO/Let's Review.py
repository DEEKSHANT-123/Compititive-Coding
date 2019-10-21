for _ in range(int(input())):  #Test cases
    s = input()
    print(*["".join(s[::2]),"".join(s[1::2])]) #"* symbol remove breckets from list."
                                               #s[::2] here 2 is steps, and in s[1::2] 1 is starting index of string and 2 is steps. 
