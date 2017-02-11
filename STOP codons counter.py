##PROGRAMME COMPTAGE CODONS STOP (Approche Biologique) :
maseq=raw_input("Tappez votre séquence ADN (séquence test : ATGTAGCCTAAGTAGCCG) : ")
maseq=maseq.lower()
#séquence test : ATGTAGCCTAAGTAGCCG
def monprogramme(maseq):
    stop = len(maseq)
    i = 0
    find = False
    while i < stop and find == False :
        if maseq[i] != "t" :
            i=i+1
        else :
            if maseq[i+1] == "a" :
                if maseq[i+2] == "a" or maseq[i+2] == "g" :
                    find = True
                    startCodStop = i
                else :
                    i=i+1
            else :
                if maseq[i+1] == "g" and maseq[i+2] == "a" :
                    find = True
                    startCodStop = i
                else :
                    i=i+1
    if find == True :
        print "Il y a ",startCodStop," codons STOP"
    else :
        print "Aucun codon stop trouvé"
        
monprogramme(maseq)

'''
Il y a  3  codons STOP
'''
