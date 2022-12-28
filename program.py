from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from db import Database
from tkinter import messagebox
import tkinter.font

db = Database('maq.db')

mainwin=Tk()
mainwin.maxsize= (1500, 300)

my_font = tkinter.font.Font(mainwin,family="Arial Black", size=12)
my_fonts = tkinter.font.Font(mainwin,family="Arial Black", size=10)
my_fontb = tkinter.font.Font(mainwin,family="Arial Black", size=12, underline=True)
my_fontdisplay = tkinter.font.Font(mainwin,family="Arial Black", size=8)

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
table_frame = Frame(mainwin, width = 1000, height = 200, padx = 3)
table_frame.grid(row=1, sticky="ns")
table_frame.grid_remove()
small_table_frame = Frame(mainwin, width = 1000, height = 200, padx = 3)
small_table_frame.grid(row=1, sticky="ns")
small_table_frame.grid_remove()
table_frame_buttons = Frame(mainwin, width = 1000, height = 200, padx = 3)

def small_populate_list():
    # small_table_frame = Frame(mainwin, width = 1000, height = 200, padx = 3)
    # small_table_frame.grid(row=1, sticky="ns")
    small_table_frame.grid()
    marco1_label = Label(small_table_frame, text='Excavadora', font=my_fontdisplay)
    marco1_label.grid(row=1, column=1, sticky=W)
    marco2_label = Label(small_table_frame, text='Cuchara', font=my_fontdisplay)
    marco2_label.grid(row=1, column=2, sticky=W)
    marco3_label = Label(small_table_frame, text='Productividad', font=my_fontdisplay)
    marco3_label.grid(row=1, column=3, sticky=W)
    marco4_label = Label(small_table_frame, text='Rendimiento', font=my_fontdisplay)
    marco4_label.grid(row=1, column=4, sticky=W)
    i = 2
    for row in db.smallfetch():
        try:
            n = 0
            print('populate list')
            print(thisid)
            for j in range(len(row)):
                e = Text(small_table_frame, width=16, height=2, fg='black', font=my_fontdisplay, wrap=None)
                e.grid(row=i, column=j)
                # if n == 0:
                #     e.config(width=4)
                #     e.insert(END, row[j])
                # elif n == 1 or n == 2:
                #     e.config(width=13)
                #     e.insert(END, row[j])
                # else:
                #     e.config(width=10)
                #     e.insert(END, round(float(str(row[j])), 2))

                e.insert(END, row[j])
                n = n + 1
            i=i+1
        except IndexError:
            pass

def populate_list():
    # table_frame = Frame(mainwin, width = 1000, height = 200, padx = 3)
    # table_frame.grid(row=1, sticky="ns")
    # excavadora, excavacion, balanceo, carga, tiempocarga, cuchara, eficiencia, capacidadcuchara, capacidadneta, alto, ancho, largo, volumen, sobreexcavacion, tiempoalquiler, numerocicloshora, productividad, rendimiento
    table_frame.grid()
    marco1_label = Label(table_frame, text='Excavadora', font=my_fontdisplay)
    marco1_label.grid(row=1, column=1, sticky=W)
    marco2_label = Label(table_frame, text='Excavacion', font=my_fontdisplay)
    marco2_label.grid(row=1, column=2, sticky=W)
    marco3_label = Label(table_frame, text='Balanceo', font=my_fontdisplay)
    marco3_label.grid(row=1, column=3, sticky=W)
    marco4_label = Label(table_frame, text='Carga', font=my_fontdisplay)
    marco4_label.grid(row=1, column=4, sticky=W)
    marco5_label = Label(table_frame, text='Tiempo de carga', font=my_fontdisplay)
    marco5_label.grid(row=1, column=5, sticky=W)
    marco6_label = Label(table_frame, text='Cuchara', font=my_fontdisplay)
    marco6_label.grid(row=1, column=6, sticky=W)
    marco7_label = Label(table_frame, text='Eficiencia', font=my_fontdisplay)
    marco7_label.grid(row=1, column=7, sticky=W)
    marco8_label = Label(table_frame, text='Capacidad de cuchara', font=my_fontdisplay, wraplength=100)
    marco8_label.grid(row=1, column=8, sticky=W)
    marco9_label = Label(table_frame, text='Capacidad neta', font=my_fontdisplay)
    marco9_label.grid(row=1, column=9, sticky=W)
    marco10_label = Label(table_frame, text='Alto', font=my_fontdisplay)
    marco10_label.grid(row=1, column=10, sticky=W)
    marco11_label = Label(table_frame, text='Ancho', font=my_fontdisplay)
    marco11_label.grid(row=1, column=11, sticky=W)
    marco12_label = Label(table_frame, text='Largo', font=my_fontdisplay)
    marco12_label.grid(row=1, column=12, sticky=W)
    marco13_label = Label(table_frame, text='Volumen', font=my_fontdisplay)
    marco13_label.grid(row=1, column=13, sticky=W)
    marco14_label = Label(table_frame, text='Sobreexcavacion', font=my_fontdisplay)
    marco14_label.grid(row=1, column=14, sticky=W)
    marco15_label = Label(table_frame, text='Tiempo de alquiler', font=my_fontdisplay)
    marco15_label.grid(row=1, column=15, sticky=W)
    marco16_label = Label(table_frame, text='Numero de ciclos por hora', font=my_fontdisplay)
    marco16_label.grid(row=1, column=16, sticky=W)
    marco17_label = Label(table_frame, text='Productividad', font=my_fontdisplay)
    marco17_label.grid(row=1, column=17, sticky=W)
    marco18_label = Label(table_frame, text='Rendimiento', font=my_fontdisplay)
    marco18_label.grid(row=1, column=18, sticky=W)
    i = 2
    for row in db.fetch():
        try:
            n = 0
            print('populate list')
            print(thisid)
            for j in range(len(row)):
                e = Text(table_frame, width=16, height=2, fg='black', font=my_fontdisplay, wrap=None)
                e.grid(row=i, column=j)
                # if n == 0 or n == 1 or n == 6:
                if n == 0:
                    e.config(width=4)
                    e.insert(END, row[j])
                elif n == 1 or n == 6:
                    e.config(width=13)
                    e.insert(END, row[j])
                else:
                    e.config(width=10)
                    e.insert(END, round(float(str(row[j])), 2))
                # e.insert(END, row[j])
                n = n + 1
            i=i+1
            vacio_label = Label(table_frame, text='', font=my_font, pady=10, padx=10)
            vacio_label.grid(row=i, column=0)
        except IndexError:
            pass

