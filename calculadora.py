import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk


class calculadora():
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("menu_princ.glade")

        self.menu = self.builder.get_object("menu_pr")
        self.menu.set_default_size(600, 400)

        self.s_matr = self.builder.get_object("s_matrices")
        self.s_matr.connect("clicked", self.suma_matrices)

        self.r_matr = self.builder.get_object("r_matrices")
        self.r_matr.connect("clicked", self.resta_matrices)

        self.m_matr = self.builder.get_object("m_matrices")
        self.m_matr.connect("clicked", self.multiplicacion_matrices)

        self.d_matr = self.builder.get_object("det_matriz")
        self.d_matr.connect("clicked", self.determinante_matriz)

        self.trans_matr = self.builder.get_object("trans_matriz")
        self.trans_matr.connect("clicked", self.matriz_transpuesta)

        self.inver_matr = self.builder.get_object("inver_matriz")
        self.inver_matr.connect("clicked", self.matriz_inversa)

        self.menu.show_all()

    def suma_matrices(self, boton):
        # abrir la ventana para sumar
        ventana_tres_matrices("sumar")

    def resta_matrices(self, boton):
        # abrir la ventana de restas
        ventana_tres_matrices("restar")

    def multiplicacion_matrices(self, boton):
        ventana_tres_matrices("multiplicar")

    def determinante_matriz(self, boton):
        ventana_determinante()

    def matriz_transpuesta(self, boton):
        ventana_dos_matrices("transpuesta")

    def matriz_inversa(self, boton):
        ventana_dos_matrices("inversa")


