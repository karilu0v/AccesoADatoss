contenido_binario = None

with open("jaidee.jpg", "rb") as f:
    contenido_binario = f.read()


with open("jaidee2.jpg", "wb") as f:
    f.write(contenido_binario + b'\x55')