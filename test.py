from libs import materia
from libs import elementos

##############ELEMENTOS#########################################

# print(elementos.He.nombre)

# elementos.imprimirTabla()
#################MATERIA#########################

# print(materia._umaelemento('He'))

# print(materia.umacompuesto('H2 O'))

# print(materia.umapercentual('H2 O'))

# print(materia.umapercentual('O'))

# print(materia.gmol(18.01528,'H2 O'))
# print(materia.molg(1, 'H2 O'))

###############gases#######################

from libs import gases


#print(gases.BoyleP2(1.5,3,2.5))
#print(gases.BoyleV2(4.2,760,415,unidadespres = "mmhg"))
#print(gases.BoyleV1(3.4,5,2.5))
#print(gases.LussacT2(25, 970, 760, unidadespres = 'mmhg', unidadestemp = 'C'))



print(gases.LussacP2(45, 125, 460, unidadespres = 'mmhg', unidadestemp = 'C'))

