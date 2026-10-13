#porcentaje de pasajeros supervivientes
#porcentanje de hombres y mujeres supervivientes
#porcentaje de menores supervivientes
#media de edad supervivientes
#media de edad de muertos
#ticket medio superviviente
#ticket medio de la víctima

pasajeros = []

def porcentaje_menores(datos):
    numero_menores = 0
    numero_supervivientes = 0
    for p in datos:
        if p["age"] < 18:
            numero_menores += 1
            if p["sup"] == 1:
                numero_supervivientes += 1
    return (numero_supervivientes/numero_menores)*100

def media_edad_supervivientes(datos):
    edad_total = 0
    num_sup = 0
    for p in datos:
        if p["sup"] == 1:
            edad_total+= p["age"]
            num_sup += 1
    return edad_total/num_sup

def media_edad_muertos(datos):
    edad_total = 0
    num_vic = 0
    for p in datos:
        if p["sup"] == 0:
            edad_total+= p["age"]
            num_vic+=1
    return edad_total/num_vic

def media_ticket_supervivientes(datos):
    ticket_total = 0
    num_tick = 0
    for p in datos:
        if p["sup"] == 1:
            ticket_total+= p["fare"]
            num_tick += 1
    return ticket_total/num_tick

def media_ticket_muertos(datos):
    ticket_total = 0
    num_tick = 0
    for p in datos:
        if p["sup"] == 0:
            ticket_total+= p["fare"]
            num_tick +=1
    return ticket_total/num_tick

def porcentaje_supervivientes(datos):
    numero_supervivientes = 0
    for p in datos:
        if p["sup"] == 1:
            numero_supervivientes += 1
    return (numero_supervivientes/len(datos))*100

def porcentaje_por_sexo(datos):
    hombres_sup=0
    hombres_totales=0
    mujeres_sup=0
    mujeres_totales=0
    for p in datos:
        if p["sex"] == 1:
            hombres_totales+=1
            if p["sup"] == 1:
                hombres_sup+=1
        else:
            mujeres_totales+=1
            if p["sup"] == 1:
                mujeres_sup+=1
    return (hombres_sup/hombres_totales*100 ,mujeres_sup/mujeres_totales*100)



with open ("titanic.csv", "r", encoding="utf-8") as f:
    f.readline()
    for linea  in f:
        #print(linea.split(","))
        
        datos = linea.split(",")
        pasajero = {}
        pasajero["sup"] = int(datos[0])
        pasajero["class"] = int(datos[1])
        pasajero["sex"] = 1 if datos[2] == "male" else 0
        if datos[3].strip() == "":
            continue
        pasajero["age"] = float(datos[3])
        pasajero["fare"] = float(datos[4])
        pasajeros.append(pasajero)
        
    #print(pasajeros)

print(f"porcentaje supervivientes: {porcentaje_supervivientes(pasajeros):.2f}%")

print(f"porcentaje hombres supervivientes: {porcentaje_por_sexo(pasajeros)[0]:.2f}%")

print(f"porcentaje mujeres supervivientes: {porcentaje_por_sexo(pasajeros)[1]:.2f}%")

print(f"porcentaje menores supervivientes: {porcentaje_menores(pasajeros):.2f}%")

print(f"media edad supervivientes: {media_edad_supervivientes(pasajeros):.2f}")

print(f"media edad víctimas: {media_edad_muertos(pasajeros):.2f}")

print(f"media ticket supervivientes: {media_ticket_supervivientes(pasajeros):.2f}")

print(f"media ticket victimas: {media_ticket_muertos(pasajeros):.2f}")
