message="monika"
i=0
while i<len(message):
    letter = message[i]
    print(chr(ord(letter)+2), end='')
    i+=1
