from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from db import Database
from tkinter import messagebox
import tkinter.font

db = Database('maq.db')
rows = db.fetch()
rowssmall = db.smallfetch

mainwin=Tk()
mainwin.maxsize= (1000, 1000)
mainwin.title('Registro')
mainwin.configure(bg='white')

my_font = tkinter.font.Font(family="Arial Black", size=12)
my_fonts = tkinter.font.Font(family="Arial Black", size=10)
my_fontb = tkinter.font.Font(family="Arial Black", size=12, underline=True)
my_fontdisplay = tkinter.font.Font(family="Arial Black", size=8)

global thisid
thisid = 0

for row in db.fetch():
    thisid = thisid + 1
global capacidadcuchara
capacidadcuchara = 0.0
global cuchara
cuchara = ""
global flag1
flag1 = 1
global flag_ingresar_excavadora
flag_ingresar_excavadora = 0
global flag_mostrar_detalles
flag_mostrar_detalles = 0
global flag_eliminar
flag_eliminar = 0
print(thisid)

# crear un frame y poner la tabla ahi, luego borrar el frame

table_frame_buttons = Frame(mainwin, padx = 3)
table_frame_buttons.config(bg='white')

# small_table_frame = Frame(mainwin, width = 700, height = 200, padx = 3)
# small_table_frame.config(bg='white')

table_frame = Frame(mainwin, padx = 3)
table_frame.config(bg='white')

table_frame_buttons.pack(side='top')
# small_table_frame.pack(side='bottom')
table_frame.pack(side='bottom')

# ocultar los frames
# small_table_frame.pack_forget()

tree = ttk.Treeview(table_frame)
# tree2 = ttk.Treeview(table_frame)

def small_populate_list():

    # small_table_frame.grid()
    

    # marco1_label = Label(small_table_frame, text='Excavadora', font=my_fontdisplay)
    # marco1_label.config(bg='white')
    # marco1_label.grid(row=1, column=1, sticky=W)
    # marco2_label = Label(small_table_frame, text='Cuchara', font=my_fontdisplay)
    # marco2_label.config(bg='white')
    # marco2_label.grid(row=1, column=2, sticky=W)
    # marco3_label = Label(small_table_frame, text='Productividad', font=my_fontdisplay)
    # marco3_label.config(bg='white')
    # marco3_label.grid(row=1, column=3, sticky=W)
    # marco4_label = Label(small_table_frame, text='Rendimiento', font=my_fontdisplay)
    # marco4_label.config(bg='white')
    # marco4_label.grid(row=1, column=4, sticky=W)
    # i = 2
    # for row in db.smallfetch():
    #     try:
    #         n = 0
    #         for j in range(len(row)):
    #             e = Text(small_table_frame, width=16, height=2, fg='black', font=my_fontdisplay, wrap=None)
    #             e.grid(row=i, column=j)
    #             if n == 0:
    #                 e.config(width=4)
    #                 e.insert(END, row[j])
    #             elif n == 1 or n == 2:
    #                 e.config(width=13)
    #                 e.insert(END, row[j])
    #             else:
    #                 e.config(width=10)
    #                 e.insert(END, round(float(str(row[j])), 2))
    #             n = n + 1
    #         i=i+1
    #     except IndexError:
    #         pass

    # tree = ttk.Treeview(table_frame)

    # Definir las columnas y los encabezados personalizados
    tree.column('#0', width=1)
    headers = ['ID', 'Tipo de excavadora', 'Tipo de cuchara', 'Productividad', 'Rendimiento']
    tree['columns'] = list(range(len(headers)))
    for i, header in enumerate(headers):
        tree.heading(i, text=header, anchor='center')

    # Agregar las filas de datos
    for row in rows[0:]:
        tree.insert('', 'end', values=row)

    # Crear una barra de desplazamiento
    scrollbar = ttk.Scrollbar(table_frame, orient='vertical', command=tree.yview)
    tree.config(yscrollcommand=scrollbar.set)

    # Agregar la tabla y la barra de desplazamiento al marco
    tree.pack(side='left', fill='both', expand=True)
    tree.pack()
    scrollbar.pack(side='right', fill='y')

    # Configurar los encabezados para que encajen horizontalmente
    for i, header in enumerate(headers):
        tree.heading(i, text=header, anchor=CENTER)
        tree.column(i, anchor=CENTER)

    tree.column(0, width=1)
    tree.column(1, width=200)
    tree.column(2, width=150)
    tree.column(3, width=120)
    tree.column(4, width=180)

    mainwin.update_idletasks()

# def populate_list():
    
#     # table_frame.grid()

#     # table_frame.pack()

