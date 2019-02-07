# ROT cipher

def encrypt(string, shift):
    slist = []
    characters = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    translate = characters[shift*2:] + characters[:shift*2]
    for i in string:
        if characters.find(i) > -1:
            slist.append(translate[characters.find(i)])
        else:
            slist.append(i)
    return ''.join(slist)

    #    rot_char = lambda c: trans[chars.find(c)] if chars.find(c)>-1 else c
    # return ''.join( rot_char(c) for c in s )

message = input("What message would you like to encrypt? : ")

while True:
    shift = input("When we encrypt how far should we shift? : ")
    if shift.isdigit():
        shift = int(shift)
        break
    else:
        print("Please enter a number")

print(f"We will now encrypt your message '{message}' and shift it by {shift} characters : {encrypt(message, shift)}")
