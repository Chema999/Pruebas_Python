# -*- coding: iso-8859-1 -*-

import argparse


class GeneradorDic:
    """
        Generador de diccionario a partir de una palabra o fichero con palabras, haciendo sustituciones
        como a por 4, o s por $.
    """

    def __init__(self, args):
        self.__args = args
        self.lista = []
        self.extFDest = ".dic"
        self.__DEBUG = False

    def __str__(self):
        cad = ""
        for p in self.lista:
            cad = cad + p + "\n"
        return cad

    """
        Procesa la palabra, teniendo en cuenta los parámetros pasados en línea de comandos """

    def procesoPalabra2(self, palabra):
        if self.__args.voc_num:
            print("Procesando vocales -> números")
            self.vocales2Numeros(palabra)
            print("Procesando consonantes -> símbolos")
            self.consonantes2Simbolos(palabra)

    """
        Convierte letras a números """

    def procesoPalabraNumeros2(self, palabra):
        longitud = len(palabra)
        # Nota: Las cadenas son inmutables
        nuevaPal = ""
        for i in range(0, longitud):
            if palabra[i] == 'a':
                nuevaPal = nuevaPal + '4'
            elif palabra[i] == 'e':
                nuevaPal = nuevaPal + '3'
            elif palabra[i] == 'o':
                nuevaPal = nuevaPal + '0'
            elif palabra[i] == 'i':
                nuevaPal = nuevaPal + '1'
            else:
                nuevaPal = nuevaPal + palabra[i]
        self.lista.append(nuevaPal)

    """
        Convierte algunos caracteres a un equivalente (1 -> ! s -> $) """

    def procesoPalabraSimbolos2(self, palabra):
        longitud = len(palabra)
        # Nota: Las cadenas son inmutables
        nuevaPal = ""
        for i in range(0, longitud):
            if palabra[i] == 'l':
                nuevaPal = nuevaPal + '!'
            elif palabra[i] == 'c':
                nuevaPal = nuevaPal + '('
            elif palabra[i] == 's':
                nuevaPal = nuevaPal + '$'
            elif palabra[i] == 'o':
                nuevaPal = nuevaPal + '*'
            else:
                nuevaPal = nuevaPal + palabra[i]
        self.lista.append(nuevaPal)

    """
        Convierte caracteres a números y símbolos correspondientes """

    def procesoPalabraNumerosSimbolos2(self, palabra):
        longitud = len(palabra)
        # Nota: Las cadenas son inmutables
        nuevaPal = ""
        for i in range(0, longitud):
            if palabra[i] == 'a':
                nuevaPal = nuevaPal + '4'
            elif palabra[i] == 'e':
                nuevaPal = nuevaPal + '3'
            elif palabra[i] == 'o':
                nuevaPal = nuevaPal + '0'
            elif palabra[i] == 'i':
                nuevaPal = nuevaPal + '1'
            elif palabra[i] == 'l':
                nuevaPal = nuevaPal + '!'
            elif palabra[i] == 'c':
                nuevaPal = nuevaPal + '('
            elif palabra[i] == 's':
                nuevaPal = nuevaPal + '$'
            elif palabra[i] == 'o':
                nuevaPal = nuevaPal + '*'
            else:
                nuevaPal = nuevaPal + palabra[i]
        self.lista.append(nuevaPal)

    """
        Aplica las transformaciones """

    def procesar(self):
        self.procesarPalabra(self.__args.pal)

    """
        Aplica las transformaciones de caracteres que se han indicado en los parámetros """

    def procesarPalabra(self, pal):
        if self.__DEBUG:
            print("Procesando palabra", pal)
        if self.__args.voc_num or self.__args.todos:
            genDic.procesoPalabraNumeros2(pal)
        if self.__args.cons_simb or self.__args.todos:
            genDic.procesoPalabraSimbolos2(pal)
        if self.__args.voc_simb or self.__args.todos:
            genDic.procesoPalabraNumerosSimbolos2(pal)

    """
        Aplica las transformaciones de caracteres que se han indicado en los parámetros a cada línea de
        texto del fichero pasado en el parámetro """
    def procesarFichero(self):
        try:
            fOrig = open(self.__args.f_orig, "r")
            # Leo el fichero y creo la lista
            buffer = fOrig.readline()
            while buffer:
                buffer = buffer.replace("\n", "")
                self.procesarPalabra(buffer)
                buffer = fOrig.readline()
            fOrig.close()

            try:
                nomFichDest = self.__args.f_orig + self.extFDest
                fDest = open(nomFichDest, "w")
                for i in range(0, len(self.lista)):
                    buffer = self.lista[i] + "\n"
                    fDest.write(buffer)
                fDest.close()
                print("Fichero", nomFichDest, "creado")
            except IOError:
                print("No se puede crear el fichero destino", nomFichDest)
        except IOError:
            print("No se puede abrir", args.f_orig)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generador de diccionario",
                                     epilog="Genera un fichero de palabras convirtiendo letras por números y símbolos")
    parser.add_argument("-p", "--palabra", dest="pal",
                        help="Palabra a partir de la que se generarán nuevas palabras")
    parser.add_argument("-i", "--fichero_orig", dest="f_orig",
                        help="Nombre del fichero que contiene las palabras originales, una por línea")
    parser.add_argument("-vn", "--vocal_numero", dest="voc_num", action="store_true",
                        help="Cambia vocales por sus correspondientes números")
    parser.add_argument("-cs", "--consonante_simbolo", dest="cons_simb", action="store_true",
                        help="Cambia consonantes por sus correspondientes símbolos")
    parser.add_argument("-cv", "--vocal_simbolo", dest="voc_simb", action="store_true",
                        help="Cambia consonantes por sus correspondientes símbolos y vocales por sus correspondientes números")
    parser.add_argument("-t", "--todos", dest="todos", action="store_true",
                        help="Aplica todos los cambios disponibles")

    args = parser.parse_args()

    if args.pal or args.f_orig:
        genDic = GeneradorDic(args)
        if args.pal or args.f_orig:
            if args.pal:
                # Trato la palabra
                genDic.procesar()
                print(genDic)
            else:
                # Trato el fichero
                print(args.f_orig)
                genDic.procesarFichero()
        else:
            print("Necesito una palabra o un fichero con palabras, una por línea")
    else:
        print()
        print("Necesito una palabra o un fichero origen para generar una lista de palabras.")
        print("-h o --help para la ayuda.")
        print()
