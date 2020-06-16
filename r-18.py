sueldo_min = int(input(" Ingrese sueldo del trabajador: "))
años = int(input(" Ingrese su años de servicio en la empresa: "))
estamento = int(input(" Ingrese su estamento (cargo) perteneciente a la empresa con los siguientes números 1 Obrero, 2 Administrativo, 3 Directivo: "))

# Creo e incializo @obrero @adminsitrativo y @directivo
# char es un carácter (una letra)

obrero = int
administrativo = int
directivo = int

# Clasificacion segun su estamento

obrero = 1
administrativo = 2
directivo = 3

# Descuento por salud(7%) y prevision(10%)

descuento_salud = sueldo_min*0.7
descuento_prevision = sueldo_min*0.1
sueldo_liquido = sueldo_min

# Bono segun los años de servicio

if años <=3 : # Trabajadores con hasta 3 años de antigüedad bono igual al
    bono_trabajador = sueldo_min*0.15 # 15% del sueldo
elif años <=6: #  Trabajadores con hasta 6 años de antigüedad bono igual al
    if estamento == obrero or estamento == administrativo : # 20% del sueldo para Obreros y Administrativos
        bono_trabajador = sueldo_min*0.2
    else : # 25% del sueldo para Directivos
        bono_trabajador = sueldo_min*0.25
else : # Trabajadores con más de 6 años de antigüedad bono igual al
    if estamento == obrero : # 30% del sueldo para Obreros
        bono_trabajador = sueldo_min*0.3
    elif estamento == administrativo : # 35% del sueldo para Administrativos
        bono_trabajador = sueldo_min*0.35
    else : # 40% del sueldo para Directivos
        bono_trabajador = sueldo_min*0.4

sueldo_liquido = sueldo_liquido - descuento_salud - descuento_prevision + bono_trabajador

# RESPUESTAS
# Además del bono que le corresponde al trabajador, el algoritmo debe mostrar el 
# monto a descontar por salud que es de un 7% del sueldo, el monto a descontar por 
# previsión que es de un 10% del sueldo y el monto final que se le debe pagar (sueldo líquido) 
# considerando los descuentos anteriores y el bono que se le entrega (el monto del bono que se 
# le entrega está libre de todo descuento).

print(" ")
# 0) Monto del bono que le corresponde al trabajador. @bono_trabajador
print(" El bono al trabajador es de: ", (bono_trabajador))
# 1) Monto a descontar por salud que es de un 7% del sueldo. @descuento_salud
print(" Descuento por salud -", (descuento_salud))
# 2) Monto a descontar por previsión que es de un 10% del sueldo. @descuento_prevision
print(" Descuento por prevision -", (descuento_prevision))
# 3) Monto final que se le debe pagar (sueldo líquido) considerando los descuentos anteriores y el bono que se le entrega 
# (el monto del bono que se le entrega está libre de todo descuento). @sueldo_liquido
print(" Sueldo final a entregar al trabajador: ", (sueldo_liquido))