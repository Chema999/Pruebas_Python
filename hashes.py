# -*- coding: iso-8859-1 -*-

import hashlib


class Hashes(object):
    """
        Objeto con los hashes sha512, sha256 y md5 de la cadena asignada """

    def __init__(self):
        self.orig = ""
        self.hash_sha512 = ""
        self.hash_sha256 = ""
        self.hash_md5 = ""

    """
        Asigna cadena al objeto y calcula sus hashes """

    def asignar(self, cadena):
        self.orig = cadena
        self.hash_sha512 =hashlib.sha512(cadena.encode()).hexdigest()
        self.hash_sha256 = hashlib.sha256(cadena.encode()).hexdigest()
        self.hash_md5 = hashlib.md5(cadena.encode()).hexdigest()

    def asignar2(self, cad, sha512, sha256, md5):
        self.orig = cad
        self.hash_sha512 = sha512
        self.hash_sha256 = sha256
        self.hash_md5 = md5

    def __str__(self):
        return self.orig + "\nsha512: #" + self.hash_sha512 + "#\nsha256: #" + self.hash_sha256 + "#\nmd5: #" + self.hash_md5 + "#\n"

    def imprimir(self):
        return self.orig + "," + self.hash_sha256 + "," + self.hash_sha256 + "," + self.hash_md5

    """
        Devuelve el sha512 """

    def sha512(self):
        return self.hash_sha512

    """
        Devuelve el sha256 """

    def sha256(self):
        return self.hash_sha256

    """
        Devuelve el md5 """

    def md5(self):
        return self.hash_md5

    """
        Devuelve el texto original """

    def original(self):
        return self.orig


if __name__ == "__main__":
    texto = Hashes()
    texto.asignar("password")
    print(texto)
    print(texto.original())
    print(texto.sha512())
    print(texto.sha256())
    print(texto.md5())
