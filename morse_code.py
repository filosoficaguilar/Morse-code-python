alphabet = {"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--.."}
def splitWord(word): 
    return [char for char in word]
last = ""
choose = int(input("Select an option: \n1. Morse to String \n2. String to Morse\n"))
if(choose==1):
    morse = input("Type the code morse with a space between each letter\n").split()
    for i in morse:
        for key,val in alphabet.items():
            if(val == i):
                last += " "+key
else:
    st = splitWord(input("Type the string\n").upper().replace(" ",""))
    for i in st:
        for key,val in alphabet.items():
            if(key == i):
                last += " "+val

print(last)
