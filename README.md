# Calculadora de Matrices
Usuarios	1 usuario
Complejidad	Baja

Calculadora de matrices es un programa que permite la ejecución de diferentes operaciones básicas de matrices de dimensiones 3x3. 

# Obtención del Programa
Clonar este repositorio y ejecutar "calculadora.py" dentro de la carpeta "Calculadora" teniendo su entorno virtual activado.

# Prerrequisitos
- Python 3. Desarrollado y probado en 3.5.6.
- Diseñador de interfaces Glade
- Conjunto de bibliotecas multiplataforma para desarrollar interfaces gráficas GTK, como la librería pygobject.

# Objetivo
Ofrecer al usuario un programa amigable y sencillo que ayude con los calculos básicos de matrices con dimensión 3x3

# Controles
Puede ultilizarse el mouse y el teclado númerico.
Los valores a ingresar han de ser exclusivamente números.

# Sobre el código:
El código está orientado a objetos en donde se le dan ordenes ha ser ejectudas. Gtk hace que el trabajo se mucho más fácil teniendo ciertas funciones propias para la ejecucíon de acciones.
El código contiene 6 funciones (suma, sustracción, multiplicación, determinante, transpuesta e inversa de matrices 3x3) encargadas de realizar los cálculos correspondientes indicados en el menú principal. Estas son llamadas cuando se hace click en cualquiera de ellas, la función "'__init__'" es la que le da a ordenes a Gtk builder para que este trabaje con los distintos objetos (valores) que son entregados por el usuario. Los archivos creados en glade (ventanas: principal y emergentes) se van entregando , siendo la única condición para su ejecucuión presionar click en cada un de ellos.
Finalmente se le es entregada una condición que permite que la instancia se ejecute.

# Errores del programa:
- Solo es capaz de recibir matrices de 3x3 
- Las ventanas carecen de la opción de volver atras, siendo la únicas opciones posibles: cerrarlas o seguir adelante
- En cuanto al código en sí se la podría considerar un tanto ineficiente, pues al ir recibiendo la información entregada por el usuario en la interfaz gráfica las operaciones se realizan de una en una para asegurar un resultado exacto.

# Autores
- Rachell Aravena
- Constanza Valenzuela
