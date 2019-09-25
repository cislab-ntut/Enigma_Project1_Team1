from copy import deepcopy

def SwapListVal(myList,index1,index2):
    a=myList[index1]
    b=myList[index2]
    myList[index1]=b
    myList[index2]=a

stdAlphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
plugBoardKey=deepcopy(stdAlphabet)
rotorsOrderKey=list()
rotorsStartPointKey=list()

## Clear files
file=open('RotorsOrder.txt','w')
file.write('')
file=open('RotorsStartPoint.txt','w')
file.write('')
file=open('PlugBoard.txt','w')
file.write('')

swapTable=list()

found=False;
rotor0=2
for rotor1 in range(0,5):
    if found:
        break
    for rotor2 in range(0,5):
        if found:
            break
        if rotor1!=rotor0:
            if rotor2!=rotor1 and rotor2!=rotor0:
                file=open('RotorsOrder.txt','a')
                file.write(str(rotor0)+str(rotor1)+str(rotor2))

                for startPoint2 in stdAlphabet:
                    if found:
                        break
                    for startPoint1 in stdAlphabet:
                        if found:
                            break
                        for startPoint0 in stdAlphabet:
                            file=open('RotorsStartPoint.txt','a')
                            file.write(startPoint2+startPoint1+startPoint0)

                            ## Try all possibility of plugboard with 6 lines
                            ## line1
                            for i in range(0,len(plugBoardKey)):
                                for j in range(i+1,len(plugBoardKey)):
                                    swapTable.append(stdAlphabet.index(plugBoardKey[i]))
                                    swapTable.append(stdAlphabet.index(plugBoardKey[j]))

                                    ###### modify list for next loop
                                    swapPairs=[plugBoardKey[i],plugBoardKey[j]]
                                    plugBoardKey.pop(plugBoardKey.index(swapPairs[0]))
                                    plugBoardKey.pop(plugBoardKey.index(swapPairs[1]))

                                    ### line2
                                    plugBoardKey_loop1=deepcopy(plugBoardKey)
                                    for m in range(0,len(plugBoardKey)):
                                        for n in range(m+1,len(plugBoardKey)):
                                            swapTable.append(stdAlphabet.index(plugBoardKey[m]))
                                            swapTable.append(stdAlphabet.index(plugBoardKey[n]))

                                            swapPairs=[plugBoardKey[m],plugBoardKey[n]]
                                            plugBoardKey.pop(plugBoardKey.index(swapPairs[0]))
                                            plugBoardKey.pop(plugBoardKey.index(swapPairs[1]))

                                            #### line3
                                            plugBoardKey_loop2=deepcopy(plugBoardKey)
                                            for x in range(0,len(plugBoardKey)):
                                                for y in range(x+1,len(plugBoardKey)):
                                                    swapTable.append(stdAlphabet.index(plugBoardKey[x]))
                                                    swapTable.append(stdAlphabet.index(plugBoardKey[y]))

                                                    swapPairs=[plugBoardKey[x],plugBoardKey[y]]
                                                    plugBoardKey.pop(plugBoardKey.index(swapPairs[0]))
                                                    plugBoardKey.pop(plugBoardKey.index(swapPairs[1]))

                                                    ### line4
                                                    plugBoardKey_loop3=deepcopy(plugBoardKey)
                                                    for a in range(0,len(plugBoardKey)):
                                                        for b in range(a+1,len(plugBoardKey)):
                                                            swapTable.append(stdAlphabet.index(plugBoardKey[a]))
                                                            swapTable.append(stdAlphabet.index(plugBoardKey[b]))

                                                            swapPairs=[plugBoardKey[a],plugBoardKey[b]]
                                                            plugBoardKey.pop(plugBoardKey.index(swapPairs[0]))
                                                            plugBoardKey.pop(plugBoardKey.index(swapPairs[1]))

                                                            ### line5
                                                            plugBoardKey_loop4=deepcopy(plugBoardKey)
                                                            for p in range(0,len(plugBoardKey)):
                                                                for q in range(p+1,len(plugBoardKey)):
                                                                    swapTable.append(stdAlphabet.index(plugBoardKey[p]))
                                                                    swapTable.append(stdAlphabet.index(plugBoardKey[q]))

                                                                    swapPairs=[plugBoardKey[p],plugBoardKey[q]]
                                                                    plugBoardKey.pop(plugBoardKey.index(swapPairs[0]))
                                                                    plugBoardKey.pop(plugBoardKey.index(swapPairs[1]))

                                                                    ### line6
                                                                    plugBoardKey_loop5=deepcopy(plugBoardKey)
                                                                    for e in range(0,len(plugBoardKey)):
                                                                        for f in range(e+1,len(plugBoardKey)):
                                                                            swapTable.append(stdAlphabet.index(plugBoardKey[e]))
                                                                            swapTable.append(stdAlphabet.index(plugBoardKey[f]))
                                                                            print('Pairs of letters indices to swap in plugboard: ',swapTable)

                                                                            swapPairs=[plugBoardKey[e],plugBoardKey[f]]
                                                                            plugBoardKey.pop(plugBoardKey.index(swapPairs[0]))
                                                                            plugBoardKey.pop(plugBoardKey.index(swapPairs[1]))

                                                                            ## Use swapTable to bulid the plugboard
                                                                            tempPlugBoard=deepcopy(stdAlphabet)
                                                                            for swap_item_index in range(0,len(swapTable),2):
                                                                                SwapListVal(tempPlugBoard,swapTable[swap_item_index],swapTable[swap_item_index+1])

                                                                            file=open('PlugBoard.txt','a')
                                                                            for letter in tempPlugBoard:
                                                                                file.write(letter)
                                                                            exec(open("Enigma.py").read())
                                                                            file=open('PlugBoard.txt','w')
                                                                            file.write('')

                                                                            plugBoardKey=deepcopy(plugBoardKey_loop5)
                                                                            swapTable.pop()
                                                                            swapTable.pop()

                                                                    plugBoardKey=deepcopy(plugBoardKey_loop4)
                                                                    swapTable.pop()
                                                                    swapTable.pop()

                                                            plugBoardKey=deepcopy(plugBoardKey_loop3)
                                                            swapTable.pop()
                                                            swapTable.pop()



                                                    plugBoardKey=deepcopy(plugBoardKey_loop2)
                                                    swapTable.pop()
                                                    swapTable.pop()


                                            plugBoardKey=deepcopy(plugBoardKey_loop1)
                                            swapTable.pop()
                                            swapTable.pop()

                                    plugBoardKey=deepcopy(stdAlphabet)

                                    swapTable.pop()
                                    swapTable.pop()


                            file=open('RotorsStartPoint.txt','w')
                            file.write('')
                            file=open('PlugBoard.txt','w')
                            file.write('')

                            file=open('result.txt','r')
                            resultStr=file.read()
                            if resultStr[-6:]=='HITLER':
                                found=True
                                break

                file=open('RotorsOrder.txt','w')
                file.write('')

file.close()








