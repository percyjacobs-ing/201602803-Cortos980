"""
Corto 1
201602803 - Percy Matthew Jacobs Orellana

Usando los ultimos 3 digitos de 201602803 
para realizar las secuencias de Collatz desde 2 hasta 803.

"""

# se define la función que da lugar a la secuencia N de Collatz
def secuenciaCollatz(n):
    res = [n]
    while(n != 1):    # enciclado hasta que n sea igual a 1
        if(n%2 == 0): # si es par hacer n/2
            n = n/2
            res.append(int(n))
        else:         # si es impar hacer 3n+1
            n = 3*n+1
            res.append(int(n))
    return res

# función de escritura en modo write, sobreescribiendo el archivo cada vez que se ejecute el codigo 
def escribir(num):
    n = num
    fileName = 'collatz.txt' # como se tiene un nombre específico no se pide como parámetro de la función
    archivo = open(fileName,'w') # se abre el archivo 
    print('Espere, agregando datos al archivo...')
    for i in range(2,n+1):
        archivo.write(str(secuenciaCollatz(i))+'\n')
    archivo.close() #Siempre cerrar el archivo al finalizar la escritura

# main -- para llamar a las funciones
escribir(803)