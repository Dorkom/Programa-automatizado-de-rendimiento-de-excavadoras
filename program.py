from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from db import Database
from tkinter import messagebox
import tkinter.font

db = Database('maq.db')

mainwin=Tk()
# mainwin.geometry('1500x300')
mainwin.maxsize= (1500, 300)
# mainwin.maxsize= (50000, 500)

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
print(thisid)

frame_main = tkinter.Frame(mainwin)
frame_main.grid(sticky='news')

def small_populate_list():
    frame_canvas = tkinter.Frame(frame_main)
    marco1_label = Label(mainwin, text='Excavadora', font=my_fontdisplay)
    marco1_label.grid(row=1, column=1, sticky=W)
    marco1_label = Label(mainwin, text='Cuchara', font=my_fontdisplay)
    marco1_label.grid(row=1, column=2, sticky=W)
    marco1_label = Label(mainwin, text='Productividad', font=my_fontdisplay)
    marco1_label.grid(row=1, column=3, sticky=W)
    marco1_label = Label(mainwin, text='Rendimiento', font=my_fontdisplay)
    marco1_label.grid(row=1, column=4, sticky=W)
    i = 2
    # vari = 0
    for row in db.smallfetch():
        # parts_list.insert(END, row)
        try:
            n = 0
            # vari = vari+1
            print('populate list')
            print(thisid)
            # print('vari')
            # print(vari)
            # if vari == thisid:
            #     break
            for j in range(len(row)):
                e = Text(mainwin, width=16, height=2, fg='black', font=my_fontdisplay, wrap=None)
                e.grid(row=i, column=j)
                # e.insert(END, row[j])
                if n == 0:
                    e.config(width=4)
                    e.insert(END, row[j])
                elif n == 1 or n == 2:
                    e.config(width=13)
                    e.insert(END, row[j])
                else:
                    e.config(width=10)
                    e.insert(END, round(float(str(row[j])), 2))

                # e.insert(END, row[j])
                n = n + 1
            i=i+1
            # vacio_label = Label(mainwin, text='', pady=10)
            # vacio_label.grid(row=i, column=0)
            
            # vsb = Scrollbar(mainwin, orient='vertical', command=mainwin.yview)
            # vsb.grid(row=i, column=j+2)
        except IndexError:
            pass

def populate_list():
    # parts_list.delete(0, END)
    # excavadora, excavacion, balanceo, carga, tiempocarga, cuchara, eficiencia, capacidadcuchara, capacidadneta, alto, ancho, largo, volumen, sobreexcavacion, tiempoalquiler, numerocicloshora, productividad, rendimiento
    marco1_label = Label(mainwin, text='Excavadora', font=my_fontdisplay)
    marco1_label.grid(row=1, column=1, sticky=W)
    marco1_label = Label(mainwin, text='Excavacion', font=my_fontdisplay)
    marco1_label.grid(row=1, column=2, sticky=W)
    marco1_label = Label(mainwin, text='Balanceo', font=my_fontdisplay)
    marco1_label.grid(row=1, column=3, sticky=W)
    marco1_label = Label(mainwin, text='Carga', font=my_fontdisplay)
    marco1_label.grid(row=1, column=4, sticky=W)
    marco1_label = Label(mainwin, text='Tiempo de carga', font=my_fontdisplay)
    marco1_label.grid(row=1, column=5, sticky=W)
    marco1_label = Label(mainwin, text='Cuchara', font=my_fontdisplay)
    marco1_label.grid(row=1, column=6, sticky=W)
    marco1_label = Label(mainwin, text='Eficiencia', font=my_fontdisplay)
    marco1_label.grid(row=1, column=7, sticky=W)
    marco1_label = Label(mainwin, text='Capacidad de cuchara', font=my_fontdisplay, wraplength=100)
    marco1_label.grid(row=1, column=8, sticky=W)
    marco1_label = Label(mainwin, text='Capacidad neta', font=my_fontdisplay)
    marco1_label.grid(row=1, column=9, sticky=W)
    marco1_label = Label(mainwin, text='Alto', font=my_fontdisplay)
    marco1_label.grid(row=1, column=10, sticky=W)
    marco1_label = Label(mainwin, text='Ancho', font=my_fontdisplay)
    marco1_label.grid(row=1, column=11, sticky=W)
    marco1_label = Label(mainwin, text='Largo', font=my_fontdisplay)
    marco1_label.grid(row=1, column=12, sticky=W)
    marco1_label = Label(mainwin, text='Volumen', font=my_fontdisplay)
    marco1_label.grid(row=1, column=13, sticky=W)
    marco1_label = Label(mainwin, text='Sobreexcavacion', font=my_fontdisplay)
    marco1_label.grid(row=1, column=14, sticky=W)
    marco1_label = Label(mainwin, text='Tiempo de alquiler', font=my_fontdisplay)
    marco1_label.grid(row=1, column=15, sticky=W)
    marco1_label = Label(mainwin, text='Numero de ciclos por hora', font=my_fontdisplay)
    marco1_label.grid(row=1, column=16, sticky=W)
    marco1_label = Label(mainwin, text='Productividad', font=my_fontdisplay)
    marco1_label.grid(row=1, column=17, sticky=W)
    marco1_label = Label(mainwin, text='Rendimiento', font=my_fontdisplay)
    marco1_label.grid(row=1, column=18, sticky=W)
    i = 2
    # vari = 0
    for row in db.fetch():
        # parts_list.insert(END, row)
        try:
            n = 0
            # vari = vari+1
            print('populate list')
            print(thisid)
            # print('vari')
            # print(vari)
            # if vari == thisid:
            #     break
            for j in range(len(row)):
                e = Text(mainwin, width=16, height=2, fg='black', font=my_fontdisplay, wrap=None)
                e.grid(row=i, column=j)
                # e.insert(END, row[j])
                if n == 0 or n == 1 or n == 6:
                    e.insert(END, row[j])
                else:
                    e.insert(END, round(float(str(row[j])), 2))
                    # e.insert(END, row[j])
                n = n + 1
            i=i+1
            vacio_label = Label(mainwin, text='', font=my_font, pady=10, padx=10)
            vacio_label.grid(row=i, column=0)
            
            # vsb = Scrollbar(mainwin, orient='vertical', command=mainwin.yview)
            # vsb.grid(row=i, column=j+2)
        except IndexError:
            pass


