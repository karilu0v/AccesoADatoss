extensiones = {
    "jpg" : b'\xff\xd8\xff',
    "pdf" : b'\x25\x50\x44\x46',
    }


def is_jpg(path):
    with open(path, "rb") as f:
        return f.read(3) == extensiones["jpg"]
 
 
def is_pdf(path):
    with open(path, "rb") as f:
        return f.read(4) == extensiones["pdf"]
 
 
 
 
print(is_jpg("jaidee.jpg"))

print(is_pdf("jaidee.jpg"))
print(is_pdf("PracticaUT1ElisabethMolinaRebollo.pdf"))
