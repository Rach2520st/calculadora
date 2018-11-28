import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk


class calculadora:
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

    def suma_matrices(self, event):
        ventana_suma()


class ventana_suma:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("suma_matrices.glade")
        ventana = self.builder.get_object("ventana_suma_matrices")

        # deja cerrar la ventana al apretar la X roja
        ventana.connect("destroy", Gtk.main_quit)
        # mostrar todo
        ventana.show_all()

    def obtener_matriz_a(self):
        # tomar el valor de cada cuadradito
        AF1C1 = self.builder.get_object("AF1C1").get_value()
        AF1C2 = self.builder.get_object("AF1C2").get_value()
        AF1C3 = self.builder.get_object("AF1C3").get_value()
        AF2C1 = self.builder.get_object("AF2C1").get_value()
        AF2C2 = self.builder.get_object("AF2C2").get_value()
        AF2C3 = self.builder.get_object("AF2C3").get_value()
        AF3C1 = self.builder.get_object("AF3C1").get_value()
        AF3C2 = self.builder.get_object("AF3C2").get_value()
        AF3C3 = self.builder.get_object("AF3C3").get_value()

        # devolver todos los valores
        return (AF1C1, AF1C2, AF1C3, AF2C1, AF2C2, AF2C3, AF3C1, AF3C2, AF3C3)

    def obtener_matriz_b(self):
        BF1C1 = self.builder.get_object("BF1C1").get_value()
        BF1C2 = self.builder.get_object("BF1C2").get_value()
        BF1C3 = self.builder.get_object("BF1C3").get_value()
        BF2C1 = self.builder.get_object("BF2C1").get_value()
        BF2C2 = self.builder.get_object("BF2C2").get_value()
        BF2C3 = self.builder.get_object("BF2C3").get_value()
        BF3C1 = self.builder.get_object("BF3C1").get_value()
        BF3C2 = self.builder.get_object("BF3C2").get_value()
        BF3C3 = self.builder.get_object("BF3C3").get_value()

        return (BF1C1, BF1C2, BF1C3, BF2C1, BF2C2, BF2C3, BF3C1, BF3C2, BF3C3)

    def obtener_matriz_c(self):
        CF1C1 = self.builder.get_object("CF1C1").get_value()
        CF1C2 = self.builder.get_object("CF1C2").get_value()
        CF1C3 = self.builder.get_object("CF1C3").get_value()
        CF2C1 = self.builder.get_object("CF2C1").get_value()
        CF2C2 = self.builder.get_object("CF2C2").get_value()
        CF2C3 = self.builder.get_object("CF2C3").get_value()
        CF3C1 = self.builder.get_object("CF3C1").get_value()
        CF3C2 = self.builder.get_object("CF3C2").get_value()
        CF3C3 = self.builder.get_object("CF3C3").get_value()

        return (CF1C1, CF1C2, CF1C3, CF2C1, CF2C2, CF2C3, CF3C1, CF3C2, CF3C3)
