
stdAlphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
plugBoard=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
reflector=['Y','R','U','H','Q','S','L','D','P','X','N','G','O','K','M','I','E','B','F','Z','C','W','V','J','A','T']
rotors = [['E','K','M','F','L','G','D','Q','V','Z','N','T','O','W','Y','H','X','U','S','P','A','I','B','R','C','J'],
            ['A','J','D','K','S','I','R','U','X','B','L','H','W','T','M','C','Q','G','Z','N','P','Y','F','V','O','E'],
            ['B','D','F','H','J','L','C','P','R','T','X','V','Z','N','Y','E','I','W','G','A','K','M','U','S','Q','O'],
            ['E','S','O','V','P','Z','J','A','Y','Q','U','I','R','H','X','L','N','F','T','G','K','D','C','M','W','B'],
            ['V','Z','B','R','G','I','T','Y','U','P','S','D','N','H','L','X','A','W','M','J','Q','O','F','E','C','K']]
rotorsStartPoint=['H','D','X']
turnover=['Q','E','V','J','Z']
counter=0
rotorOrder=[2,1,0]

def rotorMapping(rotors,rotorOrderNumber,reverse,input):
    if reverse==False:
        index=(ord(rotorsStartPoint[rotorOrderNumber])-65+input)%26
        ##x=stdAlphabet[index]
        y=rotors[rotorOrderNumber][index]
        if stdAlphabet.index(y)<stdAlphabet.index(rotorsStartPoint[rotorOrderNumber]):
            return y,stdAlphabet.index(y)+(26-stdAlphabet.index(rotorsStartPoint[rotorOrderNumber]))
        else:
            return y,stdAlphabet.index(y)-stdAlphabet.index(rotorsStartPoint[rotorOrderNumber])
    else:
        index=(ord(rotorsStartPoint[rotorOrderNumber])-65+input)%26
        x=stdAlphabet[index]
        y=stdAlphabet[rotors[rotorOrderNumber].index(x)]
        if stdAlphabet.index(y)<stdAlphabet.index(rotorsStartPoint[rotorOrderNumber]):
            return y,stdAlphabet.index(y)+(26-stdAlphabet.index(rotorsStartPoint[rotorOrderNumber]))
        else:
            return y,stdAlphabet.index(y)-stdAlphabet.index(rotorsStartPoint[rotorOrderNumber])

def encryptOneLetter(rotors,rotorsOrder,plugBoard,reflector,letter):
    rotate()
    letterNumber=stdAlphabet.index(letter)
    rotor3_forward_input=letterNumber
    r3f,rotor3_forward_output=rotorMapping(rotors,rotorsOrder[0],False,rotor3_forward_input)
    r2f,rotor2_forward_output=rotorMapping(rotors,rotorsOrder[1],False,rotor3_forward_output)
    r1f,rotor1_forward_output=rotorMapping(rotors,rotorsOrder[2],False,rotor2_forward_output)
    reflector_output=stdAlphabet.index(reflector[rotor1_forward_output])
    r1r,rotor1_reverse_output=rotorMapping(rotors,rotorsOrder[2],True,reflector_output)
    r2r,rotor2_reverse_output=rotorMapping(rotors,rotorsOrder[1],True,rotor1_reverse_output)
    r3r,rotor3_reverse_output=rotorMapping(rotors,rotorsOrder[0],True,rotor2_reverse_output)
    encryptedLetter=stdAlphabet[rotor3_reverse_output]
    print(r3r)
    #encryptedLetter=stdAlphabet[plugBoard.index(r3r)]
    return encryptedLetter

def rotate():
    #double stepping
    if turnover[rotorOrder[0]]!=rotorsStartPoint[2] and turnover[rotorOrder[1]]!=rotorsStartPoint[1]:
        rotorsStartPoint[2]=stdAlphabet[(stdAlphabet.index(rotorsStartPoint[2])+1)%26]
    else:
        rotorsStartPoint[2]=stdAlphabet[(stdAlphabet.index(rotorsStartPoint[2])+1)%26]
        if turnover[rotorOrder[1]]==rotorsStartPoint[1]:
            rotorsStartPoint[0]=stdAlphabet[(stdAlphabet.index(rotorsStartPoint[0])+1)%26]
        rotorsStartPoint[1]=stdAlphabet[(stdAlphabet.index(rotorsStartPoint[1])+1)%26]
    return
plainText=''

##while plainText!='exit' or plainText!='EXIT':
plainText = raw_input('Input plaintext:')
cipherText=''
for letter in plainText:
    cipherText+=encryptOneLetter(rotors,rotorOrder,plugBoard,reflector,letter)
print(cipherText)




