

encr=int(input("do you want to encr (1) o decr (0): "))

name=input("please enter the phraze: ")

#move=int(input("please enter the step to move: "))

for move in range(-26,0):

    eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

    if name[1] in rus_lower_alphabet or name[1] in rus_upper_alphabet:
        leng="rus"
    else: leng="eng"


    def encr_in(alp):
        for i in range(len(name)):
            if name[i] in l or name[i] in L:
                if l.find(name[i])+move>alp-1 or L.find(name[i])+move>alp-1:
                    print(chr(ord(name[i])-alp+move), end="")
                else:
                    print(chr(ord(name[i])+ move), end="")
            else:
                print(name[i], end="")

    def encr_out(alp):
        for i in range(len(name)):
            if name[i] in l or name[i] in L:
                if (l.find(name[i])+move)<0 and (L.find(name[i])+move)<0:
                    print(chr(ord(name[i])+alp+move), end="")
                else:
                    print(chr(ord(name[i])+move), end="")
            else:
                print(name[i], end="")

    if encr == 1:
        if leng == "rus":
            l=rus_lower_alphabet
            L=rus_upper_alphabet
            encr_in(32)
        elif leng == "eng":
            l = eng_lower_alphabet
            L = eng_upper_alphabet
            encr_in(26)

    if encr == 0:
        if leng == "rus":
            l = rus_lower_alphabet
            L = rus_upper_alphabet
            encr_out(32)
        elif leng == "eng":
            l = eng_lower_alphabet
            L = eng_upper_alphabet
            encr_out(26)
    print()




