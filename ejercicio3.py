def verificar_contrasena(contrasena, condiciones):
    for nombre_condicion, expresion in condiciones:
        if not expresion(contrasena):
            return False
    return True

# Definición de condiciones
longitud_valida = ("Longitud válida", lambda contrasena: len(contrasena) >= 8)
tiene_mayuscula = ("Tiene mayúscula", lambda contrasena: any(c.isupper() for c in contrasena))
tiene_minuscula = ("Tiene minúscula", lambda contrasena: any(c.islower() for c in contrasena))
tiene_numero = ("Tiene número", lambda contrasena: any(c.isdigit() for c in contrasena))

# Lista de condiciones
condiciones_contraseña = [longitud_valida, tiene_mayuscula, tiene_minuscula, tiene_numero]

# Prueba de la función
contrasena = "Segura"
es_valida = verificar_contrasena(contrasena, condiciones_contraseña)
if es_valida:
    print("La contraseña es válida.")
else:
    print("La contraseña no cumple con los requisitos.")
