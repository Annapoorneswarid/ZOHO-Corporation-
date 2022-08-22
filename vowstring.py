def vowstring(string):
    string=string.lower()
    vowels=set("aeiou")
    set_a=set({})

    for char in string:
        if char in vowels:
            set_a.add(char)
        else:
            pass
    if len(set_a)==len(vowels):

        print("string is:", string)
        print("output is:", set(string) )
    else:
        print("not possible")
    return 0

if __name__=="__main__":
    string="aeiouae"
    vowstring(string)