#     # marco1_label = Label(table_frame, text='Excavadora', font=my_fontdisplay)
#     # marco1_label.config(bg='white')
#     # marco1_label.grid(row=1, column=1, sticky=W)
#     # marco2_label = Label(table_frame, text='Excavacion', font=my_fontdisplay)
#     # marco2_label.config(bg='white')
#     # marco2_label.grid(row=1, column=2, sticky=W)
#     # marco3_label = Label(table_frame, text='Balanceo', font=my_fontdisplay)
#     # marco3_label.config(bg='white')
#     # marco3_label.grid(row=1, column=3, sticky=W)
#     # marco4_label = Label(table_frame, text='Carga', font=my_fontdisplay)
#     # marco4_label.config(bg='white')
#     # marco4_label.grid(row=1, column=4, sticky=W)
#     # marco5_label = Label(table_frame, text='Tiempo de carga', font=my_fontdisplay)
#     # marco5_label.config(bg='white')
#     # marco5_label.grid(row=1, column=5, sticky=W)
#     # marco6_label = Label(table_frame, text='Cuchara', font=my_fontdisplay)
#     # marco6_label.config(bg='white')
#     # marco6_label.grid(row=1, column=6, sticky=W)
#     # marco7_label = Label(table_frame, text='Eficiencia', font=my_fontdisplay)
#     # marco7_label.config(bg='white')
#     # marco7_label.grid(row=1, column=7, sticky=W)
#     # marco8_label = Label(table_frame, text='Capacidad de cuchara', font=my_fontdisplay, wraplength=100)
#     # marco8_label.config(bg='white')
#     # marco8_label.grid(row=1, column=8, sticky=W)
#     # marco9_label = Label(table_frame, text='Capacidad neta', font=my_fontdisplay)
#     # marco9_label.config(bg='white')
#     # marco9_label.grid(row=1, column=9, sticky=W)
#     # marco10_label = Label(table_frame, text='Alto', font=my_fontdisplay)
#     # marco10_label.config(bg='white')
#     # marco10_label.grid(row=1, column=10, sticky=W)
#     # marco11_label = Label(table_frame, text='Ancho', font=my_fontdisplay)
#     # marco11_label.config(bg='white')
#     # marco11_label.grid(row=1, column=11, sticky=W)
#     # marco12_label = Label(table_frame, text='Largo', font=my_fontdisplay)
#     # marco12_label.config(bg='white')
#     # marco12_label.grid(row=1, column=12, sticky=W)
#     # marco13_label = Label(table_frame, text='Volumen', font=my_fontdisplay)
#     # marco13_label.config(bg='white')
#     # marco13_label.grid(row=1, column=13, sticky=W)
#     # marco14_label = Label(table_frame, text='Sobreexcavacion', font=my_fontdisplay)
#     # marco14_label.config(bg='white')
#     # marco14_label.grid(row=1, column=14, sticky=W)
#     # marco15_label = Label(table_frame, text='Tiempo de alquiler', font=my_fontdisplay)
#     # marco15_label.config(bg='white')
#     # marco15_label.grid(row=1, column=15, sticky=W)
#     # marco16_label = Label(table_frame, text='Numero de ciclos por hora', font=my_fontdisplay)
#     # marco16_label.config(bg='white')
#     # marco16_label.grid(row=1, column=16, sticky=W)
#     # marco17_label = Label(table_frame, text='Productividad', font=my_fontdisplay)
#     # marco17_label.config(bg='white')
#     # marco17_label.grid(row=1, column=17, sticky=W)
#     # marco18_label = Label(table_frame, text='Rendimiento', font=my_fontdisplay)
#     # marco18_label.config(bg='white')
#     # marco18_label.grid(row=1, column=18, sticky=W)
#     # i = 2
#     # for row in db.fetch():
#     #     try:
#     #         n = 0
#     #         for j in range(len(row)):
#     #             e = Text(table_frame, width=16, height=2, fg='black', font=my_fontdisplay, wrap=None)
#     #             e.grid(row=i, column=j)
#     #             if n == 0:
#     #                 e.config(width=4)
#     #                 e.insert(END, row[j])
#     #             elif n == 1 or n == 6:
#     #                 e.config(width=13)
#     #                 e.insert(END, row[j])
#     #             else:
#     #                 e.config(width=10)
#     #                 e.insert(END, round(float(str(row[j])), 2))
#     #             n = n + 1
#     #         i=i+1
#     #         vacio_label = Label(table_frame, text='', font=my_font, pady=10, padx=10)
#     #         vacio_label.config(bg='white')
#     #         vacio_label.grid(row=i, column=0)
#     #     except IndexError:
#     #         pass

#     # tree2 = ttk.Treeview(table_frame)

#     # Definir las columnas y los encabezados personalizados
#     headers2 = ['ID', 'Tipo de excavadora', 'Tipo de excavación', 'Tipo de balanceo', 'Tipo de carga', 'Tiempo de carga', 'Tipo de cuchara', 'Eficiencia', 'Capacidad de la cuchara', 'Capacidad neta', 'Altura', 'Anchura', 'Longitud', 'Volumen de excavación', 'Sobreexcavación', 'Tiempo de alquiler', 'Número de ciclos por hora', 'Productividad', 'Rendimiento']
#     tree2['columns'] = list(range(len(headers2)))
#     tree2.column('#0', width=1)
#     for i, header in enumerate(headers2):
#         tree2.heading(i, text=header, anchor='center')
#         tree2.column(i, width=[50, 150, 150, 150, 150, 100, 150, 100, 150, 100, 100, 100, 100, 150, 150, 150, 150, 100, 100][i], anchor='center')

#     # Agregar las filas de datos
#     for row in rows[0:]:
#         tree2.insert('', 'end', values=row)

