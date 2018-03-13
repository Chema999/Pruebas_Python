# -*- coding: iso-8859-1 -*-

from hashes import Hashes

class ListaHashes:
    """
        Lista de objetos de la clase hashes para poder buscar el hash y obtener la palabra correspondiente
    """

    def __init__(self):
        self.lista = []
        self.__DEBUG = False

    """
        Agrega un hash a la lista de hashes """

    def agregar(self, cad):
        hashCad = Hashes()
        hashCad.asignar(cad)
        self.lista.append(hashCad)

    """
        Lista por pantalla todos los hashes """

    def listar(self):
        for unHash in self.lista:
            print(unHash)

    """
        Busca el hash en formato sha512, devolviendo su original """

    def buscar_sha512(self, str_sha512):
        tamanyo = len(self.lista)
        i = 0
        encontrado = False
        salir = False
        while not salir:
            unHash = self.lista[i]
            if str_sha512 == unHash.sha512():
                encontrado = True
                salir = True
            else:
                i = i + 1
                if i >= tamanyo:
                    salir = True
        if encontrado:
            return unHash.original()
        else:
            return "-No encontrado-"

    """
        Busca el hash en formato sha256, devolviendo su original """

    def buscar_sha256(self, str_sha256):
        tamanyo = len(self.lista)
        i = 0
        encontrado = False
        salir = False
        while not salir:
            unHash = self.lista[i]
            if str_sha256 == unHash.sha256():
                encontrado = True
                salir = True
            else:
                i = i + 1
                if i >= tamanyo:
                    salir = True
        if encontrado:
            return unHash.original()
        else:
            return "-No encontrado-"

    """
        Busca el hash en formato md5, devolviendo su original """

    def buscar_md5(self, str_md5):
        tamanyo = len(self.lista)
        i = 0
        encontrado = False
        salir = False
        while not salir:
            unHash = self.lista[i]
            if str_md5 == unHash.md5():
                encontrado = True
                salir = True
            else:
                i = i + 1
                if i >= tamanyo:
                    salir = True
        if encontrado:
            return unHash.original()
        else:
            return "-No encontrado-"

    """
        Guarda la lista en el fichero nomFich """

    def guardar(self, nomFich):
        try:
            print("Creando fichero:", nomFich)
            f = open(nomFich, "w")
            i = 0
            tamanyo = len(self.lista)
            try:
                # La primera línea son los nombres de los campos
                buffer = "palabra,sha512,sha256,md5\n"
                f.writelines(buffer)
                if self.__DEBUG:
                        print("Guardando ...")
                while i < tamanyo:
                    hash = self.lista[i]
                    buffer = hash.imprimir()
                    if self.__DEBUG:
                        print(hash)
                    buffer = buffer + "\n"
                    f.writelines(buffer)
                    i = i + 1
                print("Fichero", nomFich, "guardado")
            finally:
                f.close()

        except IOError:
            print("Error al guardar el archivo", nomFich)

    """
        Carga el fichero nomFich en la lista """

    def cargar(self, nomFich):
        try:
            print("Leyendo fichero", nomFich)
            f = open(nomFich, "r")
            try:
                # La primera línea son los nombres de los campos
                buffer = f.readline()
                # La siguiente línea tiene ya la información
                buffer = f.readline()
                self.lista.clear()
                while buffer:
                    partes = buffer.split(",")
                    # Quito el '\n' final de la última parte
                    partes[2]=partes[2].strip("\n")
                    unHash = Hashes()
                    unHash.asignar2(partes[0], partes[1], partes[2])
                    if self.__DEBUG:
                        print("Leído:", unHash)
                    self.lista.append(unHash)
                    buffer = f.readline()
            finally:
                f.close()

        except IOError:
            print("No se ha podido abrir el fichero", nomFich)


if __name__ == "__main__":
    listaHashes = ListaHashes()

    listaHashes.agregar("password")
    listaHashes.agregar("Password")
    listaHashes.agregar("PassworD")
    listaHashes.agregar("123")

    #listaHashes.cargar("passwords.hash")
    listaHashes.listar()
    print(listaHashes.buscar_sha256("a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3"))
    print(listaHashes.buscar_sha256("e7cf3ef4f17c3999a94f2c6f612e8a888e5b1026878e4e19398b23bd38ec221a"))
    print(listaHashes.buscar_md5("5f4dcc3b5aa765d61d8327deb882cf99"))
    print(listaHashes.buscar_md5("202cb962ac59075b964b07152d234b70"))
    print(listaHashes.buscar_sha256("5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"))
    print(listaHashes.buscar_sha512("b109f3bbbc244eb82441917ed06d618b9008dd09b3befd1b5e07394c706a8bb980b1d7785e5976ec049b46df5f1326af5a2ea6d103fd07c95385ffab0cacbc86"))
    listaHashes.guardar("passwords.hash")