def escoger_excavadora():
    mainwin.withdraw()
    selwin=Toplevel()
    # selwin.geometry('330x800')
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
                    # capacidadhora_text.set(round(capacidadporhora, 2))
                    productividad_text.set(round(productividad, 2))
                    rendimiento_text.set(round(rendimiento, 2))
                    
                    flag_ingresar_excavadora = 0
                    global flag1
                    flag1 = 1

                    # if tiempo1_text.get() != '' or tiempo2_text.get() != '' or tiempo3_text.get() != '':
                    #     calt = float(tiempo1_text.get()) + float(tiempo2_text.get()) + float(tiempo3_text.get())
                    #     prod = float(calt)*float(volumen_text.get())
                    #     rend = prod*8.0
                    #     productividad_text.set(prod)
                    #     rendimiento_text.set(rend)
                    # print('productividad')
                    # print(prod)
                    # print('rendimiento')
                    # print(rend)
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

        # capacidadhora_text = StringVar(app,'','capacidadhora')
        # capacidadhora_label = Label(app, text='Capacidad por hora', font=my_font, pady=10, padx=10)
        # capacidadhora_label.grid(row=8, column=0, sticky=W)
        # capacidadhora_output = Label(app, textvariable=capacidadhora_text, relief=RAISED, font=my_font)
        # capacidadhora_output.grid(row=8, column=1)

        # Buttons
        calcular_btn = Button(app, text='Calcular rendimiento', width=20, command=calcular_rend, font=my_fonts)
        calcular_btn.grid(row=12, column=0, pady=10, padx=20)

        app.title('Rendimiento')
        app.maxsize(1000, 1000)
        # app.geometry('400x600')

        app.protocol("WM_DELETE_WINDOW", on_closingapp)
        app.mainloop()
        
    def on_closingselwin():
        print('para el flag')
        print(thisid)
        global flag_ingresar_excavadora
        if 'flag_ingresar_excavadora' in globals():
            if flag_ingresar_excavadora == 1:
                db.remove(thisid)
                # db.remove(thisid+1)
                flag_ingresar_excavadora = 0
        actualizar_lista()
        mainwin.deiconify()
        selwin.destroy()

    def comboclick1(event):
        # imagenexca = Label(selwin, text=myCombo1.get(), font=my_font, pady=10, padx=10)
        # imagehy = PhotoImage(file='Hyundai_Robex_200LC-9SB.jpg')
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
                # global flag1
                # flag1 = 0
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

    # myCombo2 = ttk.Combobox(selwin, value=cuchoptions, width=25)
    # myCombo2.current()
    # myCombo2.bind("<<ComboboxSelected>>", comboclick2)
    # myCombo2.grid(row=4, column=0, sticky=W, pady=10, padx=10)

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



iniciar_btn = Button(mainwin, text='Iniciar', width=10, command=escoger_excavadora, font=my_fonts)
iniciar_btn.grid(row=0, column=0, pady=10, padx=10)
detalles_btn = Button(mainwin, text='Detalles', width=10, command=populate_list, font=my_fonts)
detalles_btn.grid(row=0, column=1, pady=10, padx=10)

def actualizar_lista():
    global thisid
    if flag1 != 0:
        thisid = 0
        for row in db.fetch():
            thisid = thisid + 1
        small_populate_list()

# actualizar_btn = Button(mainwin, text='Actualizar lista', width=20, command=actualizar_lista)
# actualizar_btn.grid(row=0, column=1, pady=10, padx=10)

# parts_list = Listbox(mainwin, height=10, width=180, border=1)
# parts_list.grid(row=1, column=0, columnspan=19, rowspan=6, pady=20, padx=20)

# scrollbar = Scrollbar(mainwin)
# scrollbar.grid(row=1, column=3)

# parts_list.configure(yscrollcommand=scrollbar.set)
# scrollbar.configure(command=parts_list.yview)

small_populate_list()

mainwin.mainloop()

# r_set=my_conn.execute('''SELECT * from student LIMIT 0,10''');
# i=0 # row value inside the loop 
# for student in r_set: 
#     for j in range(len(student)):
#         e = Entry(my_w, width=10, fg='blue') 
#         e.grid(row=i, column=j) 
#         e.insert(END, student[j])
#     i=i+1
# my_w.mainloop()

# pyinstaller program.py --onefile --windowed --add-data "Hyundai_Robex_200LC-9SB.jpg;." --add-data "Doosan_DX225LCA.jpg;." --add-data "SAE_APILADO_N_01.jpg;." --add-data "SAE_APILADO_N_02.jpg;." --add-data "SAE_APILADO_N_03.jpg;." --add-data "SAE_APILADO_N_04.jpg;." --add-data "SAE_APILADO_N_05.jpg;." --add-data "SAE_APILADO_N_06.jpg;." --add-data "SAE_APILADO_N_07.jpg;." --add-data "SAE_APILADO_N_08.jpg;." --add-data "cucharon_de_uso_general.jpg;." --add-data "cucharon_de_servicio_pesado.jpg;." --add-data "cucharon_de_servicio_severo.jpg;." --add-data "maq.db;."