#     # Crear una barra de desplazamiento
#     scrollbar2 = ttk.Scrollbar(table_frame, orient='vertical', command=tree2.yview)
#     tree2.config(yscrollcommand=scrollbar2.set)

#     # Agregar la tabla y la barra de desplazamiento al marco
#     tree2.pack(side='left', fill='both', expand=True)
#     scrollbar2.pack(side='right', fill='y')

#     # Configurar los encabezados para que encajen horizontalmente
#     for i, header in enumerate(headers2):
#         tree2.heading(i, text=header, anchor=CENTER)
#         tree2.column(i, anchor=CENTER)

#     tree2.pack_forget()
#     scrollbar2.pack_forget()

# def new_small_populate_list():
#     small_table_frame = Frame(mainwin, width = 1000, height = 200, padx = 3)

#     # small_table_frame.grid(row=1, sticky="ns")

#     small_table_frame.pack(side='bottom')

#     marco1_label = Label(small_table_frame, text='Excavadora', font=my_fontdisplay)
#     marco1_label.grid(row=1, column=1, sticky=W)
#     marco2_label = Label(small_table_frame, text='Cuchara', font=my_fontdisplay)
#     marco2_label.grid(row=1, column=2, sticky=W)
#     marco3_label = Label(small_table_frame, text='Productividad', font=my_fontdisplay)
#     marco3_label.grid(row=1, column=3, sticky=W)
#     marco4_label = Label(small_table_frame, text='Rendimiento', font=my_fontdisplay)
#     marco4_label.grid(row=1, column=4, sticky=W)
#     i = 2
#     for row in db.smallfetch():
#         try:
#             n = 0
#             for j in range(len(row)):
#                 e = Text(small_table_frame, width=16, height=2, fg='black', font=my_fontdisplay, wrap=None)
#                 e.grid(row=i, column=j)
#                 if n == 0:
#                     e.config(width=4)
#                     e.insert(END, row[j])
#                 elif n == 1 or n == 2:
#                     e.config(width=13)
#                     e.insert(END, row[j])
#                 else:
#                     e.config(width=10)
#                     e.insert(END, round(float(str(row[j])), 2))

#                 e.insert(END, row[j])
#                 n = n + 1
#             i=i+1
#         except IndexError:
#             pass

# def new_populate_list():
#     table_frame = Frame(mainwin, width = 1000, height = 200, padx = 3)
#     table_frame.grid(row=1, sticky="ns")
#     # table_frame.grid_remove()
#     # excavadora, excavacion, balanceo, carga, tiempocarga, cuchara, eficiencia, capacidadcuchara, capacidadneta, alto, ancho, largo, volumen, sobreexcavacion, tiempoalquiler, numerocicloshora, productividad, rendimiento
#     # table_frame.grid()
#     marco1_label = Label(table_frame, text='Excavadora', font=my_fontdisplay)
#     marco1_label.config(bg='white')
#     marco1_label.grid(row=1, column=1, sticky=W)
#     marco2_label = Label(table_frame, text='Excavacion', font=my_fontdisplay)
#     marco2_label.config(bg='white')
#     marco2_label.grid(row=1, column=2, sticky=W)
#     marco3_label = Label(table_frame, text='Balanceo', font=my_fontdisplay)
#     marco3_label.config(bg='white')
#     marco3_label.grid(row=1, column=3, sticky=W)
#     marco4_label = Label(table_frame, text='Carga', font=my_fontdisplay)
#     marco4_label.config(bg='white')
#     marco4_label.grid(row=1, column=4, sticky=W)
#     marco5_label = Label(table_frame, text='Tiempo de carga', font=my_fontdisplay)
#     marco5_label.config(bg='white')
#     marco5_label.grid(row=1, column=5, sticky=W)
#     marco6_label = Label(table_frame, text='Cuchara', font=my_fontdisplay)
#     marco6_label.config(bg='white')
#     marco6_label.grid(row=1, column=6, sticky=W)
#     marco7_label = Label(table_frame, text='Eficiencia', font=my_fontdisplay)
#     marco7_label.config(bg='white')
#     marco7_label.grid(row=1, column=7, sticky=W)
#     marco8_label = Label(table_frame, text='Capacidad de cuchara', font=my_fontdisplay, wraplength=100)
#     marco8_label.config(bg='white')
#     marco8_label.grid(row=1, column=8, sticky=W)
#     marco9_label = Label(table_frame, text='Capacidad neta', font=my_fontdisplay)
#     marco9_label.config(bg='white')
#     marco9_label.grid(row=1, column=9, sticky=W)
#     marco10_label = Label(table_frame, text='Alto', font=my_fontdisplay)
#     marco10_label.config(bg='white')
#     marco10_label.grid(row=1, column=10, sticky=W)
#     marco11_label = Label(table_frame, text='Ancho', font=my_fontdisplay)
#     marco11_label.config(bg='white')
#     marco11_label.grid(row=1, column=11, sticky=W)
#     marco12_label = Label(table_frame, text='Largo', font=my_fontdisplay)
#     marco12_label.config(bg='white')
#     marco12_label.grid(row=1, column=12, sticky=W)
#     marco13_label = Label(table_frame, text='Volumen', font=my_fontdisplay)
#     marco13_label.config(bg='white')
#     marco13_label.grid(row=1, column=13, sticky=W)
#     marco14_label = Label(table_frame, text='Sobreexcavacion', font=my_fontdisplay)
#     marco14_label.config(bg='white')
#     marco14_label.grid(row=1, column=14, sticky=W)
#     marco15_label = Label(table_frame, text='Tiempo de alquiler', font=my_fontdisplay)
#     marco15_label.config(bg='white')
#     marco15_label.grid(row=1, column=15, sticky=W)
#     marco16_label = Label(table_frame, text='Numero de ciclos por hora', font=my_fontdisplay)
#     marco16_label.config(bg='white')
#     marco16_label.grid(row=1, column=16, sticky=W)
#     marco17_label = Label(table_frame, text='Productividad', font=my_fontdisplay)
#     marco17_label.config(bg='white')
#     marco17_label.grid(row=1, column=17, sticky=W)
#     marco18_label = Label(table_frame, text='Rendimiento', font=my_fontdisplay)
#     marco18_label.config(bg='white')
#     marco18_label.grid(row=1, column=18, sticky=W)
#     i = 2
#     for row in db.fetch():
#         try:
#             n = 0
#             for j in range(len(row)):
#                 e = Text(table_frame, width=16, height=2, fg='black', font=my_fontdisplay, wrap=None)
#                 e.grid(row=i, column=j)
#                 # if n == 0 or n == 1 or n == 6:
#                 if n == 0:
#                     e.config(width=4)
#                     e.insert(END, row[j])
#                 elif n == 1 or n == 6:
#                     e.config(width=13)
#                     e.insert(END, row[j])
#                 else:
#                     e.config(width=10)
#                     e.insert(END, round(float(str(row[j])), 2))
#                 # e.insert(END, row[j])
#                 n = n + 1
#             i=i+1
#             vacio_label = Label(table_frame, text='', font=my_font, pady=10, padx=10)
#             vacio_label.grid(row=i, column=0)
#         except IndexError:
#             pass

