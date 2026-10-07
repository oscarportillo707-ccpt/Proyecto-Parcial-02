# Proyecto-Parcial-02

Proyecto del Parcial 02

## Equipo 04

# Nombre del Equipo:

### Los 5 fantasticos

### Integrantes:

- Diego Alexander Hernández Nuñez.
- Brandon Edenilson Alas Tobias.
- Oscar Javier Portillo Tejada.
- Cristopher David Salmeron Tejada.
- William Javier Chacon Calderon.

## Escenario seleccionado

Escenario A - Sistema de biblioteca

## Descripción de la solución

Se desarrolló una demostración de un sistema de biblioteca
universitaria utilizando Python para implementar la lógica
orientada a objetos y HTML, CSS y JavaScript para desarrollar
la interfaz.

## Clase padre

La clase padre es MaterialBiblioteca. Reúne las características que comparten todos los recursos de la biblioteca: el título, el código y la disponibilidad (si el material está disponible o prestado). También define el método mostrar_informacion(), que presenta esos datos básicos, y el método calcular_dias_prestamo(), que cada clase hija debe implementar según su tipo de material.

## Clases hijas

Las clases hijas son Libro y Revista, y ambas heredan de MaterialBiblioteca. Libro incorpora el atributo autor y tiene un período de préstamo de 7 días. Revista incorpora el número de edición y tiene un período de préstamo de 3 días. Al heredar, ambas reutilizan los atributos y métodos del padre sin repetir código.

## Método sobrescrito

El método sobrescrito es mostrar_informacion(). Está definido en la clase padre y cada clase hija lo redefine para agregar su información particular: Libro muestra además el autor y Revista muestra además el número de edición. Las hijas aprovechan el método del padre mediante super() y le añaden sus propios datos. El método calcular_dias_prestamo() también se implementa de forma distinta en cada hija.

## Cómo se aplica el polimorfismo

El polimorfismo permite que objetos de distintas clases respondan de forma diferente al mismo método. En el programa, los tres libros y las tres revistas se almacenan en una misma lista, lo cual es posible porque todos heredan de MaterialBiblioteca. Luego, un único ciclo recorre la lista y llama a mostrar_informacion() y calcular_dias_prestamo() sobre cada objeto, sin verificar de qué tipo es. Python ejecuta automáticamente la versión que corresponde a cada clase: los libros muestran el autor y devuelven 7 días, y las revistas muestran el número de edición y devuelven 3 días. Además, si se agregara un nuevo tipo de material, el ciclo no tendría que modificarse.

## Explicación sobre la Función de HTML, CSS y JavaScript

HTML define la estructura de la página: el encabezado, los botones de filtro y el espacio donde se muestra el catálogo. CSS se encarga de la presentación visual: los colores, el diseño de las tarjetas de cada material y las etiquetas que indican si está disponible o prestado. JavaScript aporta el comportamiento: crea los objetos de libros y revistas, genera las tarjetas dinámicamente, filtra el catálogo por tipo y cambia la disponibilidad cuando el usuario hace clic en el botón de préstamo o devolución. En JavaScript se replica además la misma herencia y el mismo polimorfismo del modelo en Python.

## Responsabilidades del frontend

El frontend se encarga de lo que el usuario ve y toca. Muestra el catálogo y los datos de cada material, da formato visual al estado, captura las acciones del usuario (clics y filtros), actualiza la pantalla sin recargar la página y realiza validaciones básicas para dar una respuesta inmediata.

## Responsabilidades del backend

El backend, desarrollado en Python, se encarga de lo que debe ser correcto y permanente. Contiene el modelo y las reglas de negocio, como las clases del sistema y el cálculo de los días de préstamo. Almacena los datos de forma persistente en una base de datos, valida y autoriza las operaciones de manera definitiva (por ejemplo, que un material ya prestado no pueda prestarse a otra persona), gestiona usuarios y seguridad, y envía al frontend la información del catálogo.

## Relación entre ambos

Las validaciones del frontend mejoran la experiencia del usuario, pero no son seguras por sí solas, porque pueden manipularse desde el navegador. Por eso la validación definitiva siempre debe hacerse en el backend. En esta demostración los datos están dentro del archivo JavaScript para simplificar, pero en un sistema real el frontend los solicitaría al backend.
