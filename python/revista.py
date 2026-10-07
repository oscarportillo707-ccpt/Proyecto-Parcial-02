from material_biblioteca import MaterialBiblioteca

class Revista(MaterialBiblioteca):
    def __init__(self, titulo, codigo, numero_edicion, disponible=True):
        super().__init__(titulo, codigo, disponible)
        self.numero_edicion = numero_edicion

    def mostrar_informacion(self):
        return (f"[Revista] {super().mostrar_informacion()} "
                f"| Edición N.º: {self.numero_edicion}")

    def calcular_dias_prestamo(self):
        return 3