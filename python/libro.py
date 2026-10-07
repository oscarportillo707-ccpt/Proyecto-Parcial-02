from material_biblioteca import MaterialBiblioteca

class Libro(MaterialBiblioteca):
    def __init__(self, titulo, codigo, autor, disponible=True):
        super().__init__(titulo, codigo, disponible)
        self.autor = autor

    def mostrar_informacion(self):
        return f"[Libro] {super().mostrar_informacion()} | Autor: {self.autor}"

    def calcular_dias_prestamo(self):
        return 7