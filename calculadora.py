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
        self.inver_matr = self.builder.get_object("inver_matriz")
        self.inver_matr.connect("clicked", self.matriz_inversa)
        menu.show_all()

    def suma_matrices(self, btn=None):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("#int_numA.glade")
        m_A = self.builder.get_object("int_numA")
        m_A.set_default_size(600, 400)
        #añade el boton siguiente que hace que aparezca la matriz B
        self.si_matriz = self.builder.get_object("siguiente_A")
        self.si_matriz.connect("clicked", self.sig_matriz)

        # obtener el valor de la entrada de texto en glade
        af1c1 = self.builder.get_object("F1C1").get_value()
        af1c2 = self.builder.get_object("F1C2").get_value()
        af1c3 = self.builder.get_object("F1C3").get_value()
        af2c1 = self.builder.get_object("F2C1").get_value()
        af2c2 = self.builder.get_object("F2C2").get_value()
        af2c3 = self.builder.get_object("F2C3").get_value()
        af3c1 = self.builder.get_object("F3C1").get_value()
        af3c2 = self.builder.get_object("F3C2").get_value()
        af3c3 = self.builder.get_object("F3C3").get_value()
        m_A.show_all()
        
        
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
        self.r_f1c1.set_text(rf1c1)
        self.r_f1c2.set_text(rf1c2)
        self.r_f1c3.set_text(rf1c3)
        self.r_f2c1.set_text(rf2c1)
        self.r_f2c2.set_text(rf2c2)
        self.r_f2c3.set_text(rf2c3)
        self.r_f3c1.set_text(rf3c1)
        self.r_f3c2.set_text(rf3c2)
        self.r_f3c3.set_text(rf3c3)
    def sig_matriz(self, btn=None):

        self.builder = Gtk.Builder()
        self.builder.add_from_file("#int_numB.glade")
        m_B = self.builder.get_object("int_numB")
        m_B.set_default_size(600, 400)
     

        bf1c1 = self.builder.get_object("f1c1").get_value()
        bf1c2 = self.builder.get_object("f1c2").get_value()
        bf1c3 = self.builder.get_object("f1c3").get_value()
        bf2c1 = self.builder.get_object("f2c1").get_value()
        bf2c2 = self.builder.get_object("f2c2").get_value()
        bf2c3 = self.builder.get_object("f2c3").get_value()
        bf3c1 = self.builder.get_object("f3c1").get_value()
        bf3c2 = self.builder.get_object("f3c2").get_value()
        bf3c3 = self.builder.get_object("f3c3").get_value()
        m_B.show_all()

    def resta_matrices(self, btn=None):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("#int_numA.glade")
        m_A = self.builder.get_object("int_numA")
        m_A.set_default_size(600, 400)
        
        # obtener el valor de la entrada de texto en glade
        af1c1 = self.builder.get_object("F1C1").get_value()
        af1c2 = self.builder.get_object("F1C2").get_value()
        af1c3 = self.builder.get_object("F1C3").get_value()
        af2c1 = self.builder.get_object("F2C1").get_value()
        af2c2 = self.builder.get_object("F2C2").get_value()
        af2c3 = self.builder.get_object("F2C3").get_value()
        af3c1 = self.builder.get_object("F3C1").get_value()
        af3c2 = self.builder.get_object("F3C2").get_value()
        af3c3 = self.builder.get_object("F3C3").get_value()
        m_A.show_all()

        self.builder.add_from_file("#int_numB.glade")
        m_B = self.builder.get_object("#int_numB")

        bf1c1 = self.builder.get_object("f1c1").get_value()
        bf1c2 = self.builder.get_object("f1c2").get_value()
        bf1c3 = self.builder.get_object("f1c3").get_value()
        bf2c1 = self.builder.get_object("f2c1").get_value()
        bf2c2 = self.builder.get_object("f2c2").get_value()
        bf2c3 = self.builder.get_object("f2c3").get_value()
        bf3c1 = self.builder.get_object("f3c1").get_value()
        bf3c2 = self.builder.get_object("f3c2").get_value()
        bf3c3 = self.builder.get_object("f3c3").get_value()
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
        self.builder = Gtk.Builder()
        self.builder.add_from_file("#int_numA.glade")
        m_A = self.builder.get_object("int_numA")
        m_A.set_default_size(600, 400)
        
        af1c1 = self.builder.get_object("F1C1").get_value()
        af1c2 = self.builder.get_object("F1C2").get_value()
        af1c3 = self.builder.get_object("F1C3").get_value()
        af2c1 = self.builder.get_object("F2C1").get_value()
        af2c2 = self.builder.get_object("F2C2").get_value()
        af2c3 = self.builder.get_object("F2C3").get_value()
        af3c1 = self.builder.get_object("F3C1").get_value()
        af3c2 = self.builder.get_object("F3C2").get_value()
        af3c3 = self.builder.get_object("F3C3").get_value()
        m_A.show_all()

        self.builder.add_from_file("#int_numB.glade")
        m_B = self.builder.get_object("#int_numB")

        bf1c1 = self.builder.get_object("f1c1").get_value()
        bf1c2 = self.builder.get_object("f1c2").get_value()
        bf1c3 = self.builder.get_object("f1c3").get_value()
        bf2c1 = self.builder.get_object("f2c1").get_value()
        bf2c2 = self.builder.get_object("f2c2").get_value()
        bf2c3 = self.builder.get_object("f2c3").get_value()
        bf3c1 = self.builder.get_object("f3c1").get_value()
        bf3c2 = self.builder.get_object("f3c2").get_value()
        bf3c3 = self.builder.get_object("f3c3").get_value()
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
        
        self.builder = Gtk.Builder()
        self.builder.add_from_file("#int_numA.glade")
        m_A = self.builder.get_object("int_numA")
        m_A.set_default_size(600, 400)
        
        af1c1 = self.builder.get_object("F1C1").get_value()
        af1c2 = self.builder.get_object("F1C2").get_value()
        af1c3 = self.builder.get_object("F1C3").get_value()
        af2c1 = self.builder.get_object("F2C1").get_value()
        af2c2 = self.builder.get_object("F2C2").get_value()
        af2c3 = self.builder.get_object("F2C3").get_value()
        af3c1 = self.builder.get_object("F3C1").get_value()
        af3c2 = self.builder.get_object("F3C2").get_value()
        af3c3 = self.builder.get_object("F3C3").get_value()
        m_A.show_all()

        determinante = ((af1c1 * ((af2c2 * af3c3) - 0(af2c3 * af3c2))) - (af1c2 * ((af2c1 * af3c3) - (af2c3 * af3c1))) + (af1c3 * ((af2c1 * af3c2) - (af2c2 * af3c1))))

        self.builder.add_from_file("resultados_DET.glade")
        self.resultado_determinante.set_text(determinante)
    def matriz_transpuesta(self, dtn=None):
        
        self.builder = Gtk.Builder()
        self.builder.add_from_file("#int_numA.glade")
        m_A = self.builder.get_object("int_numA")
        m_A.set_default_size(600, 400)

        af1c1 = self.builder.get_object("F1C1").get_value()
        af1c2 = self.builder.get_object("F1C2").get_value()
        af1c3 = self.builder.get_object("F1C3").get_value()
        af2c1 = self.builder.get_object("F2C1").get_value()
        af2c2 = self.builder.get_object("F2C2").get_value()
        af2c3 = self.builder.get_object("F2C3").get_value()
        af3c1 = self.builder.get_object("F3C1").get_value()
        af3c2 = self.builder.get_object("F3C2").get_value()
        af3c3 = self.builder.get_object("F3C3").get_value()
        m_A.show_all()

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
    def matriz_inversa(self, dtn=None):
        
        self.builder = Gtk.Builder()
        self.builder.add_from_file("#int_numA.glade")
        m_A = self.builder.get_object("int_numA")
        m_A.set_default_size(600, 400)
        
        af1c1 = self.builder.get_object("F1C1").get_value()
        af1c2 = self.builder.get_object("F1C2").get_value()
        af1c3 = self.builder.get_object("F1C3").get_value()
        af2c1 = self.builder.get_object("F2C1").get_value()
        af2c2 = self.builder.get_object("F2C2").get_value()
        af2c3 = self.builder.get_object("F2C3").get_value()
        af3c1 = self.builder.get_object("F3C1").get_value()
        af3c2 = self.builder.get_object("F3C2").get_value()
        af3c3 = self.builder.get_object("F3C3").get_value()
        m_A.show_all()
        
        determinante = ((af1c1 * ((af2c2 * af3c3) - 0(af2c3 * af3c2))) - (af1c2 * ((af2c1 * af3c3) - (af2c3 * af3c1))) + (af1c3 * ((af2c1 * af3c2) - (af2c2 * af3c1))))
        # si el determinate es distinto de cero
        # existe una matriz inversa
        if determinante != 0:
            rf1c1 = (af2c2*af3c3-af3c2*af2c3)/determinante
            rf1c2 = ((af1c2*af3c3-af3c2*af1c3)*-1)/determinante
            rf1c3 = (af1c2*af2c3-af2c2*af1c3)/determinante
            rf2c1 = ((af2c1*af3c3-af3c1*af2c3)*-1)/determinante
            rf2c2 = ((af1c1*af3c3-af3c1*af1c3))/determinante
            rf2c3 = ((af1c1*af2c3-af2c1*af1c3)*-1)/determinante
            rf3c1 = ((af2c1*af3c2-af3c1*af2c2))/determinante
            rf3c2 = ((af1c1*af3c2-af3c1*af1c2)*-1)/determinante
            rf3c3 = (af1c1*af2c2-af2c1*af1c2)/determinante

            self.builder.get_object("resultados.glade")
            # ingresa el resultado de la matriz inversa a la matriz resultado
            self.r_f1c1.set_text(rf1c1)
            self.r_f1c2.set_text(rf1c2)
            self.r_f1c3.set_text(rf1c3)
            self.r_f2c1.set_text(rf2c1)
            self.r_f2c2.set_text(rf2c2)
            self.r_f2c3.set_text(rf2c3)
            self.r_f3c1.set_text(rf3c1)
            self.r_f3c2.set_text(rf3c2)
            self.r_f3c3.set_text(rf3c3)
        else:
            self.builder.add_from_file("resultados_DET.glade")
            self.resultado_determinante.set_text("esta matriz no posee inversa")    
            


if __name__ == "__main__":
    w = calculadora()
    Gtk.main()
