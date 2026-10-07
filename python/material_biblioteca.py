class MaterialBiblioteca:
    def __init__(self, titulo, codigo, disponible=True):
        self.titulo = titulo
        self.codigo = codigo
        self.disponible = disponible

    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"Título: {self.titulo} | Código: {self.codigo} | Estado: {estado}"

    def calcular_dias_prestamo(self):
        raise NotImplementedError("Las clases hijas deben implementar este método")