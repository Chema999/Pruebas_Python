# -*- coding: iso-8859-1 -*-

import codecs
import argparse


class CodecFichero:
    """
        Lee un fichero codificado en un determinado codec y lo graba en otro fichero con otro codec
    """

    def __init__(self):
        self.nomFOrig = ""
        self.nomFDest = ""
        self.__opOrig = 0
        self.__opDest = 0
        self.__codecs = ["salir", "iso-8859-1", "utf-8", "cp850", "utf-16", "utf-16le", "big5", "base64-codec", "hex-codec"]
        self.__desc = ["Finaliza el programa", "Europa Occidental", "Todos los lenguajes", "Ventana CMD",
                       "Ventana PowerShell", "Ventana PowerShell", "Chino tradicional", "Base 64", "Hexadecimal"]
        # Anoto los codecs que "deben ser guardados como bytes", no como str
        self.__tipoBytes = ["base64-codec", "hex-codec"]

    # Hay más códigos en https://docs.python.org/2.4/lib/standard-encodings.html

    """
        Muestra un menú de opciones de codificaciones """

    def __str__(self):
        texto = ""
        for i in range(0, len(self.__codecs)):
            texto = texto + str(i) + " - " + self.__codecs[i] + " " + self.__desc[i] + "\n"
        return texto

    """
        Pide por teclado la opción a utilizar. 0 sale del programa """

    def seleccion(self):
        op = -1
        while op < 0 or op >= len(self.__codecs):
            mens = "¿Opción [0 - " + str(len(self.__codecs) - 1) + "]? "
            resp = input(mens)
            op = int(resp)
        if op == 0:
            print("Programa finalizado")
            quit(0)
        return op

    """
        Devuelve un listado con los codecs soportados """

    def codecsSoportados(self):
        codecsSop = ""
        for i in range(1, len(codecFichero.__codecs)):
            codecsSop = codecsSop + self.__codecs[i] + " - " + self.__desc[i] + "\n"
        return codecsSop

    """
        Selecciona la opción de codificación del fichero origen """

    def seleccionOrig(self):
        self.__opOrig = self.seleccion()

    """
        Selecciona la opción de codificación del fichero destino """

    def seleccionDest(self):
        self.__opDest = self.seleccion()

    """
        Lee por teclado el nombre del fichero a utilizar, mostrando el mensaje pasado. Si se introduce exit
         se finaliza el programa """

    def nombreFichero(self, mens):
        nomFich = ""
        while nomFich == "":
            nomFich = input(mens)
        if nomFich == "exit":
            print("Programa finalizado")
            quit(0)
        return nomFich

    """
        Lee el nombre del fichero origen """

    def ficheroOrigen(self):
        self.nomFOrig = self.nombreFichero("¿Nombre del fichero origen? (o exit) ")

    """
        Lee el nombre del fichero destino """

    def ficheroDestino(self):
        self.nomFDest = self.nombreFichero("¿Nombre del fichero destino? (o exit) ")

    """
        Realiza el proceso interactivo de recodificación de un fichero a otro """

    def proceso(self):
        print("Recodificando ", self.nomFOrig, "(" + self.__codecs[self.__opOrig] + ") a", self.nomFDest, "(" +
              self.__codecs[self.__opDest] + ")")
        try:
            fO = codecs.open(self.nomFOrig, "r", self.__codecs[self.__opOrig])
            fD = codecs.open(self.nomFDest, "w", self.__codecs[self.__opDest])
            try:
                buffer = fO.readline()
                while buffer:
                    print("Leído:", buffer)
                    # Distingo si hay que guardar como str o com byte
                    if self.__codecs[self.__opDest] in self.__tipoBytes:
                        fD.write(buffer.encode())
                    else:
                        if self.__codecs[self.__opOrig] in self.__tipoBytes:
                            fD.write(buffer.decode())
                        else:
                            fD.write(buffer)
                    buffer = fO.readline()
            finally:
                fO.close()
                fD.close()
                print("Fichero recoficado:", self.nomFDest)
        except IOError as IOEr:
            print("  ** Error: No se puede abrir el fichero", self.nomFOrig)
            print(IOEr)
        except UnicodeDecodeError as UDEr:
            print("  ** Error: El fichero", self.nomFOrig, "no tiene la codificación indicada")
            print(UDEr)
        except UnicodeError as UEr:
            print("  ** Error :El fichero", self.nomFOrig, "no tiene la codificación indicada")
            print(UEr)

    """
        Comprueba si el texto codTexto es una de las codificaciones soportadas """

    def validarCodificacion(self, codTexto):
        minus = codTexto.lower()
        return minus in self.__codecs

    """
        Asignar el código numérico de la lista para las codificaciones pasadas como cadenas de texto """

    def asignarCodecs(self, strCodO, strCodD):
        pos = self.__codecs.index(strCodO)
        self.__opOrig = pos
        pos = self.__codecs.index(strCodD)
        self.__opDest = pos


