import libreria

assert (libreria.validar_nombre("juan") == True)
assert (libreria.validar_nombre("1999999") == False)
assert (libreria.validar_nombre(False) == False)
assert (libreria.validar_nombre("fr") == False)
print("OK")


assert (libreria.validar_entero(4564) == True)
assert (libreria.validar_entero("no") == False)
assert (libreria.validar_entero(5.9) == False)
assert (libreria.validar_entero("jkh") == False)
print("OK")



assert (libreria.validar_cadena("ds4d5ds") == True)
assert (libreria.validar_cadena("bueno") == True)
assert (libreria.validar_cadena(212.23) == False)
assert (libreria.validar_cadena(12333211) == False)
assert (libreria.validar_cadena(True) == False)
print("OK")

assert (libreria.validar_rango("suave",10,25) == False)
assert (libreria.validar_rango("duro","56","23") == False)
assert (libreria.validar_rango(True,5,6) == False)
assert (libreria.validar_rango(46,23,56) == True)
print("OK")

assert (libreria.validar_sexo("masculino") == True)
assert (libreria.validar_sexo("femenino") == True)
assert (libreria.validar_sexo(True) == False)
assert (libreria.validar_sexo(12333211) == False)
assert (libreria.validar_sexo("hola") == False)
print("OK")


