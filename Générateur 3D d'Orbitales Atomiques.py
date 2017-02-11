
## MODE D'EMPLOI
'''
Pour utiliser ce script, il faut l'exéctuer une fois en entier (CTRL+E).
Depuis la console, on peut alors appeler la fonction orbitale qui prend en arguments les nombres quantiques l et ml. Par exemple, lorsqu'on saisit :

orbitale(2,1)
 
depuis la console, Python affiche (au bout d'un temps assez long) l'orbitale atomique correspondant à l=2 et ml=1
'''
## CHARGEMENT DES MODULES UTILES
 
import math
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
 
## DEFINITION DE LA CLASSE POLYNOME
 
class polynome:
    def __init__(self,liste_coeffs):
        self.coeffs=liste_coeffs
         
    def degre(self):
        n=len(self.coeffs)
        i=n-1
        while self.coeffs[i]==0:
            i-=1
            if i==-n:
                return -1
        return i
         
    def __add__(self,B):
        dA=self.degre()
        dB=B.degre()
        if dA<dB:
            self,B=B,self
        B0=B.coeffs+[0]*abs((dA-dB))
        return polynome([a+b for a,b in zip(self.coeffs,B0)])
     
    def __mul__(self,B):
        # multiplication par un scalaire à droite uniquement
        if isinstance(B,int) or isinstance(B,float):
            B=polynome([B])
        dA=self.degre()
        dB=B.degre()
        A0=self.coeffs+[0]*(dB)
        B0=B.coeffs+[0]*(dA)
        C=list()
        for i in range(dA+dB+1):
            c=0
            for k in range(i+1):
                c+=A0[k]*B0[i-k]
            C.append(c)
        return polynome(C)
         
    def __sub__(self,B):
        return self+polynome([-1])*B
         
    def __div__(self,scalaire):
        return polynome([ai/scalaire for ai in self.coeffs])
         
    def __call__(self,x):
        p=0
        for ai in reversed(self.coeffs):
            p=ai+x*p
        return p
 
    def deriv(self):
        return polynome([ai*(i+1) for i,ai in enumerate(self.coeffs[1:])])
         
    def deriv_n(self,n):
        p=self
        for i in range(n):
            p=p.deriv()
        return p

## PARTIE ANGULAIRE DE LA FONCTION D'ONDE
 
def fact(n):
    r=1
    for i in range(1,n+1):
        r=r*i
    return r
 
def legendre(l):
    L0=polynome([1])
    L1=polynome([0,1])
    if l==1:
        return L1
    elif l==0:
        return L0
    else:
        for i in range(2,l+1):
            A=L0*(-(i-1))
            B=(polynome([0,1])*L1)*(2*i-1)
            Ln=(B+A)*(1./i)
            L0=L1
            L1=Ln
    return Ln
         
def harmo(l,m,theta):
    x=math.cos(theta)
    L=legendre(l).deriv_n(abs(m))
    N=math.sqrt(fact(l-abs(m))*(2*l+1)/(fact(l+abs(m))*4*math.pi))
    Y1=polynome([1,0,-1])*N
     
    return L(x)*(Y1(x)**(abs(m)/2.))*(-1)**(abs(m)) if m>0 else L(x)*(Y1(x)**(abs(m)/2.))
     
def orbitale(l,ml):
    assert abs(ml)<=l, "ml doit être inférieur à l"
    phi=[-math.pi+i*math.pi/400. for i in range(801)]
    theta=[-math.pi+i*math.pi/400. for i in range(801)]
    TH,PHI=np.meshgrid(theta,phi)
    if ml==0:
        R=[[abs(harmo(l,ml,val))**2 for val in ligne] for ligne in TH]
    elif ml>0:
        R=[[abs(harmo(l,ml,val))**2*math.cos(ml*phi)*math.sqrt(2.) for val,phi in zip(L1,L2)] for L1,L2 in zip(TH,PHI)]
    else:
        R=[[abs(harmo(l,ml,val))**2*math.sin(ml*phi)*math.sqrt(2.) for val,phi in zip(L1,L2)] for L1,L2 in zip(TH,PHI)]
         
    x = [[Rval*math.sin(th)*math.cos(phi) \
    for Rval,th,phi in zip(L1,L2,L3)]\
    for L1,L2,L3 in zip(R,TH,PHI)]
    y=[[Rval*math.sin(th)*math.sin(phi)\
    for Rval,th,phi in zip(L1,L2,L3)]\
    for L1,L2,L3 in zip(R,TH,PHI)]
    z=[[Rval*math.cos(th)\
    for Rval,th in zip(L1,L2)]\
    for L1,L2 in zip(R,TH)]
    fig=plt.figure()
    ax=fig.gca(projection='3d')
    ax.plot_surface(x,y,z,color='w')
    plt.axis('off')
    plt.axis('equal')
    titre='$l$='+str(l)+', '+'$m_l$='+str(ml)
    plt.title(titre,family='serif',fontsize=18,style='italic')
    plt.show()