class ventana_tres_matrices:
    def __init__(self, metodo):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("tres_matrices.glade")
        ventana = self.builder.get_object("ventana_tres_matrices")

        # ponerle un titulo a la ventana
        titulo = self.builder.get_object("titulo")
        operacion = self.builder.get_object("signo_operacion")

        if metodo == "sumar":
            titulo.set_label("Suma de matrices")
            operacion.set_label(") + (")
        elif metodo == "restar":
            titulo.set_label("Resta de matrices")
            operacion.set_label(") - (")
        elif metodo == "multiplicar":
            titulo.set_label("Multiplicación")
            operacion.set_label(") x (")

        # la matriz A
        self.AF1C1 = self.builder.get_object("AF1C1")
        self.AF1C2 = self.builder.get_object("AF1C2")
        self.AF1C3 = self.builder.get_object("AF1C3")
        self.AF2C1 = self.builder.get_object("AF2C1")
        self.AF2C2 = self.builder.get_object("AF2C2")
        self.AF2C3 = self.builder.get_object("AF2C3")
        self.AF3C1 = self.builder.get_object("AF3C1")
        self.AF3C2 = self.builder.get_object("AF3C2")
        self.AF3C3 = self.builder.get_object("AF3C3")

        # matriz B
        self.BF1C1 = self.builder.get_object("BF1C1")
        self.BF1C2 = self.builder.get_object("BF1C2")
        self.BF1C3 = self.builder.get_object("BF1C3")
        self.BF2C1 = self.builder.get_object("BF2C1")
        self.BF2C2 = self.builder.get_object("BF2C2")
        self.BF2C3 = self.builder.get_object("BF2C3")
        self.BF3C1 = self.builder.get_object("BF3C1")
        self.BF3C2 = self.builder.get_object("BF3C2")
        self.BF3C3 = self.builder.get_object("BF3C3")

        # matriz C de resultados
        self.CF1C1 = self.builder.get_object("CF1C1")
        self.CF1C2 = self.builder.get_object("CF1C2")
        self.CF1C3 = self.builder.get_object("CF1C3")
        self.CF2C1 = self.builder.get_object("CF2C1")
        self.CF2C2 = self.builder.get_object("CF2C2")
        self.CF2C3 = self.builder.get_object("CF2C3")
        self.CF3C1 = self.builder.get_object("CF3C1")
        self.CF3C2 = self.builder.get_object("CF3C2")
        self.CF3C3 = self.builder.get_object("CF3C3")

        boton_borrar = self.builder.get_object("boton_borrar")
        boton_borrar.connect("clicked", self.borrar_todo)

        boton_calcular = self.builder.get_object("boton_calcular")

        # esto ayuda a decidir si vamos a sumar, restar o multiplicar
        if metodo == "sumar":
            boton_calcular.connect("clicked", self.sumar)
        elif metodo == "restar":
            boton_calcular.connect("clicked", self.restar)
        elif metodo == "multiplicar":
            boton_calcular.connect("clicked", self.multiplicar)

        # deja cerrar la ventana al apretar la X roja
        ventana.connect("destroy", Gtk.main_quit)

        # mostrar todo
        ventana.show_all()

    def sumar(self, boton):
        # obtener los numeros de la matriz A
        (AF1C1, AF1C2, AF1C3, AF2C1, AF2C2, AF2C3, AF3C1, AF3C2, AF3C3) = self.obtener_valores_matriz_a()

        # obtener los numeros en la matriz B
        (BF1C1, BF1C2, BF1C3, BF2C1, BF2C2, BF2C3, BF3C1, BF3C2, BF3C3) = self.obtener_valores_matriz_b()

        # a cada casilla de la matriz C de resultados, asignarle la suma
        self.CF1C1.set_value(AF1C1 + BF1C1)
        self.CF1C2.set_value(AF1C2 + BF1C2)
        self.CF1C3.set_value(AF1C3 + BF1C3)
        self.CF2C1.set_value(AF2C1 + BF2C1)
        self.CF2C2.set_value(AF2C2 + BF2C2)
        self.CF2C3.set_value(AF2C3 + BF2C3)
        self.CF3C1.set_value(AF3C1 + BF3C1)
        self.CF3C2.set_value(AF3C2 + BF3C2)
        self.CF3C3.set_value(AF3C3 + BF3C3)

    def restar(self, boton):
        # obtener los numeros de la matriz A
        (AF1C1, AF1C2, AF1C3, AF2C1, AF2C2, AF2C3, AF3C1, AF3C2, AF3C3) = self.obtener_valores_matriz_a()

        # obtener los numeros en la matriz B
        (BF1C1, BF1C2, BF1C3, BF2C1, BF2C2, BF2C3, BF3C1, BF3C2, BF3C3) = self.obtener_valores_matriz_b()

        # por cada casilla de la matriz C, ponerle el valor de la resta
        self.CF1C1.set_value(AF1C1 - BF1C1)
        self.CF1C2.set_value(AF1C2 - BF1C2)
        self.CF1C3.set_value(AF1C3 - BF1C3)
        self.CF2C1.set_value(AF2C1 - BF2C1)
        self.CF2C2.set_value(AF2C2 - BF2C2)
        self.CF2C3.set_value(AF2C3 - BF2C3)
        self.CF3C1.set_value(AF3C1 - BF3C1)
        self.CF3C2.set_value(AF3C2 - BF3C2)
        self.CF3C3.set_value(AF3C3 - BF3C3)

    def multiplicar(self, boton):
        # obtener los numeros de la matriz A y B
        (AF1C1, AF1C2, AF1C3, AF2C1, AF2C2, AF2C3, AF3C1, AF3C2, AF3C3) = self.obtener_valores_matriz_a()
        (BF1C1, BF1C2, BF1C3, BF2C1, BF2C2, BF2C3, BF3C1, BF3C2, BF3C3) = self.obtener_valores_matriz_b()

        RF1C1 = (AF1C1 * BF1C1) + (AF1C2 * BF2C1) + (AF1C3 * BF3C1)
        RF1C2 = (AF1C1 * BF1C2) + (AF1C2 * BF2C2) + (AF1C3 * BF3C2)
        RF1C3 = (AF1C1 * BF1C3) + (AF1C2 * BF2C3) + (AF1C3 * BF3C3)
        RF2C1 = (AF2C1 * BF1C1) + (AF2C2 * BF2C1) + (AF2C3 * BF3C1)
        RF2C2 = (AF2C1 * BF1C2) + (AF2C2 * BF2C2) + (AF2C3 * BF3C2)
        RF2C3 = (AF2C1 * BF1C3) + (AF2C2 * BF2C3) + (AF2C3 * BF3C3)
        RF3C1 = (AF3C1 * BF1C1) + (AF3C2 * BF2C1) + (AF3C3 * BF3C1)
        RF3C2 = (AF3C1 * BF1C2) + (AF3C2 * BF2C2) + (AF3C3 * BF3C2)
        RF3C3 = (AF3C1 * BF1C3) + (AF3C2 * BF2C3) + (AF3C3 * BF3C3)

        self.CF1C1.set_value(RF1C1)
        self.CF1C2.set_value(RF1C2)
        self.CF1C3.set_value(RF1C3)
        self.CF2C1.set_value(RF2C1)
        self.CF2C2.set_value(RF2C2)
        self.CF2C3.set_value(RF2C3)
        self.CF3C1.set_value(RF3C1)
        self.CF3C2.set_value(RF3C2)
        self.CF3C3.set_value(RF3C3)

    def borrar_todo(self, boton):
        # ponerle el numero cero a la matriz A
        self.AF1C1.set_value(0)
        self.AF1C2.set_value(0)
        self.AF1C3.set_value(0)
        self.AF2C1.set_value(0)
        self.AF2C2.set_value(0)
        self.AF2C3.set_value(0)
        self.AF3C1.set_value(0)
        self.AF3C2.set_value(0)
        self.AF3C3.set_value(0)

        # cero a la matriz B
        self.BF1C1.set_value(0)
        self.BF1C2.set_value(0)
        self.BF1C3.set_value(0)
        self.BF2C1.set_value(0)
        self.BF2C2.set_value(0)
        self.BF2C3.set_value(0)
        self.BF3C1.set_value(0)
        self.BF3C2.set_value(0)
        self.BF3C3.set_value(0)

        # cero a los resultados
        self.CF1C1.set_value(0)
        self.CF1C2.set_value(0)
        self.CF1C3.set_value(0)
        self.CF2C1.set_value(0)
        self.CF2C2.set_value(0)
        self.CF2C3.set_value(0)
        self.CF3C1.set_value(0)
        self.CF3C2.set_value(0)
        self.CF3C3.set_value(0)

    def obtener_valores_matriz_a(self):
        # tomar el VALOR de cada cuadro de entrada de numeros
        valor_AF1C1 = self.AF1C1.get_value()
        valor_AF1C2 = self.AF1C2.get_value()
        valor_AF1C3 = self.AF1C3.get_value()
        valor_AF2C1 = self.AF2C1.get_value()
        valor_AF2C2 = self.AF2C2.get_value()
        valor_AF2C3 = self.AF2C3.get_value()
        valor_AF3C1 = self.AF3C1.get_value()
        valor_AF3C2 = self.AF3C2.get_value()
        valor_AF3C3 = self.AF3C3.get_value()

        # devolver todos los valores de la matriz A
        return (valor_AF1C1, valor_AF1C2, valor_AF1C3, valor_AF2C1, valor_AF2C2, valor_AF2C3, valor_AF3C1, valor_AF3C2, valor_AF3C3)

    def obtener_valores_matriz_b(self):
        valor_BF1C1 = self.BF1C1.get_value()
        valor_BF1C2 = self.BF1C2.get_value()
        valor_BF1C3 = self.BF1C3.get_value()
        valor_BF2C1 = self.BF2C1.get_value()
        valor_BF2C2 = self.BF2C2.get_value()
        valor_BF2C3 = self.BF2C3.get_value()
        valor_BF3C1 = self.BF3C1.get_value()
        valor_BF3C2 = self.BF3C2.get_value()
        valor_BF3C3 = self.BF3C3.get_value()

        # devolver los VALORES de la matriz B
        return (valor_BF1C1, valor_BF1C2, valor_BF1C3, valor_BF2C1, valor_BF2C2, valor_BF2C3, valor_BF3C1, valor_BF3C2, valor_BF3C3)