def actualizar_lista():
    global thisid
    if flag1 != 0:
        thisid = 0
        for row in db.fetch():
            thisid = thisid + 1
        print('flag')
        print(flag_mostrar_detalles)
        if flag_mostrar_detalles == 0:
            small_populate_list()
        # else:
        #     populate_list()

def escoger_excavadora():
    mainwin.withdraw()
    selwin=Toplevel()
    # selwin.maxsize(500, 800)
    selwin.title('Datos')

    def calcular_datos():
        print('calcular datos')
        selwin.withdraw()

        def calcular_rend():
            global flag_ingresar_excavadora
            if alto_text.get() == '' or ancho_text.get() == '' or largo_text.get() == '':
                messagebox.showerror('Required Fields', 'Please include all fields')
                return
            else:
                try:
                    print('para cal rend')
                    print(thisid)
                    volumen = float(alto_text.get()) * float(ancho_text.get()) * float(largo_text.get())
                    sobreexcava = volumen*1.15
                    tiempodecarga = float(db.fetchtiempocarga(thisid))
                    numerocicloshora = 55.0/(tiempodecarga/60.0)
                    capacidadporhora = numerocicloshora*float(db.fetchcapacidadneta(thisid))
                    productividad = capacidadporhora
                    rendimiento = productividad*8.0
                    tiempoalquiler = sobreexcava/productividad
                    # alto, ancho, largo, volumen, sobreexcavacion, tiempoalquiler, numerocicloshora, productividad, rendimiento
                    db.insertarexcava(thisid, alto_text.get(), ancho_text.get(), largo_text.get(), volumen, sobreexcava, tiempoalquiler, numerocicloshora, productividad, rendimiento)
                    volumen_text.set(round(volumen, 2))
                    sobreexcava_text.set(round(sobreexcava, 2))
                    tiempoalquiler_text.set(round(tiempoalquiler, 2))
                    numerocicloshora_text.set(round(numerocicloshora, 2))
                    productividad_text.set(round(productividad, 2))
                    rendimiento_text.set(round(rendimiento, 2))
                    
                    flag_ingresar_excavadora = 0
                    global flag1
                    flag1 = 1
                except ValueError:
                    flag_ingresar_excavadora = 1
                    messagebox.showerror('Not a number', 'Please insert a number')

        def on_closingapp():
            selwin.deiconify()
            app.destroy()

        app = Toplevel()
        app.configure(bg='white')

        groupfinal = Frame(app)
        groupfinaltitle1 = Frame(groupfinal)
        groupfinalaal = Frame(groupfinal)
        groupfinaltitle2 = Frame(groupfinal)
        groupfinalnpr = Frame(groupfinal)
        groupfinaltitle3 = Frame(groupfinal)
        groupfinalvst = Frame(groupfinal)
        groupfinalbut = Frame(groupfinal)

        groupfinal.pack()
        groupfinaltitle1.pack()
        groupfinalaal.pack()
        groupfinaltitle2.pack()
        groupfinalnpr.pack()
        groupfinaltitle3.pack()
        groupfinalvst.pack()
        groupfinalbut.pack()

        ingexca_label = Label(groupfinaltitle1, text='Ingresar excavacion:', font=my_fontb, pady=10, padx=10)
        ingexca_label.config(bg='white')
        ingexca_label.pack()
        

        groupfinalaal1 = Frame(groupfinalaal, background='white')
        groupfinalaal1.pack()
        # Tiempo de ciclo
        alto_text = StringVar(groupfinalaal1,'','alto')
        alto_label = Label(groupfinalaal1, text='Alto', font=my_font, pady=10, padx=10)
        alto_label.config(bg='white')
        alto_entry = Entry(groupfinalaal1, textvariable=alto_text, width = 10, font=my_font)
        alto_label2 = Label(groupfinalaal1, text='m', font=my_font, pady=10, padx=10)
        alto_label2.config(bg='white')

        alto_label.pack(side='left', fill='x', anchor='w')
        alto_entry.pack(side='left', padx=5)
        alto_label2.pack(side='left', fill='x', anchor='e')

        groupfinalaal2 = Frame(groupfinalaal, background='white')
        groupfinalaal2.pack()
        ancho_text = StringVar(groupfinalaal2,'','ancho')
        ancho_label = Label(groupfinalaal2, text='Ancho', font=my_font, pady=10, padx=10)
        ancho_label.config(bg='white')
        ancho_entry = Entry(groupfinalaal2, textvariable=ancho_text, width = 10, font=my_font)
        ancho_label2 = Label(groupfinalaal2, text='m', font=my_font, pady=10, padx=10)
        ancho_label2.config(bg='white')

        ancho_label.pack(side='left', fill='x', anchor='w')
        ancho_entry.pack(side='left', padx=5)
        ancho_label2.pack(side='left', fill='x', anchor='e')

        groupfinalaal3 = Frame(groupfinalaal, background='white')
        groupfinalaal3.pack()
        largo_text = StringVar(groupfinalaal3,'','largo')
        largo_label = Label(groupfinalaal3, text='Largo', font=my_font, pady=10, padx=10)
        largo_label.config(bg='white')
        largo_entry = Entry(groupfinalaal3, textvariable=largo_text, width = 10, font=my_font)
        largo_label2 = Label(groupfinalaal3, text='m', font=my_font, pady=10, padx=10)
        largo_label2.config(bg='white')

        largo_label.pack(side='left', fill='x', anchor='w')
        largo_entry.pack(side='left', padx=5)
        largo_label2.pack(side='left', fill='x', anchor='e')

        resuldeexca_label = Label(groupfinaltitle2, text='Resultados de la excavadora:', font=my_fontb, pady=10, padx=10)
        resuldeexca_label.config(bg='white')
        resuldeexca_label.pack()

        groupfinalnpr1 = Frame(groupfinalnpr)
        groupfinalnpr1.pack()
        numerocicloshora_text = StringVar(groupfinalnpr1,'','numerocicloshora')
        numerocicloshora_label = Label(groupfinalnpr1, text='Numero de ciclos por hora', font=my_font, pady=10, padx=10)
        numerocicloshora_label.config(bg='white')
        numerocicloshora_output = Label(groupfinalnpr1, textvariable=numerocicloshora_text, relief=RAISED, font=my_font)
        numerocicloshora_output.config(bg='white')

        numerocicloshora_label.pack(side='left', fill='x', anchor='w')
        numerocicloshora_output.pack(side='left', padx=5)

        groupfinalnpr2 = Frame(groupfinalnpr)
        groupfinalnpr2.pack()
        # Productividad
        productividad_text = StringVar(groupfinalnpr2,'','prod')
        productividad_label = Label(groupfinalnpr2, text='Productividad', font=my_font, pady=10, padx=10)
        productividad_label.config(bg='white')
        productividad_output = Label(groupfinalnpr2, textvariable=productividad_text, relief=RAISED, font=my_font)
        productividad_output.config(bg='white')
        productividad_label2 = Label(groupfinalnpr2, text='m3/h', font=my_font, pady=10, padx=10)
        productividad_label2.config(bg='white')

        productividad_label.pack(side='left', fill='x', anchor='w')
        productividad_output.pack(side='left', padx=5)
        productividad_label2.pack(side='left', fill='x', anchor='e')

        groupfinalnpr3 = Frame(groupfinalnpr)
        groupfinalnpr3.pack()
        # Rendimiento
        rendimiento_text = StringVar(groupfinalnpr3,'','rend')
        rendimiento_label = Label(groupfinalnpr3, text='Rendimiento', font=my_font, pady=10, padx=10)
        rendimiento_label.config(bg='white')
        rendimiento_output = Label(groupfinalnpr3, textvariable=rendimiento_text, relief=RAISED, font=my_font)
        rendimiento_output.config(bg='white')
        rendimiento_label2 = Label(groupfinalnpr3, text='m3/d', font=my_font, pady=10, padx=10)
        rendimiento_label2.config(bg='white')

        rendimiento_label.pack(side='left', fill='x', anchor='w')
        rendimiento_output.pack(side='left', padx=5)
        rendimiento_label2.pack(side='left', fill='x', anchor='e')

        resuldeexcava_label = Label(groupfinaltitle3, text='Resultados de la excavacion:', font=my_fontb, pady=10, padx=10)
        resuldeexcava_label.config(bg='white')
        resuldeexca_label.pack()

        groupfinalvst1 = Frame(groupfinalvst)
        groupfinalvst1.pack()
        # Volumen
        volumen_text = StringVar(groupfinalvst1,'','volumen')
        volumen_label = Label(groupfinalvst1, text='Volumen', font=my_font, pady=10, padx=10)
        volumen_label.config(bg='white')
        volumen_output = Label(groupfinalvst1, textvariable=volumen_text, relief=RAISED, font=my_font)
        volumen_output.config(bg='white')
        volumen_label2 = Label(groupfinalvst1, text='m3', font=my_font, pady=10, padx=10)
        volumen_label2.config(bg='white')

        volumen_label.pack(side='left', fill='x', anchor='w')
        volumen_output.pack(side='left', padx=5)
        volumen_label2.pack(side='left', fill='x', anchor='e')

        groupfinalvst2 = Frame(groupfinalvst)
        groupfinalvst2.pack()
        sobreexcava_text = StringVar(groupfinalvst2,'','sobreexcava')
        sobreexcava_label = Label(groupfinalvst2, text='Sobreexcavacion', font=my_font, pady=10, padx=10)
        sobreexcava_label.config(bg='white')
        sobreexcava_output = Label(groupfinalvst2, textvariable=sobreexcava_text, relief=RAISED, font=my_font)
        sobreexcava_output.config(bg='white')
        sobreexcava_label2 = Label(groupfinalvst2, text='m3', font=my_font, pady=10, padx=10)
        sobreexcava_label2.config(bg='white')

        sobreexcava_label.pack(side='left', fill='x', anchor='w')
        sobreexcava_output.pack(side='left', padx=5)
        sobreexcava_label2.pack(side='left', fill='x', anchor='e')

        groupfinalvst3 = Frame(groupfinalvst)
        groupfinalvst3.pack()
        tiempoalquiler_text = StringVar(groupfinalvst3,'','tiempoalquiler')
        tiempoalquiler_label = Label(groupfinalvst3, text='Tiempo de alquiler', font=my_font, pady=10, padx=10)
        tiempoalquiler_label.config(bg='white')
        tiempoalquiler_output = Label(groupfinalvst3, textvariable=tiempoalquiler_text, relief=RAISED, font=my_font)
        tiempoalquiler_output.config(bg='white')
        tiempoalquiler_label2 = Label(groupfinalvst3, text='h', font=my_font, pady=10, padx=10)
        tiempoalquiler_label2.config(bg='white')

        tiempoalquiler_label.pack(side='left', fill='x', anchor='w')
        tiempoalquiler_output.pack(side='left', padx=5)
        tiempoalquiler_label2.pack(side='left', fill='x', anchor='e')

        # Buttons
        calcular_btn = Button(groupfinalbut, text='Calcular rendimiento', width=20, command=calcular_rend, font=my_fonts)
        calcular_btn.pack()

        app.title('Rendimiento')
        # app.maxsize(1000, 1000)

        app.protocol("WM_DELETE_WINDOW", on_closingapp)
        app.mainloop()
        
    def on_closingselwin():
        global flag_ingresar_excavadora
        if 'flag_ingresar_excavadora' in globals():
            if flag_ingresar_excavadora == 1:
                db.remove(thisid)
                flag_ingresar_excavadora = 0
        actualizar_lista()
        mainwin.deiconify()
        selwin.destroy()

    def comboclick1(event):
        if myCombo1.get() == "Hyundai Robex 200LC-9SB":
            imagemaq = Image.open('Hyundai_Robex_200LC-9SB.jpg')
            # imagemaqr = imagemaq.resize((150,150))

        elif myCombo1.get() == "Doosan DX225LCA":
            imagemaq = Image.open('Doosan_DX225LCA.jpg')
            
        imagemaqr = imagemaq.resize((150,150))

        photoimagemaq = ImageTk.PhotoImage(imagemaqr)
        # imagenexca = Label(groupcombotop, image=photoimagemaq)
        imagenexca.config(image=photoimagemaq)
        imagenexca.image = photoimagemaq
        # imagenexca.grid(row=2, column=0)
        # imagenexca.pack()

        if myCombo1.get() == "Hyundai Robex 200LC-9SB":
            cuchoptions = [
                "SAE APILADO N01",
                "SAE APILADO N02",
                "SAE APILADO N03",
                "SAE APILADO N04",
                "SAE APILADO N05",
                "SAE APILADO N06",
                "SAE APILADO N07",
                "SAE APILADO N08",
            ]
        elif myCombo1.get() == "Doosan DX225LCA":
            cuchoptions = [
                "Cucharon de uso general",
                "Cucharon de servicio pesado",
                "Cucharon de servicio severo"
            ]
        
        def comboclick2(event):
            if myCombo2.get() == "SAE APILADO N01":
                imagepal = Image.open('SAE_APILADO_N_01.jpg')
                imagepalr = imagepal.resize((150,150))
                capacidadcuchara = 0.51
                cuchara = "SAE APILADO N01"
            elif myCombo2.get() == "SAE APILADO N02":
                imagepal = Image.open('SAE_APILADO_N_02.jpg')
                imagepalr = imagepal.resize((150,150))
                capacidadcuchara = 0.80
                cuchara = "SAE APILADO N02"
            elif myCombo2.get() == "SAE APILADO N03":
                imagepal = Image.open('SAE_APILADO_N_03.jpg')
                imagepalr = imagepal.resize((150,150))
                capacidadcuchara = 1.10
                cuchara = "SAE APILADO N03"
            elif myCombo2.get() == "SAE APILADO N04":
                imagepal = Image.open('SAE_APILADO_N_04.jpg')
                imagepalr = imagepal.resize((150,150))
                capacidadcuchara = 1.34
                cuchara = "SAE APILADO N04"
            elif myCombo2.get() == "SAE APILADO N05":
                imagepal = Image.open('SAE_APILADO_N_05.jpg')
                imagepalr = imagepal.resize((150,150))
                capacidadcuchara = 0.74
                cuchara = "SAE APILADO N05"
            elif myCombo2.get() == "SAE APILADO N06":
                imagepal = Image.open('SAE_APILADO_N_06.jpg')
                imagepalr = imagepal.resize((150,150))
                capacidadcuchara = 0.87
                cuchara = "SAE APILADO N06"
            elif myCombo2.get() == "SAE APILADO N07":
                imagepal = Image.open('SAE_APILADO_N_07.jpg')
                imagepalr = imagepal.resize((150,150))
                capacidadcuchara = 0.75
                cuchara = "SAE APILADO N07"
            elif myCombo2.get() == "SAE APILADO N08":
                imagepal = Image.open('SAE_APILADO_N_08.jpg')
                imagepalr = imagepal.resize((150,150))
                capacidadcuchara = 0.52
                cuchara = "SAE APILADO N08"
            elif myCombo2.get() == "Cucharon de uso general":
                imagepal = Image.open('cucharon_de_uso_general.jpg')
                imagepalr = imagepal.resize((150,150))
                capacidadcuchara = 0.39
                cuchara = "Cucharon de uso general"
            elif myCombo2.get() == "Cucharon de servicio pesado":
                imagepal = Image.open('cucharon_de_servicio_pesado.jpg')
                imagepalr = imagepal.resize((150,150))
                capacidadcuchara = 0.60
                cuchara = "Cucharon de servicio pesado"
            elif myCombo2.get() == "Cucharon de servicio severo":
                imagepal = Image.open('cucharon_de_servicio_severo.jpg')
                imagepalr = imagepal.resize((150,150))
                capacidadcuchara = 0.91
                cuchara = "Cucharon de servicio severo"
            photoimagepal = ImageTk.PhotoImage(imagepalr)
            # imagenpala = Label(groupcombobot, image=photoimagepal)
            imagenpala.config(image=photoimagepal)
            imagenpala.image = photoimagepal
            # imagenpala.grid(row=5, column=0)
            # imagenpala.pack()
            global flag1
            flag1 = 0

            def ingresaexca():
                global flag_ingresar_excavadora
                global thisid
                if not myCombo1.get() or not myCombo2.get() or excavacion_text.get() == '' or balanceo_text.get() == '' or carga_text.get() == '':
                    messagebox.showerror('Required Fields', 'Please include all fields')
                    return
                else:
                    try:
                        flag_ingresar_excavadora = 1
                        db.insert('', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
                        thisid = thisid + 1
                        print('nuevo thisid')
                        print(thisid)
                        eficiencia = 0.75
                        tiempocarga = (float(excavacion_text.get()) + float(balanceo_text.get()) + float(carga_text.get()))/3.0
                        capacidadneta = capacidadcuchara*eficiencia
                        db.insertartiempocarga(thisid, myCombo1.get(), excavacion_text.get(), balanceo_text.get(), carga_text.get(), tiempocarga, cuchara, capacidadcuchara, eficiencia, capacidadneta)
                        escojer1_btn["state"] = "normal"
                        ingresarexca_btn["state"] = "disabled"
                    except ValueError:
                        flag_ingresar_excavadora = 0
                        db.remove(thisid)
                        thisid = thisid - 1
                        messagebox.showerror('Not a number', 'Please insert a number')
            # db.insert('', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
            ingresarexca_btn.configure(text='Ingresar excavadora', width=20, command=ingresaexca, font=my_fonts)
            # ingresarexca_btn.grid(row=10, column=0, pady=10)
            # ingresarexca_btn.pack()

        myCombo2.configure(value=cuchoptions, width=25, font=my_fonts)
        myCombo2.current()
        myCombo2.bind("<<ComboboxSelected>>", comboclick2)
        # myCombo2.grid(row=4, column=0, sticky=W, pady=10, padx=10)
        # myCombo2.pack()
        
    maqoptions = [
        "Hyundai Robex 200LC-9SB",
        "Doosan DX225LCA"
    ]

    global flag1
    flag1 = 1
    groupcombo = Frame(selwin, background='white')
    groupcombotop = Frame(groupcombo, background='white')
    groupcombobot = Frame(groupcombo, background='white')
    groupingresa = Frame(selwin, background='white')
    groupcombo.pack()
    groupcombotop.pack(side='top')
    groupcombobot.pack(side='bottom')
    groupingresa.pack()
    selex_label = Label(groupcombotop, text='Seleccionar Excavadora:', font=my_fontb, pady=10, padx=10)
    selex_label.pack()

    myCombo1 = ttk.Combobox(groupcombotop, value=maqoptions, width=25, font = my_fonts)
    myCombo1.current()
    myCombo1.bind("<<ComboboxSelected>>", comboclick1)
    myCombo1.pack()

    imagenexca = Label(groupcombotop)
    imagenexca.pack()

    selcu_label = Label(groupcombobot, text='Seleccionar cucharon:', font=my_fontb, pady=10, padx=10)
    selcu_label.pack()

    myCombo2 = ttk.Combobox(groupcombobot)
    myCombo2.pack()

    imagenpala = Label(groupcombobot)
    imagenpala.pack()

    ingresardat_label = Label(selwin, text='Ingresar tiempo de carga:', font=my_fontb, pady=10, padx=10)
    ingresardat_label.pack()

    group1 = Frame(groupingresa, background='white')
    group1.pack(side='top', pady=5)
    excavacion_text = StringVar(group1,'','excavacion')
    excavacion_label = Label(group1, text='Excavacion', font=my_font, pady=10, padx=3)
    excavacion_entry = Entry(group1, textvariable=excavacion_text, width=10, font=my_font)
    excavacion_label2 = Label(group1, text='segundos', font=my_font, pady=10, padx=3)
    excavacion_label.pack(side='left', fill='x', anchor='w')
    excavacion_entry.pack(side='left', padx=5)
    excavacion_label2.pack(side='left', fill='x', anchor='e')

    group2 = Frame(groupingresa, background='white')
    group2.pack(side='top', pady=5)
    espacio2_label = Label(group2, text='', width=2, bg='white')
    espacio2_label.pack(side='left')
    balanceo_text = StringVar(group2,'','balanceo')
    balanceo_label = Label(group2, text='Balanceo', font=my_font, pady=10, padx=3)
    balanceo_entry = Entry(group2, textvariable=balanceo_text, width=10, font=my_font)
    balanceo_label2 = Label(group2, text='segundos', font=my_font, pady=10, padx=3)
    balanceo_label.pack(side='left', fill='x', anchor='w')
    balanceo_entry.pack(side='left', padx=5)
    balanceo_label2.pack(side='left', fill='x', anchor='e')

    group3 = Frame(groupingresa, background='white')
    group3.pack(side='top', pady=5)
    espacio3_label = Label(group3, text='', width=6, bg='white')
    espacio3_label.pack(side='left')
    carga_text = StringVar(group3,'','carga')
    carga_label = Label(group3, text='Carga', font=my_font, pady=10, padx=3)
    carga_entry = Entry(group3, textvariable=carga_text, width=10, font=my_font)
    carga_label2 = Label(group3, text='segundos', font=my_font, pady=10, padx=3)
    carga_label.pack(side='left', fill='x', anchor='w')
    carga_entry.pack(side='left', padx=5)
    carga_label2.pack(side='left', fill='x', anchor='e')

    # ingresar excavadora
    ingresarexca_btn = Button(groupingresa)
    ingresarexca_btn.pack()

    escojer1_btn = Button(selwin, text='Ingresar excavacion', width=20, command=calcular_datos, font=my_fonts)
    escojer1_btn["state"] = "disabled"
    escojer1_btn.pack(side='top', anchor='center')

    selwin.protocol("WM_DELETE_WINDOW", on_closingselwin)
    selex_label.config(bg='white')
    selcu_label.config(bg='white')
    ingresardat_label.config(bg='white')
    excavacion_label.config(bg='white')
    excavacion_label2.config(bg='white')
    balanceo_label.config(bg='white')
    balanceo_label2.config(bg='white')
    carga_label.config(bg='white')
    carga_label2.config(bg='white')
    selwin.configure(bg='white')
    selwin.mainloop()

def eliminar_id():
    iniciar_btn["state"] = "disabled"
    detalles_btn["state"] = "disabled"
    global thisid
    global flag_mostrar_detalles
    db.remove(thisid)
    thisid = 0
    for row in db.fetch():
        thisid = thisid + 1
    print('flag')
    print(flag_mostrar_detalles)
    if flag_mostrar_detalles == 0:
        new_small_populate_list()
    else:
        new_populate_list()

# def mostrar_detalles():
#     global flag_mostrar_detalles
#     if flag_mostrar_detalles == 0:
#         tree.pack_forget()
#         # populate_list()
#         tree2.pack()
#         flag_mostrar_detalles = 1
#     else:
#         tree2.pack_forget()
#         # small_populate_list()
#         tree.pack()
#         flag_mostrar_detalles = 0
#     print('flag')
#     print(flag_mostrar_detalles)

iniciar_btn = Button(table_frame_buttons, text='Iniciar', width=6, command=escoger_excavadora, font=my_fonts)

# detalles_btn = Button(table_frame_buttons, text='Detalles', width=7, command=mostrar_detalles, font=my_fonts)

eliminar_btn = Button(table_frame_buttons, text='Eliminar', width=7, command=eliminar_id, font=my_fonts)

iniciar_btn.pack(anchor='n', side='left', padx=5, pady=5)
eliminar_btn.pack(anchor='n', side='right', padx=5, pady=5)
# detalles_btn.pack(anchor='n', side='right', padx=5, pady=5)

small_populate_list()
# populate_list()

mainwin.mainloop()