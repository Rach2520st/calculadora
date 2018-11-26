import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
class calculadora():
    def __init__(self):
        # se crea un objeto builder para manipular Gtk
        self.builder = Gtk.Builder()
        # agregamos los objetos creados en glade
        self.builder.add_from_file("menu_princ.glade")
        # se le atribuye un valor a la ventana de menu principal en glade
        menu = self.builder.get_object("menu_pr")
        # se establece el tamaño de la ventana
        menu.set_default_size(600, 400)

        # opciones de calculadora
        # cargar los botones de las opciones
        # carga el boton
        self.s_matr = self.builder.get_object("s_matrices")
        # vincula el click con ingresar a la opcion
        self.s_matr.connect("clicked", self.suma_matrices)
        self.r_matr = self.builder.get_object("r_matrices")
        self.r_matr.connect("clicked", self.resta_matrices)
        self.m_matr = self.builder.get_object("m_matrices")
        self.m_matr.connect("clicked", self.multiplicacion_matrices)
        self.d_matr = self.builder.get_object("det_matriz")
        self.d_matr.connect("clicked", self.determinante_matriz)
        self.trans_matr = self.builder.get_object("trans_matriz")
        self.trans_matr.connect("clicked", self.matriz_transpuesta)
        menu.show_all()

    def suma_matrices(self, btn=None):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("#int_numA.glade")
        m_A = self.builder.get_object("int_numA")
        m_A.set_default_size(600, 400)

        # obtener el valor de la entrada de texto en glade
        af1c1 = self.builder.get_object("FC1C1").get_text()
        af1c2 = self.builder.get_object("F1C2").get_text()
        af1c3 = self.builder.get_object("F1C3").get_text()
        af2c1 = self.builder.get_object("F2C1").get_text()
        af2c2 = self.builder.get_object("F2C2").get_text()
        af2c3 = self.builder.get_object("F2C3").get_text()
        af3c1 = self.builder.get_object("F3C1").get_text()
        af3c2 = self.builder.get_object("F3C2").get_text()
        af3c3 = self.builder.get_object("F3C3").get_text()
        m_A.show_all()
        self.builder.add_from_file("#int_numB.glade")
        m_B = self.builder.get_object("#int_numB")

        bf1c1 = self.builder.get_object("f1c1").get_text()
        bf1c2 = self.builder.get_object("f1c2").get_text()
        bf1c3 = self.builder.get_object("f1c3").get_text()
        bf2c1 = self.builder.get_object("f2c1").get_text()
        bf2c2 = self.builder.get_object("f2c2").get_text()
        bf2c3 = self.builder.get_object("f2c3").get_text()
        bf3c1 = self.builder.get_object("f3c1").get_text()
        bf3c2 = self.builder.get_object("f3c2").get_text()
        bf3c3 = self.builder.get_object("f3c3").get_text()
        # Operacion Suma
        rf1c1 = af1c1 + bf1c1
        rf1c2 = af1c2 + bf1c2
        rf1c3 = af1c3 + bf1c3
        rf2c1 = af2c1 + bf2c1
        rf2c2 = af2c2 + bf2c2
        rf2c3 = af2c3 + bf2c3
        rf3c1 = af3c1 + bf3c1
        rf3c2 = af3c2 + bf3c2
        rf3c3 = af3c3 + bf3c3
        self.builder.get_object("resultados.glade")
        # ingresa el resultado de la suma en la matriz resultado
        self.r_f1c1.set_text(rf1c1)
        self.r_f1c2.set_text(rf1c2)
        self.r_f1c3.set_text(rf1c3)
        self.r_f2c1.set_text(rf2c1)
        self.r_f2c2.set_text(rf2c2)
        self.r_f2c3.set_text(rf2c3)
        self.r_f3c1.set_text(rf3c1)
        self.r_f3c2.set_text(rf3c2)
        self.r_f3c3.set_text(rf3c3)

    def resta_matrices(self, btn=None):
        self.builder.add_from_file("#int_numA.glade")
        m_A = self.builder.get_object("int_numA")
        # obtener el valor de la entrada de texto en glade
        af1c1 = self.builder.get_object("FC1C1").get_text()
        af1c2 = self.builder.get_object("F1C2").get_text()
        af1c3 = self.builder.get_object("F1C3").get_text()
        af2c1 = self.builder.get_object("F2C1").get_text()
        af2c2 = self.builder.get_object("F2C2").get_text()
        af2c3 = self.builder.get_object("F2C3").get_text()
        af3c1 = self.builder.get_object("F3C1").get_text()
        af3c2 = self.builder.get_object("F3C2").get_text()
        af3c3 = self.builder.get_object("F3C3").get_text()

        self.builder.add_from_file("#int_numB.glade")
        m_B = self.builder.get_object("#int_numB")

        bf1c1 = self.builder.get_object("f1c1").get_text()
        bf1c2 = self.builder.get_object("f1c2").get_text()
        bf1c3 = self.builder.get_object("f1c3").get_text()
        bf2c1 = self.builder.get_object("f2c1").get_text()
        bf2c2 = self.builder.get_object("f2c2").get_text()
        bf2c3 = self.builder.get_object("f2c3").get_text()
        bf3c1 = self.builder.get_object("f3c1").get_text()
        bf3c2 = self.builder.get_object("f3c2").get_text()
        bf3c3 = self.builder.get_object("f3c3").get_text()
        # Operacion resta
        rf1c1 = af1c1 - bf1c1
        rf1c2 = af1c2 - bf1c2
        rf1c3 = af1c3 - bf1c3
        rf2c1 = af2c1 - bf2c1
        rf2c2 = af2c2 - bf2c2
        rf2c3 = af2c3 - bf2c3
        rf3c1 = af3c1 - bf3c1
        rf3c2 = af3c2 - bf3c2
        rf3c3 = af3c3 - bf3c3
        self.builder.get_object("resultados.glade")
        # ingresa el resultado de la resta en la matriz resultado
        self.r_f1c1.set_text(rf1c1)
        self.r_f1c2.set_text(rf1c2)
        self.r_f1c3.set_text(rf1c3)
        self.r_f2c1.set_text(rf2c1)
        self.r_f2c2.set_text(rf2c2)
        self.r_f2c3.set_text(rf2c3)
        self.r_f3c1.set_text(rf3c1)
        self.r_f3c2.set_text(rf3c2)
        self.r_f3c3.set_text(rf3c3)
    def multiplicacion_matrices(self, btn=None):
        self.builder.add_from_file("#int_numA.glade")
        m_A = self.builder.get_object("int_numA")
        
        af1c1 = self.builder.get_object("FC1C1").get_text()
        af1c2 = self.builder.get_object("F1C2").get_text()
        af1c3 = self.builder.get_object("F1C3").get_text()
        af2c1 = self.builder.get_object("F2C1").get_text()
        af2c2 = self.builder.get_object("F2C2").get_text()
        af2c3 = self.builder.get_object("F2C3").get_text()
        af3c1 = self.builder.get_object("F3C1").get_text()
        af3c2 = self.builder.get_object("F3C2").get_text()
        af3c3 = self.builder.get_object("F3C3").get_text()

        self.builder.add_from_file("#int_numB.glade")
        m_B = self.builder.get_object("#int_numB")

        bf1c1 = self.builder.get_object("f1c1").get_text()
        bf1c2 = self.builder.get_object("f1c2").get_text()
        bf1c3 = self.builder.get_object("f1c3").get_text()
        bf2c1 = self.builder.get_object("f2c1").get_text()
        bf2c2 = self.builder.get_object("f2c2").get_text()
        bf2c3 = self.builder.get_object("f2c3").get_text()
        bf3c1 = self.builder.get_object("f3c1").get_text()
        bf3c2 = self.builder.get_object("f3c2").get_text()
        bf3c3 = self.builder.get_object("f3c3").get_text()
        # Operacion Multiplicacion
        rf1c1 = (af1c1 * bf1c1) + (af1c2 * bf2c1) + (af1c3 * bf3c1)
        rf1c2 = (af1c1 * bf1c2) + (af1c2 * bf2c2) + (af1c3 * bf3c2)
        rf1c3 = (af1c1 * bf1c3) + (af1c2 * bf2c3) + (af1c3 * bf3c3)
        rf2c1 = (af2c1 * bf1c1) + (af2c2 * bf2c1) + (af2c3 * bf3c1)
        rf2c2 = (af2c1 * bf1c2) + (af2c2 * bf2c2) + (af2c3 * bf3c2)
        rf2c3 = (af2c1 * bf1c3) + (af2c2 * bf2c3) + (af2c3 * bf3c3)
        rf3c1 = (af3c1 * bf1c1) + (af3c2 * bf2c1) + (af3c3 * bf3c1)
        rf3c2 = (af3c1 * bf1c2) + (af3c2 * bf2c2) + (af3c3 * bf3c2)
        rf3c3 = (af3c1 * bf1c3) + (af3c2 * bf2c3) + (af3c3 * bf3c3)
        self.builder.get_object("resultados.glade")
        # ingresa el resultado de la multiplicación de la matriz en la matriz resultado
        self.r_f1c1.set_text(rf1c1)
        self.r_f1c2.set_text(rf1c2)
        self.r_f1c3.set_text(rf1c3)
        self.r_f2c1.set_text(rf2c1)
        self.r_f2c2.set_text(rf2c2)
        self.r_f2c3.set_text(rf2c3)
        self.r_f3c1.set_text(rf3c1)
        self.r_f3c2.set_text(rf3c2)
        self.r_f3c3.set_text(rf3c3)
    def determinante_matriz(self, dtn=None):
        self.builder.add_from_file("#int_numA.glade")
        m_A = self.builder.get_object("int_numA")
        af1c1 = self.builder.get_object("FC1C1").get_text()
        af1c2 = self.builder.get_object("F1C2").get_text()
        af1c3 = self.builder.get_object("F1C3").get_text()
        af2c1 = self.builder.get_object("F2C1").get_text()
        af2c2 = self.builder.get_object("F2C2").get_text()
        af2c3 = self.builder.get_object("F2C3").get_text()
        af3c1 = self.builder.get_object("F3C1").get_text()
        af3c2 = self.builder.get_object("F3C2").get_text()
        af3c3 = self.builder.get_object("F3C3").get_text()

        determinante = ((af1c1 * ((af2c2 * af3c3) - 0(af2c3 * af3c2))) - (af1c2 * ((af2c1 * af3c3) - (af2c3 * af3c1))) + (af1c3 * ((af2c1 * af3c2) - (af2c2 * af3c1))))

        self.builder.add_from_file("resultados_DET.glade")
        self.resultado_determinante.set_text(determinante)

    def matriz_transpuesta(self, dtn=None):
        self.builder.add_from_file("#int_numA.glade")
        m_A = self.builder.get_object("int_numA")
        af1c1 = self.builder.get_object("FC1C1").get_text()
        af1c2 = self.builder.get_object("F1C2").get_text()
        af1c3 = self.builder.get_object("F1C3").get_text()
        af2c1 = self.builder.get_object("F2C1").get_text()
        af2c2 = self.builder.get_object("F2C2").get_text()
        af2c3 = self.builder.get_object("F2C3").get_text()
        af3c1 = self.builder.get_object("F3C1").get_text()
        af3c2 = self.builder.get_object("F3C2").get_text()
        af3c3 = self.builder.get_object("F3C3").get_text()

        rf1c1 = af1c1
        rf1c2 = af2c1
        rf1c3 = af3c1
        rf2c1 = af1c2
        rf2c2 = af2c2
        rf2c3 = af3c2
        rf3c1 = af1c3
        rf3c2 = af2c3
        rf3c3 = af3c3

        self.builder.get_object("resultados.glade")
        # ingresa el resultado de la matriz transpuesta a la matriz resultado
        self.r_f1c1.set_text(rf1c1)
        self.r_f1c2.set_text(rf1c2)
        self.r_f1c3.set_text(rf1c3)
        self.r_f2c1.set_text(rf2c1)
        self.r_f2c2.set_text(rf2c2)
        self.r_f2c3.set_text(rf2c3)
        self.r_f3c1.set_text(rf3c1)
        self.r_f3c2.set_text(rf3c2)
        self.r_f3c3.set_text(rf3c3)

if __name__ == "__main__":
    w = calculadora()
    Gtk.main()