# esto corresponde a treeview una nueva forma de mostrar los datos
# def new_populate_list():
#     tree=ttk.Treeview(mainwin)
#     tree['show'] = 'headings'

def actualizar_lista():
    global thisid
    if flag1 != 0:
        thisid = 0
        for row in db.fetch():
            thisid = thisid + 1
        if flag_mostrar_detalles==0:
            small_populate_list()
        else:
            populate_list()

def escoger_excavadora():
    mainwin.withdraw()
    selwin=Toplevel()
    selwin.maxsize(330, 800)

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


        ingexca_label = Label(app, text='Ingresar excavacion:', font=my_fontb, pady=10, padx=10)
        ingexca_label.grid(row=0, column=0, sticky=W)
        

        # Tiempo de ciclo
        alto_text = StringVar(app,'','alto')
        alto_label = Label(app, text='Alto', font=my_font, pady=10, padx=10)
        alto_label.grid(row=1, column=0, sticky=W)
        alto_entry = Entry(app, textvariable=alto_text, width = 10, font=my_font)
        alto_entry.grid(row=1, column=1)
        alto_label2 = Label(app, text='m', font=my_font, pady=10, padx=10)
        alto_label2.grid(row=1, column=2, sticky=W)

        ancho_text = StringVar(app,'','ancho')
        ancho_label = Label(app, text='Ancho', font=my_font, pady=10, padx=10)
        ancho_label.grid(row=2, column=0, sticky=W)
        ancho_entry = Entry(app, textvariable=ancho_text, width = 10, font=my_font)
        ancho_entry.grid(row=2, column=1)
        ancho_label2 = Label(app, text='m', font=my_font, pady=10, padx=10)
        ancho_label2.grid(row=2, column=2, sticky=W)

        largo_text = StringVar(app,'','largo')
        largo_label = Label(app, text='Largo', font=my_font, pady=10, padx=10)
        largo_label.grid(row=3, column=0, sticky=W)
        largo_entry = Entry(app, textvariable=largo_text, width = 10, font=my_font)
        largo_entry.grid(row=3, column=1)
        largo_label2 = Label(app, text='m', font=my_font, pady=10, padx=10)
        largo_label2.grid(row=3, column=2, sticky=W)

        resuldeexca_label = Label(app, text='Resultados de la excavadora:', font=my_fontb, pady=10, padx=10)
        resuldeexca_label.grid(row=4, column=0, sticky=W)

        numerocicloshora_text = StringVar(app,'','numerocicloshora')
        numerocicloshora_label = Label(app, text='Numero de ciclos por hora', font=my_font, pady=10, padx=10)
        numerocicloshora_label.grid(row=5, column=0, sticky=W)
        numerocicloshora_output = Label(app, textvariable=numerocicloshora_text, relief=RAISED, font=my_font)
        numerocicloshora_output.grid(row=5, column=1)

        # Productividad
        productividad_text = StringVar(app,'','prod')
        productividad_label = Label(app, text='Productividad', font=my_font, pady=10, padx=10)
        productividad_label.grid(row=6, column=0, sticky=W)
        productividad_output = Label(app, textvariable=productividad_text, relief=RAISED, font=my_font)
        productividad_output.grid(row=6, column=1)
        productividad_label2 = Label(app, text='m3/h', font=my_font, pady=10, padx=10)
        productividad_label2.grid(row=6, column=2, sticky=W)

        # Rendimiento
        rendimiento_text = StringVar(app,'','rend')
        rendimiento_label = Label(app, text='Rendimiento', font=my_font, pady=10, padx=10)
        rendimiento_label.grid(row=7, column=0, sticky=W)
        rendimiento_output = Label(app, textvariable=rendimiento_text, relief=RAISED, font=my_font)
        rendimiento_output.grid(row=7, column=1)
        rendimiento_label2 = Label(app, text='m3/d', font=my_font, pady=10, padx=10)
        rendimiento_label2.grid(row=7, column=2, sticky=W)

        resuldeexcava_label = Label(app, text='Resultados de la excavacion:', font=my_fontb, pady=10, padx=10)
        resuldeexcava_label.grid(row=8, column=0, sticky=W)

        # Volumen
        volumen_text = StringVar(app,'','volumen')
        volumen_label = Label(app, text='Volumen', font=my_font, pady=10, padx=10)
        volumen_label.grid(row=9, column=0, sticky=W)
        volumen_output = Label(app, textvariable=volumen_text, relief=RAISED, font=my_font)
        volumen_output.grid(row=9, column=1)
        volumen_label2 = Label(app, text='m3', font=my_font, pady=10, padx=10)
        volumen_label2.grid(row=9, column=2, sticky=W)

        sobreexcava_text = StringVar(app,'','sobreexcava')
        sobreexcava_label = Label(app, text='Sobreexcavacion', font=my_font, pady=10, padx=10)
        sobreexcava_label.grid(row=10, column=0, sticky=W)
        sobreexcava_output = Label(app, textvariable=sobreexcava_text, relief=RAISED, font=my_font)
        sobreexcava_output.grid(row=10, column=1)
        sobreexcava_label2 = Label(app, text='m3', font=my_font, pady=10, padx=10)
        sobreexcava_label2.grid(row=10, column=2, sticky=W)

        tiempoalquiler_text = StringVar(app,'','tiempoalquiler')
        tiempoalquiler_label = Label(app, text='Tiempo de alquiler', font=my_font, pady=10, padx=10)
        tiempoalquiler_label.grid(row=11, column=0, sticky=W)
        tiempoalquiler_output = Label(app, textvariable=tiempoalquiler_text, relief=RAISED, font=my_font)
        tiempoalquiler_output.grid(row=11, column=1)
        tiempoalquiler_label2 = Label(app, text='h', font=my_font, pady=10, padx=10)
        tiempoalquiler_label2.grid(row=11, column=2, sticky=W)

        # Buttons
        calcular_btn = Button(app, text='Calcular rendimiento', width=20, command=calcular_rend, font=my_fonts)
        calcular_btn.grid(row=12, column=0, pady=10, padx=20)

        app.title('Rendimiento')
        app.maxsize(1000, 1000)

        app.protocol("WM_DELETE_WINDOW", on_closingapp)
        app.mainloop()
        
    def on_closingselwin():
        print('para el flag')
        print(thisid)
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
            imagemaqr = imagemaq.resize((150,150))

        elif myCombo1.get() == "Doosan DX225LCA":
            imagemaq = Image.open('Doosan_DX225LCA.jpg')
            imagemaqr = imagemaq.resize((150,150))

        photoimagemaq = ImageTk.PhotoImage(imagemaqr)
        imagenexca = Label(selwin, image=photoimagemaq)
        imagenexca.image = photoimagemaq
        imagenexca.grid(row=2, column=0)

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
            imagenpala = Label(selwin, image=photoimagepal)
            imagenpala.image = photoimagepal
            imagenpala.grid(row=5, column=0)
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
            ingresarexca_btn = Button(selwin, text='Ingresar excavadora', width=20, command=ingresaexca, font=my_fonts)
            ingresarexca_btn.grid(row=10, column=0, pady=10)

        myCombo2 = ttk.Combobox(selwin, value=cuchoptions, width=25, font=my_fonts)
        myCombo2.current()
        myCombo2.bind("<<ComboboxSelected>>", comboclick2)
        myCombo2.grid(row=4, column=0, sticky=W, pady=10, padx=10)
        
    maqoptions = [
        "Hyundai Robex 200LC-9SB",
        "Doosan DX225LCA"
    ]

    global flag1
    flag1 = 1
    selex_label = Label(selwin, text='Seleccionar Excavadora:', font=my_fontb, pady=10, padx=10)
    selex_label.grid(row=0, column=0, sticky=W)

    myCombo1 = ttk.Combobox(selwin, value=maqoptions, width=25, font = my_fonts)
    myCombo1.current()
    myCombo1.bind("<<ComboboxSelected>>", comboclick1)
    myCombo1.grid(row=1, column=0, sticky=W, pady=10, padx=10)

    selcu_label = Label(selwin, text='Seleccionar cucharon:', font=my_fontb, pady=10, padx=10)
    selcu_label.grid(row=3, column=0, sticky=W)

    ingresardat_label = Label(selwin, text='Ingresar tiempo de carga:', font=my_fontb, pady=10, padx=10)
    ingresardat_label.grid(row=6, column=0, sticky=W)

    excavacion_text = StringVar(selwin,'','excavacion')
    excavacion_label = Label(selwin, text='Excavacion', font=my_font, pady=10, padx=3)
    excavacion_label.grid(row=7, column=0, sticky=W)
    excavacion_entry = Entry(selwin, textvariable=excavacion_text, width=10, font=my_font)
    excavacion_entry.grid(row=7, column=1)
    excavacion_label2 = Label(selwin, text='segundos', font=my_font, pady=10, padx=3)
    excavacion_label2.grid(row=7, column=2, sticky=W)

    balanceo_text = StringVar(selwin,'','balanceo')
    balanceo_label = Label(selwin, text='Balanceo', font=my_font, pady=10, padx=3)
    balanceo_label.grid(row=8, column=0, sticky=W)
    balanceo_entry = Entry(selwin, textvariable=balanceo_text, width=10, font=my_font)
    balanceo_entry.grid(row=8, column=1)
    balanceo_label2 = Label(selwin, text='segundos', font=my_font, pady=10, padx=3)
    balanceo_label2.grid(row=8, column=2, sticky=W)

    carga_text = StringVar(selwin,'','carga')
    carga_label = Label(selwin, text='Carga', font=my_font, pady=10, padx=3)
    carga_label.grid(row=9, column=0, sticky=W)
    carga_entry = Entry(selwin, textvariable=carga_text, width=10, font=my_font)
    carga_entry.grid(row=9, column=1)
    carga_label2 = Label(selwin, text='segundos', font=my_font, pady=10, padx=3)
    carga_label2.grid(row=9, column=2, sticky=W)

    escojer1_btn = Button(selwin, text='Ingresar excavacion', width=20, command=calcular_datos, font=my_fonts)
    escojer1_btn["state"] = "disabled"
    escojer1_btn.grid(row=11, column=0, pady=10)

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