if __name__ == "__main__":
    codecsSoport = ""
    validoCodOrig = True
    validoCodDest = True
    codecFichero = CodecFichero()

    codecsSoport = codecFichero.codecsSoportados()
    parser = argparse.ArgumentParser(description="Conversor de codificaciones de ficheros",
                                     epilog="Dado un fichero con una codificación, crea otro fichero con otra codificación.\n" +
                                            "Si solo se indica --cod_orig, se usarán como valores por defecto:\n" +
                                            "  --cod_orig=iso-8859-1 --fichero_dest=<nombre fichero origen>.<codificación destino>\n" +
                                            "  --cod_dest=utf-8\n" +
                                            "Codificaciones soportadas (en minúsculas):\n" + codecsSoport)
    parser.add_argument("-co", "--cod_orig", dest="codOrig",
                        help="Codificación del fichero origen")
    parser.add_argument("-i", "--fichero_orig", dest="fOrig",
                        help="Nombre del fichero origen")
    parser.add_argument("-o", "--fichero_dest", dest="fDest",
                        help="Nombre del fichero destino")
    parser.add_argument("-cd", "--cod_dest", dest="codDest",
                        help="Codificación del fichero destino")
    parser.add_argument("-c", "--mostrar-codecs", dest="mostrarCodecs", action="store_true")

    args = parser.parse_args()

    if args.fOrig or args.mostrarCodecs:
        if args.mostrarCodecs:
            print()
            print("Codecs soportados:")
            print(codecFichero.codecsSoportados())
            print()
        else:
            # Desde línea de comandos, con los parámetros
            codecFichero.nomFOrig = args.fOrig
            if args.codOrig:
                validoCodOrig = codecFichero.validarCodificacion(args.codOrig)
                if not validoCodOrig:
                    print(args.codOrig, "no es una codificación válida")
                    quit()
            else:
                args.codOrig = "iso-8859-1"
            if args.codDest:
                validoCodDest = codecFichero.validarCodificacion(args.codDest)
                if not validoCodDest:
                    print("  ** Error:", args.codDest, "no es una codificación válida")
                    quit()
            else:
                args.codDest = "utf-8"

            if args.fDest:
                codecFichero.nomFDest = args.fDest
            else:
                codecFichero.nomFDest = args.fOrig + "." + args.codDest

            codecFichero.asignarCodecs(args.codOrig, args.codDest)
    else:
        # Proceso interactivo, a través de menú
        print("¿Codificación del fichero origen?")
        print(codecFichero)
        codecFichero.seleccionOrig()
        codecFichero.ficheroOrigen()
        print()
        print(codecFichero)
        print("¿Codificación del fichero destino?")
        codecFichero.seleccionDest()
        codecFichero.ficheroDestino()

    if not args.mostrarCodecs:
        codecFichero.proceso()
