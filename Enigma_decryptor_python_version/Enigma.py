#rotorOrder=[2,1,0]
#plugBoard=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#rotorsStartPoint=['H','D','X']

stdAlphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

file=open('PlugBoard.txt','r')
plugBoard=list(file.read())

#startpoint / positionNumber: [rotor2,rotor1,rotor0]
file=open('RotorsStartPoint.txt','r')
rotorsStartPoint=list(file.read())

#Rotors Order: [rotor0,rotor1,rotor2]
file=open('RotorsOrder.txt','r')
rotorOrder=list(file.read())
for i in range(0,len(rotorOrder)):
    rotorOrder[i]=int(rotorOrder[i])

reflector=['Y','R','U','H','Q','S','L','D','P','X','N','G','O','K','M','I','E','B','F','Z','C','W','V','J','A','T']
rotors = [['E','K','M','F','L','G','D','Q','V','Z','N','T','O','W','Y','H','X','U','S','P','A','I','B','R','C','J'],
            ['A','J','D','K','S','I','R','U','X','B','L','H','W','T','M','C','Q','G','Z','N','P','Y','F','V','O','E'],
            ['B','D','F','H','J','L','C','P','R','T','X','V','Z','N','Y','E','I','W','G','A','K','M','U','S','Q','O'],
            ['E','S','O','V','P','Z','J','A','Y','Q','U','I','R','H','X','L','N','F','T','G','K','D','C','M','W','B'],
            ['V','Z','B','R','G','I','T','Y','U','P','S','D','N','H','L','X','A','W','M','J','Q','O','F','E','C','K']]

turnover=['Q','E','V','J','Z']
def rotorMapping(rotors,rotorOrderNumber,rotorPositionNumber,reverse,input):
    if reverse==False:
        index=(ord(rotorsStartPoint[rotorPositionNumber])-65+input)%26
        y=rotors[rotorPositionNumber][index]
        if stdAlphabet.index(y)<stdAlphabet.index(rotorsStartPoint[rotorPositionNumber]):
            return y,stdAlphabet.index(y)+(26-stdAlphabet.index(rotorsStartPoint[rotorPositionNumber]))
        else:
            return y,stdAlphabet.index(y)-stdAlphabet.index(rotorsStartPoint[rotorPositionNumber])
    else:
        index=(ord(rotorsStartPoint[rotorPositionNumber])-65+input)%26
        x=stdAlphabet[index]
        y=stdAlphabet[rotors[rotorOrderNumber].index(x)]
        if stdAlphabet.index(y)<stdAlphabet.index(rotorsStartPoint[rotorPositionNumber]):
            return y,stdAlphabet.index(y)+(26-stdAlphabet.index(rotorsStartPoint[rotorPositionNumber]))
        else:
            return y,stdAlphabet.index(y)-stdAlphabet.index(rotorsStartPoint[rotorPositionNumber])
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

def encryptOneLetter(rotors,rotorsOrder,plugBoard,reflector,letter):
    rotate()
    letterNumber=stdAlphabet.index(plugBoard[stdAlphabet.index(letter)])
    rotor3_forward_input=letterNumber
    r3f,rotor3_forward_output=rotorMapping(rotors,rotorsOrder[0],2,False,rotor3_forward_input)
    r2f,rotor2_forward_output=rotorMapping(rotors,rotorsOrder[1],1,False,rotor3_forward_output)
    r1f,rotor1_forward_output=rotorMapping(rotors,rotorsOrder[2],0,False,rotor2_forward_output)
    reflector_output=stdAlphabet.index(reflector[rotor1_forward_output])
    r1r,rotor1_reverse_output=rotorMapping(rotors,rotorsOrder[2],0,True,reflector_output)
    r2r,rotor2_reverse_output=rotorMapping(rotors,rotorsOrder[1],1,True,rotor1_reverse_output)
    r3r,rotor3_reverse_output=rotorMapping(rotors,rotorsOrder[0],2,True,rotor2_reverse_output)
    encryptedLetter=plugBoard[rotor3_reverse_output]

    return encryptedLetter



file=open('Input.txt','r')

plainText = file.read()
cipherText=''
for letter in plainText:
    cipherText+=encryptOneLetter(rotors,rotorOrder,plugBoard,reflector,letter)
file=open('Result.txt','w')
file.write(cipherText)

print("PlugBoard:          ",plugBoard)
print("Rotors Order:       ",rotorOrder)
print("Rotors Start Point: ",rotorsStartPoint)
print("Result:             ",cipherText)
print('\n')
file.close()






