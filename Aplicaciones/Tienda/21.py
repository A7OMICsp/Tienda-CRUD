import difflib


productos = {
    "nombre": ["Martillo", "Destornillador", "Sofá"],
}

print(productos["nombre"])

nombre = "Mart"
print(difflib.get_close_matches(nombre, productos["nombre"]))
