# Importando las librerías que se van a utilizar
import numpy as np
import pandas as pd

# Generando la clase elemento
class Elemento:
    def __init__(self, elemento, nombre, z, uma, periodo, grp, c_electron, protones, electrones,neutrones): # Genera el constructor que apsa los valores dentro de la clase
        self.elemento = elemento
        self.nombre = nombre
        self.z = z
        self.uma = uma
        self.periodo = periodo
        self.grp = grp
        self.c_electron = c_electron
        self.protones = protones
        self.electrones = electrones
        self.neutrones = neutrones

    def imprimirElemento(self): # En esta función se imprimen los datos del elemento 
        print("Elemento:", self.elemento)
        print("Nombre:", self.nombre)
        print("Número Atómico:", self.z)
        print("UMA:", self.uma)
        print("Periodo:", self.periodo)
        print("Grupo:", self.grp)
        print("Configuración Electrónica:", self.c_electron)
        print("Protones:", self.protones)
        print("Electrones", self.electrones)
        print("Neutrones:", self.neutrones)
        
    def getElemento(self): # Devuelve el valor del elemento dentro de un diccionario
        return {"Elemento":self.elemento , "Nombre":self.nombre, "Z":self.z, "UMA":self.uma, "Periodo":self.periodo, "Grupo":self.grp, "C_Electronica":self.c_electron,"Protones":self.protones,"Electrones":self.electrones, "Neutrones":self.neutrones}


def imprimirTabla(): # Esta función sirve apra imprimir la tabla periódica
    Tabla = '''
          -----                                                               -----
        1 | H |                                                               |He |
        |---+----                                       --------------------+---|
        2 |Li |Be |                                       | B | C | N | O | F |Ne |
        |---+---|                                       |---+---+---+---+---+---|
        3 |Na |Mg |3B  4B  5B  6B  7B |    8B     |1B  2B |Al |Si | P | S |Cl |Ar |
        |---+---+---------------------------------------+---+---+---+---+---+---|
        4 | K |Ca |Sc |Ti | V |Cr |Mn |Fe |Co |Ni |Cu |Zn |Ga |Ge |As |Se |Br |Kr |
        |---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|
        5 |Rb |Sr | Y |Zr |Nb |Mo |Tc |Ru |Rh |Pd |Ag |Cd |In |Sn |Sb |Te | I |Xe |
        |---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|
        6 |Cs |Ba |LAN|Hf |Ta | W |Re |Os |Ir |Pt |Au |Hg |Tl |Pb |Bi |Po |At |Rn |
        |---+---+---+------------------------------------------------------------
        7 |Fr |Ra |ACT|
        -------------
                    -------------------------------------------------------------
        Lantánidos |La |Ce |Pr |Nd |Pm |Sm |Eu |Gd |Tb |Dy |Ho |Er |Tm |Yb |Lu |
                    |---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|
        Actínidos  |Ac |Th |Pa | U |Np |Pu |Am |Cm |Bk |Cf |Es |Fm |Md |No |Lw |
                    -------------------------------------------------------------
        '''  
    print(Tabla)

