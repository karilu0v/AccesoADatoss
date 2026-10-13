with open ("PracticaUT1ElisabethMolinaRebollo.pdf", "rb") as lector, open("copia.pdf", "wb") as escritor:
    contenido = lector.read()
    escritor.write(contenido)