def crear_nuevo_table():
    small_table_frame = Frame(mainwin, width = 1000, height = 200, padx = 3)
    small_table_frame.grid(row=1, sticky="ns")
    small_table_frame.grid_remove()

def eliminar_id():
    db.remove(thisid)
    crear_nuevo_table()
    actualizar_lista()
    # global flag_eliminar
    # flag_eliminar=1
    # global thisid
    # db.remove(thisid)
    # actualizar_lista()
    

def mostrar_detalles():
    global flag_mostrar_detalles
    if flag_mostrar_detalles == 0:
        small_table_frame.grid_remove()
        populate_list()
        flag_mostrar_detalles = 1
    else:
        table_frame.grid_remove()
        small_populate_list()
        flag_mostrar_detalles = 0

def borrar():
    small_table_frame.grid_remove()

table_frame_buttons.grid(row=0, sticky="ns")
iniciar_btn = Button(table_frame_buttons, text='Iniciar', width=6, command=escoger_excavadora, font=my_fonts)
iniciar_btn.grid(row=0, column=0, pady=10, padx=10)
detalles_btn = Button(table_frame_buttons, text='Detalles', width=7, command=mostrar_detalles, font=my_fonts)
detalles_btn.grid(row=0, column=1, pady=10, padx=10)

eliminar_btn = Button(table_frame_buttons, text='Eliminar', width=7, command=eliminar_id, font=my_fonts)
eliminar_btn.grid(row=0, column=2, pady=10, padx=10)
eliminar_btn = Button(table_frame_buttons, text='borrar', width=7, command=borrar, font=my_fonts)
eliminar_btn.grid(row=0, column=3, pady=10, padx=10)
# eliminar_text = StringVar(mainwin,'','eliminar')
# eliminar_entry = Entry(mainwin, textvariable=eliminar_text, width=4, font=my_font)
# eliminar_entry.grid(row=0, column=3)

small_populate_list()

mainwin.mainloop()