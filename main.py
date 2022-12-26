import random
from colorama import Fore, init
from datetime import datetime

#Creando variables para las validaciones
cdia=input("digite su CDIA: ")
usuario=(input('Digite su alias: '))
cdia_upper=cdia.upper()
repeticion=cdia_upper.count("K")
posicion= (cdia[5])
poci1=(cdia[0])
poci10=(cdia[9])
MAS=cdia.find("+")
IGUAL=cdia.find("=")
CARACTER=cdia.find("&")
INTERROGANTE=cdia.find("?")


import sys
#Validacion del CDIA(Id) ingresado
def juego():
  tieneCaracter=0
  if len(cdia_upper) > 11:
    print("excede el limite de caracteres")
    sys.exit("CDIA invalido")
  if type(cdia)==str:
    print("es str")
  else:
    print("Solo caracteres")
    sys.exit("CDIA invalido")
  if (posicion=="@"):
    print("Si tiene el @")
  else:
    print("No tiene el @")
    sys.exit("CDIA invalido")
  
  if (poci1 != poci10):
    print("esta bien")
  else:
    print("cambie su cdia")
    sys.exit("CDIA invalido")
  if (repeticion>3):
    print("excede el limite de uso de la letra k ")
    sys.exit("CDIA invalido")
  else:
    print("es valido")

  if ( MAS >= 0):
    print("tiene el +")
  else:
    print("no tiene el +")
    sys.exit("CDIA invalido")
  if ( IGUAL > 0):
    tieneCaracter = 1
    print("Tiene el =")
  if ( CARACTER > 0 ):
    tieneCaracter = 1
    print("tiene el &")
  if (INTERROGANTE > 0):
    tieneCaracter = 1
    print("tiene el ?")
  if tieneCaracter < 1:
    print("Le hace falta un caracter")
    sys.exit("CDIA invalido")


juego()
#Validar que el CDIA ingresado este registrado
import Repository as asc
def leer_cdia():
  se_encuentra=asc.buscar_cdia(cdia)
  if (se_encuentra==0):
    print("Su CDIA no esta registrado")
   
  else:
    print("Su CDIA ya esta resgistrado")
    sys.exit("Su CDIA ya se encuentra registrado")
   

        

leer_cdia()
#Calculando la edad del usuario teniendo en cuenta su fecha de nacimiento
def calcular_edad():
    import datetime
    from datetime import date
    hoy=datetime.date.today()
    
    anioc=int(input("\nsu año de nacimiento: "))
    mesc=int(input("su mes de nacimiento: "))
    diac=int(input("su dia de nacimiento: "))
    fechaAct=date.today()
    
    calculando = (fechaAct.year) - (anioc)
    #Para saber si ya cumplio anos 
    calculando2 = calculando - 1
    edadFinal = 0
    if mesc > fechaAct.month:
      edadFinal = calculando2
    elif mesc == fechaAct.month:
       if diac >= fechaAct.day:
           edadFinal = calculando2
       else:
            edadFinal = calculando
    else: 
          edadFinal = calculando
        
    
    return edadFinal
#Definiendole la categoria de nivel que tiene
def mundo(respuesta1, edad, nivel):
   if edad>11 and edad<21:
    if respuesta1=="NO":
       print("Su mundo es el 1")
    elif respuesta1=="SI":
      if nivel < 50:
        print("Su mundo es el 2")
      elif nivel >= 50:
        print("Su mundo es el 3")
        
   if  edad>20:
    if respuesta1=="NO":
       print("Su mundo es el 4")
    elif respuesta1=="SI":
      if nivel < 50:
        print("Su mundo es el 5")
      elif nivel >= 50:
        print("Su mundo es el 6")
        


def remover_espacio(cadena):
  #Quitando espacios
  return cadena.replace(' ','')
        


