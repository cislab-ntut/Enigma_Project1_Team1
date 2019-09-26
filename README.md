# Project1-1_Enigma_machine

以下所談到之英文字母串列之起始位置皆由0起算,且wheel編號為舉例用(對應老師給的Model)
step1:

經由鍵盤輸入英文字母(假設為A)後,根據A-Z之順序找出該字母之位置,再根據該位置於wheel III 上目前之字母串列(注意:此處針對老師給的Model示意圖,因為每次輸入皆會使wheel轉動,所以將每次看成不同之串列)找到對應的字母(假設為Y),再到Enigma I之表格查出該字母(Y)於wheel III 所對應到的字母(假設為Q),並傳遞該字母(Q)在wheel III 上的串列位置給wheel II,完成wheel III 之加密工作.

step2:

wheel II 會依據所接收之位置由目前wheel II 上之字母串列找出對應之英文字母(假設為V),再跟據該字母回到Enigma I之表格查出該字母(V)於wheel II 所對應之英文字母(假設為I),並傳遞該字母在wheel II 上的串列位置給wheel I,完成wheel II 之加密工作.

step3:

wheel I 會依據所接收之位置由目前wheel I 上之字母串列找出對應之英文字母(假設為C),再跟據該字母回到Enigma I之表格查出該字母©於wheel I 所對應之英文字母(假設為M),並傳遞該字母在wheel I 上的串列位置給reflector,完成wheel I 之加密工作.

step4:

reflector 會找到所接收之位置上的英文字母(假設為F),而後再於Enigma I之表格查出該字母(F)於reflector所對應之英文字母,並傳遞該字母在reflector 上的串列位置給wheel I,完成reflector之反向動作.

step5:

依據step1 ~ step4,進行逆向加密(wheel I -> wheel II -> wheel III -> output)

done
