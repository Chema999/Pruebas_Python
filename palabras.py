""" # -*- coding: utf-8 -*-"""
# -*- coding: iso-8859-1 -*-


class Palabras(object):
    """
        Clase para contabilizar el número de apariciones que tiene las palabras
        en una frase o en un texto.
    """

    def __init__(self):
        self.__diccionario = {}
        self.__simbolos = (",", ".", "!", "¡", "¿", "?", "(", ")", "\"", "&")

    """
        Añade palabra al diccionario, para contabilizar el número de apariciones.
    """
    def agregar(self, palabra):
        if palabra in self.__diccionario:
            print("Encontrada")
            cont = self.__diccionario[palabra]
            cont = cont + 1
            self.__diccionario.update({palabra: cont})
        else:
            print("Palabra nueva")
            self.__diccionario.setdefault(palabra, 1)

    """
        Muestra el número de palabras y lista el contenido del diccionario de palabras
    """
    def informacion(self):
        print("Número de palabras:", self.__diccionario.__len__())
        print("Contenido del diccionario:")

        for pal in self.__diccionario:
            print(pal, "->", self.__diccionario[pal])

    """
        Devuelve el número de veces que aparece palabra
    """
    def veces(self, palabra):
        cont = 0
        if palabra in self.__diccionario:
            cont = self.__diccionario[palabra]
        return cont

    """
        Vacía el diccionario
    """
    def vaciar(self):
        self.__diccionario.clear()

    """
        Procesa la frase para ver qué palabras y cuántas veces aparece
    """
    def procesarFrase(self, frase):
        for simbolo in self.__simbolos:
            frase = frase.replace(simbolo, " ")
        lista = frase.split(" ")
        for pal in lista:
            pal2 = pal.strip()
            if pal2 != "":
                self.agregar(pal2.strip())

    """
        Procesa el fichero para ver qué palabras y cuántas veces aparece
    """
    def procesarFichero(self, nomFich):
        try:
            f = open(nomFich, "r")
            try:
                linea = f.readline()
                while linea:
                    self.procesarFrase(linea)
                    linea = f.readline()
            finally:
                f.close()
        except IOError:
            print("El fichero", nomFich, "no existe")

    """
        Guarda el diccionario con nombre nomFich, con las palabras que cumplan las condiciones
        de longitud mínima minLong y que aparezcan como mínimo minCont
    """
    def guardar(self, nomFich, minLong, minCont):
        try:
            print("Creando fichero", nomFich)
            f = open(nomFich, "w")
            try:
                for pal in self.__diccionario:
                    if (self.__diccionario[pal] >= minCont) and (len(pal) >= minLong):
                        buffer = pal + "," + str(self.__diccionario[pal])
                        print("Escribiendo:", buffer)
                        buffer = buffer + "\n"
                        f.writelines(buffer)
            finally:
                f.close()
        except IOError:
            print("El fichero", nomFich, "no se puede crear")


if __name__ == "__main__":
    palabras = Palabras()
    # palabras.agregar("hola")
    # palabras.procesarFrase("Esto es una línea de prueba")
    # palabras.procesarFrase("Esto es otra línea de prueba")
    palabras.procesarFichero("texto.txt")
    print("La palabra password aparece %s veces" % palabras.veces("password"))
    palabras.guardar("diccionario.txt", 5, 3)
    palabras.vaciar()
    # palabras.informacion()