# Generando las instancias de cada elemento con sus datos y constantes
# El órden de los argumentos son los siguientes: elemento, nombre, z, uma, periodo, grp, c_electron, protones, electrones, neutrones
H=Elemento("H","Hidrogeno",1,1.007,1,"1"," 1s1",1,1,0.0)
He=Elemento("He","Helio",2,4.002,1,"18"," 1s2",2,2,2.0)
Li=Elemento("Li","Litio",3,6.941,2,"1"," [He] 2s1",3,3,4.0)
Be=Elemento("Be","Berilio",4,9.012,2,"2"," [He] 2s2",4,4,5.0)
B=Elemento("B","Boro",5,10.81,2,"13"," [He] 2s2 2p1 ",5,5,6.0)
C=Elemento("C","Carbono",6,12.01,2,"14"," [He] 2s2 2p2",6,6,6.0)
N=Elemento("N","Nitrogeno",7,14.0,2,"15"," [He] 2s2 2p3",7,7,7.0)
O=Elemento("O","Oxigeno",8,15.99,2,"16"," [He] 2s2 2p4",8,8,8.0)
F=Elemento("F","Fluor",9,18.99,2,"17"," [He] 2s2 2p5 ",9,9,10.0)
Ne=Elemento("Ne","Neon",10,20.17,2,"18"," [He] 2s2 2p6 ",10,10,10.0)
Na=Elemento("Na","Sodio",11,22.98,3,"1"," [Ne] 3s1 ",11,11,12.0)
Mg=Elemento("Mg","Magnesio",12,24.3,3,"2"," [Ne] 3s2 ",12,12,12.0)
Al=Elemento("Al","Aluminio",13,26.98,3,"13"," [Ne] 3s2 3p1 ",13,13,14.0)
Si=Elemento("Si","Silicio",14,28.08,3,"14"," [Ne] 3s2 3p2 ",14,14,14.0)
P=Elemento("P","Fosforo",15,30.97,3,"15"," [Ne] 3s2 3p3 ",15,15,16.0)
S=Elemento("S","Azufre",16,32.06,3,"16"," [Ne] 3s2 3p4 ",16,16,16.0)
Cl=Elemento("Cl","Cloro",17,35.45,3,"17"," [Ne] 3s2 3p5 ",17,17,18.0)
Ar=Elemento("Ar","Argon",18,39.94,3,"18"," [Ne] 3s2 3p6 ",18,18,22.0)
K=Elemento("K","Potasio",19,39.09,4,"1"," [Ar] 4s1 ",19,19,20.0)
Ca=Elemento("Ca","Calcio",20,40.07,4,"2"," [Ar] 4s1 ",20,20,20.0)
Sc=Elemento("Sc","Escandio",21,44.95,4,"3"," [Ar] 3d1 4s2 ",21,21,24.0)
Ti=Elemento("Ti","Titanio",22,47.86,4,"4"," [Ar] 3d2 4s2 ",22,22,26.0)
Va=Elemento("Va","Vanadio",23,50.94,4,"5"," [Ar] 3d3 4s2 ",23,23,28.0)
Cr=Elemento("Cr","Cromo",24,51.99,4,"6"," [Ar] 3d5 4s1 ",24,24,28.0)
Mn=Elemento("Mn","Manganeso",25,54.93,4,"7"," [Ar] 3d5 4s2 ",25,25,30.0)
Fe=Elemento("Fe","Hierro",26,55.84,4,"8"," [Ar] 3d6 4s2 ",26,26,30.0)
Co=Elemento("Co","Cobalto",27,58.93,4,"9"," [Ar] 3d7 4s2 ",27,27,32.0)
Ni=Elemento("Ni","Niquel",28,58.69,4,"10"," [Ar] 3d8 4s2 ",28,28,31.0)
Cu=Elemento("Cu","Cobre",29,63.54,4,"11"," [Ar] 3d10 4s1 ",29,29,35.0)
Zn=Elemento("Zn","Zinc",30,65.4,4,"12"," [Ar] 3d10 4s2 ",30,30,35.0)
Ga=Elemento("Ga","Galio",31,69.72,4,"13"," [Ar] 3d10 4s2 4p1 ",31,31,39.0)
Ge=Elemento("Ge","Germanio",32,72.64,4,"14"," [Ar] 3d10 4s2 4p2 ",32,32,41.0)
As=Elemento("As","Arsenico",33,74.92,4,"15"," [Ar] 3d10 4s2 4p3 ",33,33,42.0)
Se=Elemento("Se","Selenio",34,78.96,4,"16"," [Ar] 3d10 4s2 4p4 ",34,34,45.0)
Br=Elemento("Br","Bromo",35,79.9,4,"17"," [Ar] 3d10 4s2 4p5 ",35,35,45.0)
Kr=Elemento("Kr","Kripton",36,83.79,4,"18"," [Ar] 3d10 4s2 4p6 ",36,36,48.0)
Rb=Elemento("Rb","Rubidio",37,85.46,5,"1"," [Kr] 5s1 ",37,37,48.0)
Sr=Elemento("Sr","Estroncio",38,87.62,5,"2"," [Kr] 5s2 ",38,38,50.0)
Y=Elemento("Y","Itrio",39,88.9,5,"3"," [Kr] 4d1 5s2 ",39,39,50.0)
Zr=Elemento("Zr","Circonio",40,91.22,5,"4"," [Kr] 4d2 5s2 ",40,40,51.0)
Nb=Elemento("Nb","Niobio",41,92.9,5,"5"," [Kr] 4d4 5s1 ",41,41,52.0)
Mo=Elemento("Mo","Molibdeno",42,95.94,5,"6"," [Kr] 4d5 5s1 ",42,42,54.0)
Tc=Elemento("Tc","Tecnecio",43,98.9,5,"7"," [Kr] 4d6 5s1 ",43,43,56.0)
Ru=Elemento("Ru","Rutenio",44,101.0,5,"8"," [Kr] 4d7 5s1 ",44,44,57.0)
Rh=Elemento("Rh","Rodio",45,102.9,5,"9"," [Kr] 4d8 5s1 ",45,45,58.0)
Pd=Elemento("Pd","Paladio",46,106.4,5,"10"," [Kr] 4d10 ",46,46,60.0)
Ag=Elemento("Ag","Plata",47,107.8,5,"11"," [Kr] 4d10 5s1 ",47,47,61.0)
Cd=Elemento("Cd","Cadmio",48,112.4,5,"12"," [Kr] 4d10 5s2 ",48,48,64.0)
In=Elemento("In","Indio",49,114.8,5,"13"," [Kr] 4d10 5s2 5p1 ",49,49,66.0)
Sn=Elemento("Sn","Estano",50,118.7,5,"14"," [Kr] 4d10 5s2 5p2 ",50,50,69.0)
Sb=Elemento("Sb","Antimonio",51,121.7,5,"15"," [Kr] 4d10 5s2 5p3 ",51,51,71.0)
Te=Elemento("Te","Teluro",52,127.6,5,"16"," [Kr] 4d10 5s2 5p4 ",52,52,76.0)
I=Elemento("I","Yodo",53,126.9,5,"17"," [Kr] 4d10 5s2 5p5 ",53,53,74.0)
Xe=Elemento("Xe","Xenon",54,131.2,5,"18"," [Kr] 4d10 5s2 5p6 ",54,54,77.0)
Cs=Elemento("Cs","Cesio",55,132.9,6,"1"," [Xe] 6s1",55,55,78.0)
Ba=Elemento("Ba","Bario",56,137.3,6,"2"," [Xe] 6s2",56,56,81.0)
La=Elemento("La","Lantano",57,138.9,6,"-"," [Xe] 5d1 6s2",57,57,82.0)
Ce=Elemento("Ce","Cerio",58,140.1,6,"-"," [Xe] 4f2 6s2",58,58,82.0)
Pr=Elemento("Pr","Praseodimio",59,140.9,6,"-"," [Xe] 4f3 6s2",59,59,82.0)
Nd=Elemento("Nd","Neodimio",60,144.2,6,"-"," [Xe] 4f4 6s2",60,60,84.0)
Pm=Elemento("Pm","Prometio",61,146.9,6,"-"," [Xe] 4f5 6s2",61,61,86.0)
Sm=Elemento("Sm","Samario",62,150.3,6,"-"," [Xe] 4f6 6s2",62,62,88.0)
Eu=Elemento("Eu","Europio",63,151.9,6,"-"," [Xe] 4f7 6s2",63,63,89.0)
Gd=Elemento("Gd","Gadolin",64,157.2,6,"-"," [Xe] 4f7 6s2",64,64,93.0)
Tb=Elemento("Tb","Terbio",65,158.9,6,"-"," [Xe] 4f9 6s2",65,65,94.0)
Dy=Elemento("Dy","Disprosio",66,162.5,6,"-"," [Xe] 4f10 6s2",66,66,96.0)
Ho=Elemento("Ho","Holmio",67,164.9,6,"-"," [Xe] 4f11 6s2",67,67,98.0)
Er=Elemento("Er","Erbio",68,167.2,6,"-"," [Xe] 4f12 6s2",68,68,99.0)
Tm=Elemento("Tm","Tulio",69,168.9,6,"-"," [Xe] 4f13 6s2",69,69,100.0)
Yb=Elemento("Yb","Iterbio",70,173.0,6,"-"," [Xe] 4f14 6s2",70,70,103.0)
Lu=Elemento("Lu","Lutecio",71,174.9,6,"3"," [Xe] 4f14 5d1 6s2",71,71,104.0)
Hf=Elemento("Hf","Hafnio",72,178.4,6,"4"," [Xe] 4f14 5d2 6s2",72,72,106.0)
Ta=Elemento("Ta","Tantalio",73,180.9,6,"5"," [Xe] 4f14 5d3 6s2",73,73,108.0)
W=Elemento("W","Wolframio",74,183.8,6,"6"," [Xe] 4f14 5d4 6s2",74,74,110.0)
Re=Elemento("Re","Renio",75,186.2,6,"7"," [Xe] 4f14 5d5 6s2",75,75,111.0)
Os=Elemento("Os","Osmio",76,190.2,6,"8"," [Xe] 4f14 5d6 6s2",76,76,114.0)
Ir=Elemento("Ir","Iridio",77,192.2,6,"9"," [Xe] 4f14 5d7 6s2",77,77,115.0)
Pt=Elemento("Pt","Platino",78,195.0,6,"10"," [Xe] 4f14 5d9 6s1",78,78,117.0)
Au=Elemento("Au","Oro",79,196.9,6,"11"," [Xe] 4f14 5d10 6s1",79,79,118.0)
Hg=Elemento("Hg","Mercurio",80,200.5,6,"12"," [Xe] 4f14 5d10 6s2",80,80,120.0)
Tl=Elemento("Tl","Talio",81,204.3,6,"13"," [Xe] 4f14 5d10 6s2 6p1",81,81,123.0)
Pb=Elemento("Pb","Plomo",82,207.2,6,"14"," [Xe] 4f14 5d10 6s2 6p2",82,82,125.0)
Bi=Elemento("Bi","Bismuto",83,208.9,6,"15"," [Xe] 4f14 5d10 6s2 6p3",83,83,126.0)
Po=Elemento("Po","Polonio",84,208.9,6,"16"," [Xe] 4f14 5d10 6s2 6p4",84,84,125.0)
At=Elemento("At","Astato",85,209.9,6,"17"," [Xe] 4f14 5d10 6s2 6p5",85,85,125.0)
Rn=Elemento("Rn","Radon",86,222.0,6,"18"," [Xe] 4f14 5d10 6s2 6p6",86,86,136.0)
Fr=Elemento("Fr","Francio",87,223.0,7,"1"," [Rn] 7s1 ",87,87,136.0)
Ra=Elemento("Ra","Radio",88,226.0,7,"2"," [Rn] 7s2 ",88,88,138.0)
Ac=Elemento("Ac","Actinio",89,227.0,7,"-"," [Rn] 6d1 7s2 ",89,89,138.0)
Th=Elemento("Th","Torio",90,232.0,7,"-"," [Rn] 6d2 7s2 ",90,90,142.0)
Pa=Elemento("Pa","Protactinio",91,231.0,7,"-"," [Rn] 5f2 6d1 7s2 ",91,91,140.0)
U=Elemento("U","Uranio",92,238.0,7,"-"," [Rn] 5f3 6d1 7s2 ",92,92,146.0)
Np=Elemento("Np","Neptunio",93,237.0,7,"-"," [Rn] 5f4 6d1 7s2 ",93,93,144.0)
Pu=Elemento("Pu","Plutonio",94,244.0,7,"-"," [Rn] 5f6 7s2 ",94,94,150.0)
Am=Elemento("Am","Americio",95,243.0,7,"-"," [Rn] 5f7 7s2 ",95,95,148.0)
Cm=Elemento("Cm","Curio",96,247.0,7,"-"," [Rn] 5f7 6d1 7s2 ",96,96,151.0)
Bk=Elemento("Bk","Berkelio",97,247.0,7,"-"," [Rn] 5f9 7s2 ",97,97,150.0)
Cf=Elemento("Cf","Californio",98,251.0,7,"-"," [Rn] 5f10 7s2 ",98,98,153.0)
Es=Elemento("Es","Einstenio",99,252.0,7,"-"," [Rn] 5f11 7s2 ",99,99,153.0)
Fm=Elemento("Fm","Fermio",100,257.0,7,"-"," [Rn] 5f12 7s2 ",100,100,157.0)
Md=Elemento("Md","Mendelevio",101,258.0,7,"-"," [Rn] 5f13 7s2 ",101,101,157.0)
No=Elemento("No","Nobelio",102,259.1,7,"-"," [Rn] 5f14 7s2 ",102,102,157.0)
Lr=Elemento("Lr","Laurencio",103,260.1,7,"3"," [Rn] 5f14 6d1 7s2",103,103,157.0)
Rf=Elemento("Rf","Rutherfordio",104,261.1,7,"4"," [Rn] 5f14 6d2 7s2",104,104,157.0)
Db=Elemento("Db","Dubnio",105,262.1,7,"5"," [Rn] 5f14 6d3 7s2",105,105,157.0)
Sg=Elemento("Sg","Seaborgio",106,263.1,7,"6"," [Rn] 5f14 6d4 7s2",106,106,157.0)
Bh=Elemento("Bh","Bohrio",107,262.1,7,"7"," [Rn] 5f14 6d5 7s2",107,107,155.0)
Hs=Elemento("Hs","Hassio",108,265.0,7,"8"," [Rn] 5f14 6d6 7s2",108,108,157.0)
Mt=Elemento("Mt","Meitnerio",109,266.0,7,"9"," [Rn] 5f14 6d7 7s2",109,109,157.0)
Ds=Elemento("Ds","Darmstadtio",110,269.0,7,"10"," [Rn] 5f14 6d9 7s1",110,110,159.0)
Rg=Elemento("Rg","Roentgenio",111,272.0,7,"11"," [Rn] 5f14 6d10 7s1",111,111,161.0)
Cn=Elemento("Cn","Copernicio",112,285.0,7,"12"," [Rn] 5f14 6d10 7s2",112,112,173.0)
Nh=Elemento("Nh","Nihonio",113,284.0,7,"13"," [Rn] 5f14 6d10 7s2 7p1",113,113,171.0)
Fl=Elemento("Fl","Flerovio",114,289.0,7,"14"," [Rn] 5f14 6d10 7s2 7p2",114,114,175.0)
Mc=Elemento("Mc","Moscovio",115,288.0,7,"15"," [Rn] 5f14 6d10 7s2 7p3",115,115,173.0)
Lv=Elemento("Lv","Livermorio",116,290.0,7,"16"," [Rn] 5f14 6d10 7s2 7p4",116,116,174.0)
Ts=Elemento("Ts","Tenesino",117,0,7,"17"," [Rn] 5f14 6d10 7s2 7p5",117,117,0)
Og=Elemento("Og","Oganeson",118,294.0,7,"18"," [Rn] 5f14 6d10 7s2 7p6",118,118,176.0)