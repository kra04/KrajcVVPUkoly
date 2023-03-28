# Výpočet druhé odmocniny pomocí prostých iterací
def druha_odmocnina(cislo, pocet_iteraci):
    hodnota = cislo #odmocnovane cislo jako nulty clen iteracni posloupnosti
    for j in range(pocet_iteraci): #cyklus zajistujici vypocet odmocniny jako pevneho bodu kontraktivniho zobrazeni
        hodnota = (cislo/hodnota+hodnota)/2
    return hodnota
# Výpočet obsahu vepsaných úhelníků
def obsaheuler(pocet_iteraci):
    strana = 1  
    vyska =  druha_odmocnina(3, 100)/2 #vyska v sestiuhelniku
    for j in range(pocet_iteraci):
        strana = druha_odmocnina((strana/2)**2+(1-vyska)**2, 100) #vypocet zakladny
        vyska =  druha_odmocnina(1-(strana/2)**2, 100)
    return 6*(2**pocet_iteraci)*strana*vyska/2 #funkce vraci obsah vepsaneho 6*2**pocet_iteraci uhelnika
# Součet řady vedoucí k aproximaci pí
def obsahnewton(pocet_clenu):
    a_i=1/16 #stanoveni prvniho clenu
    soucet=(1/3)*a_i #soucet pro i=1
    for i in range(2,pocet_clenu+1):  
        a_i=(1/4)*a_i*(2*i-3)/(2*i) #vypocet nasledujiciho koeficientu
        soucet += (1/(2*i+1))*a_i   #dalsi scitanec k souctu rady
    return 12*(1/2-druha_odmocnina(3,1000)/8-soucet) #funkce vraci aproximaci cisla pi pomoci n clenu rady