#Asignando los respectivos niveles teneindo en cuenta la edad y la experienecia
def edades():
  edad=calcular_edad()
  if edad>=12:
      #alias=input("Alias del jugador: ")
      if len(remover_espacio(usuario)) > 4:
        experiencia=input("ya has jugado WorldCraft ASCII? (Si, No): ")
      else:
        print("No cumple con el limite minimo de caracteres")
        sys.exit("Alias invalido")
      respuesta1_upper= experiencia.upper()
    
      nivel=0
      if respuesta1_upper=="SI":
        nivel=int(input("¿Hasta que nivel llegaste? (el nivel va desde 1 hasta 100): "))
        nivel2 = nivel+2 
          
      if edad<16 and respuesta1_upper=="NO":
        print("Sera dirigido al nivel 2 del juego")
      elif edad<16 and respuesta1_upper=="SI":
        print("Sera dirigido al nivel", nivel)
      elif edad>=16 and respuesta1_upper=="SI":
          print("Sera dirigido al nivel", nivel2)
      elif edad>=16 and respuesta1_upper=="NO":
          print("Sera dirigido al nivel 1")
  
      mundo(respuesta1_upper, edad, nivel)
   #Descartando al usuario por su edad 
  else:
    print("No tiene edad suficiente")
    sys.exit("No posee con la edad necesaria")
edades()
    

input()

creaturasp = int(input('Numero de creaturas pasivas: '))
creaturash = int(input('Numero de creaturas Hostiles: '))
def creaturas_bd(tipo):
    pasivos = {
        'P': 'Poseidón',
        'D': 'Hades',
        'R': 'Hermes',
        'F': 'Hefesto',
        'L': 'Apolo',
        'I': 'Afrodita',
        'G': 'Gera'
      
    }
    hostiles = {
        'Z': 'Zeus',
        'A': 'Atenea',
        'H': 'Herav',
        'U': 'Urano',
        'C': 'Cronos',
        'N': 'Anteo',
        'T': 'Tántalo'
    }
    if tipo == 'p':
        return pasivos
    if tipo == 'h':
        return hostiles


def generador_criaturas(hostil, pasiva):
    c_pasiva = list(creaturas_bd('p').keys())
    c_hostiles = list(creaturas_bd('h').keys())
    pasivos = []
    hostiles = []
    if hostil + pasiva > 50:
        return False
    else:
        cont = 0
        cont2 = 0
        while pasiva > 0:
            pasivos.insert(cont, random.choice(c_pasiva))
            cont += 1
            pasiva -= 1

        while hostil > 0:
            hostiles.insert(cont2, random.choice(c_hostiles))
            cont2 += 1
            hostil -= 1

        return [pasivos, hostiles]

jugador = {
        'Tipo': 'Jugador',
        'Alias': usuario,
        'Fila': random.randint(0, 32),
        'Columna': random.randint(0, 32),
        'Fecha': datetime.now(),
        'Vida': 10,
        'Simbolo': '%'      
}

def creatura_info(tipo, nombre, simbolo, fila, columna, fecha, ):
    creatura = {
        'Tipo': tipo, 
        'Nombre': nombre,
        'Simbolo': simbolo,
        'Fila': fila,
        'Columna': columna,
        'Fecha': fecha
    }
    return creatura


def creaturas_activas(creaturas):
    creaturasDBP = creaturas_bd('p') 
    creaturasDBH = creaturas_bd('h') 
    
    pasivos = creaturas[0]
    hostiles = creaturas[1]
    
    creaturas = []
    

    for i in range(0, len(pasivos)):
        codigo = dict(filter(lambda x: x[0] == pasivos[i], creaturasDBP.items()))

        cre = creatura_info('Pasivo', tuple(codigo.values()), tuple(codigo.keys()), random.randint(0, 32), random.randint(0, 32), datetime.now())
       
        creaturas.append(cre)
    for i in range(0, len(hostiles)):
        codigo = dict(filter(lambda x: x[0] == hostiles[i], creaturasDBH.items()))
        cre = creatura_info('Hostil', tuple(codigo.values()), tuple(codigo.keys()),       random.randint(0, 32),  random.randint(0, 32), datetime.now())
                            
        creaturas.append(cre)
   

    
    return tuple(creaturas)


