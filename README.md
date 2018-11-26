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
el código está orientado a objetos en donde se le van dando ciertas ordenes que deben ser ejectudas, Gtk hace que el trabajo se mucho más fácil teniendo ciertas funciones ya estipuladas que hacen que el codigo ejecute ciertas acciones.
 el código contiene 6 funciones encargadas de hacer las operaciones indicadas que aparecen en el menú principal, siendo estas llamadas cuando se hace click en cualquiera de ellas, la función "__init__" es la que le da a ordenes a Gtk builder para que este trabaje con los distintos objetos que se le van entregando, los archivos creados en glade se van entregando y la condicion para que estos se ejecuten es presionar click en cada un de ellos.
finalmente se le es entregada una condición que permite que la instancia se ejecute.


# Errores del programa:
-solo es capaz de recibir matrices de 3x3 
- es un tanto ineficiente al ir recibiendo la información que se recibe principalmente en la interfaz gráfica debido al hecho de que debe obtener los datos uno por uno de una forma no muy eficiente.
- 

# Autores
Rachell Aravena
Constanza Valenzuela
