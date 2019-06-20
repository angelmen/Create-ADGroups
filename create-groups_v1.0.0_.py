########################################################################
#                                                                      #
#                             WhiteAngel                               #
#                                                                      #
#                                                                      #
#                       Creado por Angel Mendez                        #
#                           20/Junio/2019                              #
#                                                                      #
#             Con el proposito de ahorrarme muchos clics!!!            #
#                         All rights reserved                          #
#     Don't copy or share this script without asking for permision     #
#                                                                      #
########################################################################



#Programa que crea grupos de AD



import os, subprocess, sys;

#Para limpiar la consola
def clear():
    os.system("cls");

#En caso de que desee crear mas de un grupo
def repetir():
    clear()
    repetir = input("Desea crear otro grupo [S:n]: ")
    repetir = repetir.upper()
    if repetir == "S":
        main()
    elif repetir == "N":
        sys.exit()
    elif repetir == "":
        main()
    else:
        input("Opcion invalida!!")
        repetir()

def main():
    clear()
    print("Vamos a crear un grupo!!")

    nombre = input("Ingrese el nombre del grupo: ")
    scope = input("Seleccione el tipo de SCOPE [DomainLocal | *Global* | Universal]: ")
    category = input("Seleccione la cetegoria del grupo[Distribution | *Security*]: ")
    path = input("Ingrese la ubicacion del grupo: ")

    #Crear script de PowerShell
    psf = open("./crear.ps1", "w+")
    psf.write("Import-Module ActiveDirectory; New-ADGroup -name %s -GroupScope %s -DisplayName %s -GroupCategory %s -path \"%s\"; Pause;"
              %(nombre, scope or "Global", nombre, category or "Security", path + ",dc=itla,dc=local" )) #Puedes cambiar ",dc=itla,dc=local" por ",dc={NombreDelDominio}, dc={TopLevelDomainDelDominio}"
    psf.close()
    #Ejecutar Script de PowerShell
    ejecutar = subprocess.Popen(["powershell.exe", "./crear.ps1"])
    ejecutar.communicate()
    repetir()

#Inicio del programa
main()