class ventana_determinante:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("determinante.glade")
        ventana = self.builder.get_object("ventana_determinante")

        # los gtkspinbutton con los valores del usuario
        self.AF1C1 = self.builder.get_object("AF1C1")
        self.AF1C2 = self.builder.get_object("AF1C2")
        self.AF1C3 = self.builder.get_object("AF1C3")
        self.AF2C1 = self.builder.get_object("AF2C1")
        self.AF2C2 = self.builder.get_object("AF2C2")
        self.AF2C3 = self.builder.get_object("AF2C3")
        self.AF3C1 = self.builder.get_object("AF3C1")
        self.AF3C2 = self.builder.get_object("AF3C2")
        self.AF3C3 = self.builder.get_object("AF3C3")

        # el cuadrado para el resultado
        self.resultado = self.builder.get_object("resultado")

        boton_calcular = self.builder.get_object("boton_calcular")
        boton_calcular.connect("clicked", self.calcular_determinante)

        boton_borrar = self.builder.get_object("boton_borrar")
        boton_borrar.connect("clicked", self.borrar_todo)

        # cerrar todo cuando se haga click en la x
        ventana.connect("destroy", Gtk.main_quit)

        # mostrar la ventana
        ventana.show_all()

    def calcular_determinante(self, boton):
        vF1C1 = self.AF1C1.get_value()
        vF1C2 = self.AF1C2.get_value()
        vF1C3 = self.AF1C3.get_value()
        vF2C1 = self.AF2C1.get_value()
        vF2C2 = self.AF2C2.get_value()
        vF2C3 = self.AF2C3.get_value()
        vF3C1 = self.AF3C1.get_value()
        vF3C2 = self.AF3C2.get_value()
        vF3C3 = self.AF3C3.get_value()

        determinante = (vF1C1 * (vF2C2 * vF3C3 - vF2C3 * vF3C2)) - (vF1C2 * (vF2C1 * vF3C3 - vF2C3 * vF3C1)) + (vF1C3 * (vF2C1 * vF3C2 - vF2C2 * vF3C1))

        self.resultado.set_value(determinante)

    def borrar_todo(self, boton):
        # ponerle el numero cero a la matriz A
        self.AF1C1.set_value(0)
        self.AF1C2.set_value(0)
        self.AF1C3.set_value(0)
        self.AF2C1.set_value(0)
        self.AF2C2.set_value(0)
        self.AF2C3.set_value(0)
        self.AF3C1.set_value(0)
        self.AF3C2.set_value(0)
        self.AF3C3.set_value(0)

        # borrar el resultado
        self.resultado.set_value(0)


