from libro import Libro
from revista import Revista

def main():
    materiales = [
        Libro("Cien años de soledad", "L001", "Gabriel García Márquez"),
        Libro("Don Quijote de la Mancha", "L002", "Miguel de Cervantes", disponible=False),
        Libro("El principito", "L003", "Antoine de Saint-Exupéry"),
        Revista("National Geographic", "R001", 245),
        Revista("Muy Interesante", "R002", 310),
        Revista("Scientific American", "R003", 128, disponible=False),
    ]

    print("=== Catálogo de la biblioteca ===\n")
    for material in materiales:  
        print(material.mostrar_informacion())
        print(f"Días de préstamo: {material.calcular_dias_prestamo()}\n")


if __name__ == "__main__":
    main()