def insertar_creaturas(matriz, creatura, simbolo, tipo, ):
    for i in range(0, 32):
        for j in range(0, 32):
            if creatura == (i, j):
                if tipo == 'Pasivo':
                    matriz[i][j] = Fore.BLUE + f'{simbolo}'
                elif tipo == 'Jugador':
                     matriz[i][j] = Fore.GREEN + f'{simbolo}'  
                   
                else:
                    matriz[i][j] = Fore.RED + f'{simbolo}'



  
      
  


jugador = {
        'Tipo': 'Jugador',
        'Alias': usuario,
        'Fila': random.randint(0, 32),
        'Columna': random.randint(0, 32),
        'Fecha': datetime.now(),
        'Vida': 10,
        'Simbolo': '%'
    }
   
print('---------------------------------------') 
print( f'Tipo {jugador["Tipo"]}\n'
                        f'Alias {jugador["Alias"]}\n'
                        f'Cordenadas ({jugador["Fila"]},{jugador["Columna"]})\n'
                        f'Fecha espauwn {jugador["Fecha"]}\n'
                        f'Vida {jugador["Vida"]} Corazones')  



  
def cordenadas_aleatorias():
    filas = [[random.choice([i for i in range(0, 10)]) for i in range(0, 4)] for i in range(0, 4)]
    return filas


 

def creacion_mundo(creaturas_generadas):
    init()
    entidades = creaturas_activas(creaturas_generadas)
    cordenadas = []
    
    for i in entidades:
        print(f'{i["Tipo"]} {i["Nombre"][0]}  {i["Simbolo"][0]}  ({i["Fila"]},{i["Columna"]}, {i["Fecha"]})')
        cordenadas.append(((i["Fila"], i["Columna"]), i["Simbolo"][0], i["Tipo"]))
 
       
         
       

    
    filas = cordenadas_aleatorias()[0]
    columnas = cordenadas_aleatorias()[1]
    anchos = cordenadas_aleatorias()[2]
    largos = cordenadas_aleatorias()[3]
    
   

   
    matriz = []
    cont = 0
    for i in range(0, 32):
        matriz.append([0] * 32)
        for j in range(0, 32):

            if filas[0] <= i <= filas[0] + (largos[0] - 1) and columnas[0] <= j <= columnas[0] + (anchos[0] - 1):
                matriz[i][j] = Fore.YELLOW + '#'
            elif filas[1] <= i <= filas[1] + (largos[1] - 1) and columnas[1] <= j <= columnas[1] + (anchos[1] - 1):
                matriz[i][j] = Fore.YELLOW + '#'
            elif filas[2] <= i <= filas[2] + (largos[2] - 1) and columnas[2] <= j <= columnas[2] + (anchos[2] - 1):
                matriz[i][j] = Fore.YELLOW + '#'
            elif filas[3] <= i <= filas[3] + (largos[3] - 1) and columnas[3] <= j <= columnas[3] + (anchos[3] - 1):
                matriz[i][j] = Fore.YELLOW + '#'
            else:
                matriz[i][j] = Fore.YELLOW + '-'

    for i in range(0, len(cordenadas)):
        insertar_creaturas(matriz, cordenadas[i][0], cordenadas[i][1], cordenadas[i][2])
          
 


    for fila in matriz:
        for valor in fila:
            print(valor, end="  ")
        print()
      


print('---------------------------------------')        
print("Hay",creaturasp + creaturash,"creaturas" )
print('Hay',creaturasp,'creaturas Pasivas')
print('Hay',creaturash,'creaturas Hostiles')
print('---------------------------------------') 

 
if not generador_criaturas(creaturash, creaturasp, ):
  print('No se puede crear mas de 50 creaturas\n')
else:
  creacion_mundo(generador_criaturas(creaturash, creaturasp))
 