class ventana_dos_matrices:
    def __init__(self, metodo):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("dos_matrices.glade")
        ventana = self.builder.get_object("ventana_dos_matrices")

        # ponerle un titulo a la ventana
        self.titulo = self.builder.get_object("titulo")

        if metodo == "inversa":
            self.titulo.set_label("Matriz Inversa")
        elif metodo == "transpuesta":
            self.titulo.set_label("Matriz Transpuesta")

        # la matriz A
        self.AF1C1 = self.builder.get_object("AF1C1")
        self.AF1C2 = self.builder.get_object("AF1C2")
        self.AF1C3 = self.builder.get_object("AF1C3")
        self.AF2C1 = self.builder.get_object("AF2C1")
        self.AF2C2 = self.builder.get_object("AF2C2")
        self.AF2C3 = self.builder.get_object("AF2C3")
        self.AF3C1 = self.builder.get_object("AF3C1")
        self.AF3C2 = self.builder.get_object("AF3C2")
        self.AF3C3 = self.builder.get_object("AF3C3")

        # matriz B
        self.BF1C1 = self.builder.get_object("BF1C1")
        self.BF1C2 = self.builder.get_object("BF1C2")
        self.BF1C3 = self.builder.get_object("BF1C3")
        self.BF2C1 = self.builder.get_object("BF2C1")
        self.BF2C2 = self.builder.get_object("BF2C2")
        self.BF2C3 = self.builder.get_object("BF2C3")
        self.BF3C1 = self.builder.get_object("BF3C1")
        self.BF3C2 = self.builder.get_object("BF3C2")
        self.BF3C3 = self.builder.get_object("BF3C3")

        boton_borrar = self.builder.get_object("boton_borrar")
        boton_borrar.connect("clicked", self.borrar_todo)

        boton_calcular = self.builder.get_object("boton_calcular")

        # esto ayuda a decidir si vamos a hacer la invera o transpuesta
        if metodo == "inversa":
            boton_calcular.connect("clicked", self.inversa)
        elif metodo == "transpuesta":
            boton_calcular.connect("clicked", self.transpuesta)

        # deja cerrar la ventana al apretar la X roja
        ventana.connect("destroy", Gtk.main_quit)

        # mostrar todo
        ventana.show_all()

    def inversa(self, boton):
        # obtener los numeros de la matriz A
        (AF1C1, AF1C2, AF1C3, AF2C1, AF2C2, AF2C3, AF3C1, AF3C2, AF3C3) = self.obtener_valores_matriz_a()

        vF1C1 = self.AF1C1.get_value()
        vF1C2 = self.AF1C2.get_value()
        vF1C3 = self.AF1C3.get_value()
        vF2C1 = self.AF2C1.get_value()
        vF2C2 = self.AF2C2.get_value()
        vF2C3 = self.AF2C3.get_value()
        vF3C1 = self.AF3C1.get_value()
        vF3C2 = self.AF3C2.get_value()
        vF3C3 = self.AF3C3.get_value()

        determinante = (vF1C1 * (vF2C2 * vF3C3 - vF2C3 * vF3C2)) - (vF1C2 * (vF2C1 * vF3C3 - vF2C3 * vF3C1)) + (vF1C3 * (vF2C1 * vF3C2 - vF2C2 * vF3C1))

        # si el determinate es distinto de cero
        # existe una matriz inversa
        if determinante != 0:
            RF1C1 = (((AF2C2 * AF3C3) - (AF3C2 * AF2C3)) / determinante)
            RF1C2 = ((((AF1C2 * AF2C3) - (AF3C2 * AF1C3)) * -1) / determinante)
            RF1C3 = (((AF1C2 * AF2C3) - (AF2C2 * AF1C3)) / determinante)
            RF2C1 = ((((AF2C1 * AF3C3) - (AF3C1 * AF2C3)) * -1) / determinante)
            RF2C2 = (((AF1C1 * AF3C3) - (AF3C1 * AF1C3)) / determinante)
            RF2C3 = ((((AF1C1 * AF2C3) - (AF2C1 * AF1C3)) * -1) / determinante)
            RF3C1 = (((AF2C1 * AF3C2) - (AF3C1 * AF2C2)) / determinante)
            RF3C2 = ((((AF1C1 * AF3C2) - (AF3C1 * AF1C2)) * -1) / determinante)
            RF3C3 = (((AF1C1 * AF2C2) - (AF2C1 * AF1C2)) / determinante)

            # a cada casilla de la matriz B de resultados
            self.BF1C1.set_value(RF1C1)
            self.BF1C2.set_value(RF1C2)
            self.BF1C3.set_value(RF1C3)
            self.BF2C1.set_value(RF2C1)
            self.BF2C2.set_value(RF2C2)
            self.BF2C3.set_value(RF2C3)
            self.BF3C1.set_value(RF3C1)
            self.BF3C2.set_value(RF3C2)
            self.BF3C3.set_value(RF3C3)

            self.titulo.set_text("matriz inversa")

        else:
            self.titulo.set_text("matriz no posee inversa")

    def transpuesta(self, boton):
        # obtener los numeros de la matriz A y Builder
        (AF1C1, AF1C2, AF1C3, AF2C1, AF2C2, AF2C3, AF3C1, AF3C2, AF3C3) = self.obtener_valores_matriz_a()

        # cambio de los numeros
        RF1C1 = AF1C1
        RF1C2 = AF2C1
        RF1C3 = AF3C1
        RF2C1 = AF1C2
        RF2C2 = AF2C2
        RF2C3 = AF3C2
        RF3C1 = AF1C3
        RF3C2 = AF2C3
        RF3C3 = AF3C3

        self.BF1C1.set_value(RF1C1)
        self.BF1C2.set_value(RF1C2)
        self.BF1C3.set_value(RF1C3)
        self.BF2C1.set_value(RF2C1)
        self.BF2C2.set_value(RF2C2)
        self.BF2C3.set_value(RF2C3)
        self.BF3C1.set_value(RF3C1)
        self.BF3C2.set_value(RF3C2)
        self.BF3C3.set_value(RF3C3)

    def borrar_todo(self, boton):
        # ponerle el numero cero a la matriz A
        self.AF1C1.set_value(0)
        self.AF1C2.set_value(0)
        self.AF1C3.set_value(0)
        self.AF2C1.set_value(0)
        self.AF2C2.set_value(0)
        self.AF2C3.set_value(0)
        self.AF3C1.set_value(0)
        self.AF3C2.set_value(0)
        self.AF3C3.set_value(0)

        # cero a los resultados
        self.BF1C1.set_value(0)
        self.BF1C2.set_value(0)
        self.BF1C3.set_value(0)
        self.BF2C1.set_value(0)
        self.BF2C2.set_value(0)
        self.BF2C3.set_value(0)
        self.BF3C1.set_value(0)
        self.BF3C2.set_value(0)
        self.BF3C3.set_value(0)

    def obtener_valores_matriz_a(self):
        # tomar el VALOR de cada cuadro de entrada de numeros
        valor_AF1C1 = self.AF1C1.get_value()
        valor_AF1C2 = self.AF1C2.get_value()
        valor_AF1C3 = self.AF1C3.get_value()
        valor_AF2C1 = self.AF2C1.get_value()
        valor_AF2C2 = self.AF2C2.get_value()
        valor_AF2C3 = self.AF2C3.get_value()
        valor_AF3C1 = self.AF3C1.get_value()
        valor_AF3C2 = self.AF3C2.get_value()
        valor_AF3C3 = self.AF3C3.get_value()

        # devolver todos los valores de la matriz A
        return (valor_AF1C1, valor_AF1C2, valor_AF1C3, valor_AF2C1, valor_AF2C2, valor_AF2C3, valor_AF3C1, valor_AF3C2, valor_AF3C3)


if __name__ == "__main__":
    w = calculadora()
    Gtk.main()

