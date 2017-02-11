##Programme : Tester la présence d'un caractère dans 1 ligne :
maChaine= raw_input("Copier votre phrase ci-après : ")
Letter= raw_input("Tappez la lettre que vous cherchez : ")
count=0
for i in maChaine :
    if i==Letter in maChaine :
        count = count+1
if count!=0 :
    print "il y a" , count , "fois la lettre", Letter
else :
    print "la lettre", Letter, "n'est pas présente dans votre phrase"