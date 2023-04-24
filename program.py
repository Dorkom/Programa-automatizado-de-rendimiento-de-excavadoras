from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from db import Database
from tkinter import messagebox
import tkinter.font
# forma1: detectada por antivirus
# import os
# forma2:
# import webbrowser
# forma3:
# from PyQt5.QtGui import QDesktopServices
# from PyQt5.QtCore import QUrl
# forma4:
import subprocess

db = Database('maq.db')
rows = db.fetch()
# rowssmall = db.smallfetch

mainwin=Tk()
mainwin.maxsize= (1000, 1000)
mainwin.title('RENDEXCA')
mainwin.configure(bg='white')
mainwin.resizable(False, False)

# configurando icono
icono = PhotoImage(file='excavator.png')
mainwin.iconphoto(False, icono)


my_font = tkinter.font.Font(family="Arial", size=12)
my_fonts = tkinter.font.Font(family="Arial", size=10)
my_fontb = tkinter.font.Font(family="Arial", size=12)
my_fontdisplay = tkinter.font.Font(family="Arial", size=8)

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
global rendimiento
print(thisid)

# variable de factor
global varfac
varfac = 0

# variable para editar una fila
global ideditar
ideditar = 0

# creacion de frames
table_frame_buttons = Frame(mainwin, padx = 3)
table_frame_buttons.config(bg='white')

table_frame = Frame(mainwin, padx = 3)
table_frame.config(bg='white')

inicio_frame = Frame(mainwin, padx = 3)
inicio_frame.config(bg='white')

nuevo_frame = Frame(mainwin, padx = 3)
nuevo_frame.config(bg='white')

registros_frame = Frame(mainwin, padx = 3)
registros_frame.config(bg='white')

# ayuda_frame = Frame(mainwin, padx = 3)
# ayuda_frame.config(bg='white')

formulas_frame = Frame(mainwin, padx = 3)
formulas_frame.config(bg='white')

comparar_frame = Frame(mainwin, padx = 3)
comparar_frame.config(bg='white')

table_frame_buttons.pack(side='top', anchor='nw')
table_frame.pack(side='bottom')
inicio_frame.pack(side='bottom')
nuevo_frame.pack(side='bottom')
registros_frame.pack(side='bottom')
# ayuda_frame.pack(side='bottom')
formulas_frame.pack(side='bottom')
comparar_frame.pack(side='bottom')

nuevo_frame.pack_forget()
registros_frame.pack_forget()
# ayuda_frame.pack_forget()
formulas_frame.pack_forget()
comparar_frame.pack_forget()

# creacion del tree y scrollbar
tree = ttk.Treeview(registros_frame)
scrollbar = ttk.Scrollbar(registros_frame)
tree.pack(side='left', fill='both', expand=True)
scrollbar.pack(side='right', fill='y')
# tree.pack_forget()
# scrollbar.pack_forget()

# creacion de la imagen de inicio
imageinicio = Image.open('imageninicio.jpg')
imageinicioqr = imageinicio.resize((450,350))
photoimageq = ImageTk.PhotoImage(imageinicioqr)
imagendeinicio = Label(inicio_frame, bg='white', image=photoimageq)
imagendeinicio.pack()

# creacion de la imagen de Formulas
imageformulas = Image.open('imagenformulas.jpg')
imageformulasqr = imageformulas.resize((450,350))
photoimageqformulas = ImageTk.PhotoImage(imageformulasqr)
imagendeformulas = Label(formulas_frame, bg='white', image=photoimageqformulas)
imagendeformulas.pack()

# creacion de los combobox
groupcombotop = Frame(nuevo_frame, background='white')
groupcombobot = Frame(nuevo_frame, background='white')
comboframe1 = Frame(nuevo_frame, background='white')
comboframe2 = Frame(nuevo_frame, background='white')
comboframe3 = Frame(nuevo_frame, background='white')
comboframe4 = Frame(nuevo_frame, background='white')
comboframe5 = Frame(nuevo_frame, background='white')
# simbolo metros cubicos
medida1 = Label(comboframe5, text='m³/h', width=4, bg='white', font=my_font)
groupingresa = Frame(nuevo_frame, background='white')
groupingresa2 = Frame(nuevo_frame, background='white')
maqoptions = [
    "Hyundai Robex 200LC-9SB",
    "Doosan DX225LCA"
]
cuchoptions = []
materialoptions = [
    "Arena",
    "Grava",
    "Arcilla",
    "Tierra comun"
]
estadooptions = []
convertidooptions = [
    "Natural",
    "Suelto",
    "Compactado"
]
myCombo1 = ttk.Combobox(groupcombotop, value=maqoptions, width=25, font = my_fonts)
myCombo2 = ttk.Combobox(groupcombobot, width=25, font=my_fonts)
myCombo3 = ttk.Combobox(comboframe1, value=materialoptions, width=25, font=my_fonts)
myCombo4 = ttk.Combobox(comboframe2, value=estadooptions, width=25, font=my_fonts)
myCombo5 = ttk.Combobox(comboframe3, value=convertidooptions, width=25, font=my_fonts)
ingresardat_text = StringVar(comboframe4, '', 'capacidadcucharon')
ingresardat_entry = Entry(comboframe4, textvariable=ingresardat_text, width=10, font=my_font)

imagenpala = Label(groupcombobot, bg='white')
imagenexca = Label(groupcombotop, bg='white')



# todo sobre comparar
# frame1 = Frame(comparar_frame, background='white')
# frame2 = Frame(comparar_frame, background='white')
# frame3 = Frame(comparar_frame, background='white')
# frame4 = Frame(comparar_frame, background='white')
# frame5 = Frame(comparar_frame, background='white')
# frame6 = Frame(comparar_frame, background='white')
# frame7 = Frame(comparar_frame, background='white')
# frame8 = Frame(comparar_frame, background='white')

# id_label1 = Label(frame1, text='ID:', font=my_fontb, pady=10, padx=10, bg='white', relief="solid")
# spacer1 = Label(frame1, width=15, bg='white')
# id_label2 = Label(frame1, font=my_fontb, pady=10, padx=10, bg='white', relief="solid")
# id_label3 = Label(frame1, font=my_fontb, pady=10, padx=10, bg='white', relief="solid")
# excavadora_label1 = Label(frame2, text='Excavadora:', font=my_fontb, pady=10, padx=10, bg='white', relief="solid")
# spacer2 = Label(frame2, width=6, bg='white')
# excavadora_label2 = Label(frame2, font=my_fontb, pady=10, padx=10, bg='white', relief="solid")
# excavadora_label3 = Label(frame2, font=my_fontb, pady=10, padx=10, bg='white', relief="solid")
# cuchara_label1 = Label(frame3, text='Cuchara:', font=my_fontb, pady=10, padx=10, bg='white', relief="solid")
# spacer3 = Label(frame3, width=9, bg='white')
# cuchara_label2 = Label(frame3, font=my_fontb, pady=10, padx=10, bg='white', relief="solid")
# cuchara_label3 = Label(frame3, font=my_fontb, pady=10, padx=10, bg='white', relief="solid")
# material_label1 = Label(frame4, text='Material:', font=my_fontb, pady=10, padx=10, bg='white', relief="solid")
# spacer4 = Label(frame4, width=10, bg='white')
# material_label2 = Label(frame4, font=my_fontb, pady=10, padx=10, bg='white', relief="solid")
# material_label3 = Label(frame4, font=my_fontb, pady=10, padx=10, bg='white', relief="solid")
# eactual_label1 = Label(frame5, text='Estado actual:', font=my_fontb, pady=10, padx=10, bg='white', relief="solid")
# spacer5 = Label(frame5, width=4, bg='white')
# eactual_label2 = Label(frame5, font=my_fontb, pady=10, padx=10, bg='white', relief="solid")
# eactual_label3 = Label(frame5, font=my_fontb, pady=10, padx=10, bg='white', relief="solid")
# econvertido_label1 = Label(frame6, text='Estado convertido:', font=my_fontb, pady=10, padx=10, bg='white', relief="solid")
# spacer6 = Label(frame6, width=0, bg='white')
# econvertido_label2 = Label(frame6, font=my_fontb, pady=10, padx=10, bg='white', relief="solid")
# econvertido_label3 = Label(frame6, font=my_fontb, pady=10, padx=10, bg='white', relief="solid")
# capacidad_label1 = Label(frame7, text='Capacidad:', font=my_fontb, pady=10, padx=10, bg='white', relief="solid")
# spacer7 = Label(frame7, width=6, bg='white')
# capacidad_label2 = Label(frame7, font=my_fontb, pady=10, padx=10, bg='white', relief="solid")
# capacidad_label3 = Label(frame7, font=my_fontb, pady=10, padx=10, bg='white', relief="solid")
# rendimiento_label1 = Label(frame8, text='Rendimiento:', font=my_fontb, pady=10, padx=10, bg='white', relief="solid")
# spacer8 = Label(frame8, width=5, bg='white')
# rendimiento_label2 = Label(frame8, font=my_fontb, pady=10, padx=10, bg='white', relief="solid")
# rendimiento_label3 = Label(frame8, font=my_fontb, pady=10, padx=10, bg='white', relief="solid")

def comboclick3(event):
    if myCombo3.get() == "Arena":
        estadooptions = [
            "Banco (1)",
            "Suelto (1)",
            "Compactado (1)"
        ]
    elif myCombo3.get() == "Grava":
        estadooptions = [
            "Banco (2)",
            "Suelto (2)",
            "Compactado (2)",
        ]
    elif myCombo3.get() == "Arcilla":
        estadooptions = [
            "Banco (3)",
            "Suelto (3)",
            "Compactado (3)",
        ]
    elif myCombo3.get() == "Tierra comun":
        estadooptions = [
            "Banco (4)",
            "Suelto (4)",
            "Compactado (4)",
        ]
    myCombo4.configure(value=estadooptions)


def comboclick1(event):
        if myCombo1.get() == "Hyundai Robex 200LC-9SB":
            imagemaq = Image.open('Hyundai_Robex_200LC-9SB.jpg')
            # imagemaqr = imagemaq.resize((150,150))
        elif myCombo1.get() == "Doosan DX225LCA":
            imagemaq = Image.open('Doosan_DX225LCA.jpg')
            
        imagemaqr = imagemaq.resize((150,150))

        photoimagemaq = ImageTk.PhotoImage(imagemaqr)

        imagenexca.config(image=photoimagemaq)
        imagenexca.image = photoimagemaq

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
        
        myCombo2.configure(value=cuchoptions)
    
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
        global flag1
        flag1 = 0
    

def small_populate_list():

    # Definir las columnas y los encabezados personalizados
    
    tree.column('#0', width=1)
    # excavadora, cuchara, material, eactual, econvertido, capacidad, rendimiento
    headers = ['ID', 'Tipo de excavadora', 'Tipo de cuchara', 'Clase de material', 'Estado actual', 'Estado convertido', 'Capacidad', 'Rendimiento']
    tree['columns'] = list(range(len(headers)))
    for i, header in enumerate(headers):
        tree.heading(i, text=header, anchor='center')

    # Agregar las filas de datos
    # for row in rows[0:]:
    #     tree.insert('', 'end', values=row)
    for row in rows[0:]:
        # redondear el valor de rendimiento
        estado_actual = row[4][:-3]
        rendimiento = round(float(row[7]), 2)
        # agregar la fila redondeada al tree
        tree.insert('', 'end', values=(row[0], row[1], row[2], row[3], estado_actual, row[5], row[6], rendimiento))

    # Crear una barra de desplazamiento
    # scrollbar = ttk.Scrollbar(table_frame, orient='vertical', command=tree.yview)
    scrollbar.config(orient='vertical', command=tree.yview)
    tree.config(yscrollcommand=scrollbar.set)

    # Agregar la tabla y la barra de desplazamiento al marco
    # tree.pack(side='left', fill='both', expand=True)
    # tree.pack()
    # scrollbar.pack(side='right', fill='y')

    # Configurar los encabezados para que encajen horizontalmente
    for i, header in enumerate(headers):
        tree.heading(i, text=header, anchor=CENTER)
        tree.column(i, anchor=CENTER)

    tree.column(0, width=1)
    tree.column(1, width=200)
    tree.column(2, width=150)
    tree.column(3, width=120)
    tree.column(4, width=180)
    tree.column(5, width=180)
    tree.column(6, width=180)
    tree.column(7, width=180)

    mainwin.update_idletasks()

def actualizar_lista():
    tree.delete(*tree.get_children())
    rows = db.fetch()
    for row in rows[0:]:
        # redondear el valor de rendimiento
        estado_actual = row[4][:-3]
        rendimiento = round(float(row[7]), 2)
        # agregar la fila redondeada al tree
        tree.insert('', 'end', values=(row[0], row[1], row[2], row[3], estado_actual, row[5], row[6], rendimiento))

    global thisid
    # if flag1 != 0:
    thisid = 0
    for row in db.fetch():
        thisid = thisid + 1
    print(thisid)
        # print('flag')
        # print(flag_mostrar_detalles)
        # if flag_mostrar_detalles == 0:
        #     small_populate_list()
        # else:
        #     populate_list()

def eliminar_id():
    # iniciar_btn["state"] = "disabled"
    # detalles_btn["state"] = "disabled"
    global thisid
    global flag_mostrar_detalles

    # db.remove(thisid)
    selection = tree.selection()
    ideliminar = tree.item(selection)['values'][0]
    # ideliminar = int(dato_eliminar_entry.get())
    db.remove(ideliminar)
    
    # thisid = 0
    actualizar_lista()
    # for row in db.fetch():
    #     thisid = thisid + 1
    print('flag')
    print(flag_mostrar_detalles)
    # if flag_mostrar_detalles == 0:
    #     new_small_populate_list()
    # else:
    #     new_populate_list()

def editar_id():
    global ideditar
    selection = tree.selection()
    ideditar = tree.item(selection)['values'][0]
    excavadora = tree.item(selection)['values'][1]
    cuchara = tree.item(selection)['values'][2]
    material = tree.item(selection)['values'][3]
    # eactual = tree.item(selection)['values'][4]
    econvertido = tree.item(selection)['values'][5]
    capacidad = tree.item(selection)['values'][6]

    eactual = db.fetch_eactual(ideditar)

    print('id:', ideditar)
    print('excavadora:', excavadora)
    print('cuchara:', cuchara)
    print('material:', material)
    print('estado actual:', eactual)
    print('estado convertido:', econvertido)
    print('capacidad:', capacidad)

    myCombo1.current(1)
    print(1)
    comboclick1(None)
    myCombo2.current(1)
    print(2)
    comboclick2(None)
    myCombo3.current(1)
    print(3)
    comboclick3(None)
    myCombo4.current(1)
    print(4)
    myCombo5.current(1)

    seleccionar_por_valor(excavadora, myCombo1)
    comboclick1(None)
    seleccionar_por_valor(cuchara, myCombo2)
    comboclick2(None)
    seleccionar_por_valor(material, myCombo3)
    comboclick3(None)
    seleccionar_por_valor(eactual, myCombo4)
    seleccionar_por_valor(econvertido, myCombo5)
    ingresardat_entry.delete('0','end')
    ingresardat_entry.insert(0, capacidad)

    nuevo()

def comparar_id():

    global textvariable11
    global textvariable12
    global textvariable21
    global textvariable22
    global textvariable31
    global textvariable32
    global textvariable41
    global textvariable42
    global textvariable51
    global textvariable52
    global textvariable61
    global textvariable62
    global textvariable71
    global textvariable72
    global textvariable81
    global textvariable82

    selection = tree.selection()
    if len(selection) == 2:
        ideditar1 = tree.item(selection[0])['values'][0]
        ideditar2 = tree.item(selection[1])['values'][0]
        # Obtener los valores de la fila 1
        row1 = db.fetch_by_id(ideditar1)
        excavadora1, cuchara1, material1, eactual1, econvertido1, capacidad1, rendimiento1 = row1[1:]
        # Obtener los valores de la fila 2
        row2 = db.fetch_by_id(ideditar2)
        excavadora2, cuchara2, material2, eactual2, econvertido2, capacidad2, rendimiento2 = row2[1:]

        print('id1:',ideditar1)
        print('id1:',excavadora1)
        print('id1:',cuchara1)
        print('id1:',material1)
        print('id1:',eactual1)
        print('id1:',econvertido1)
        print('id1:',capacidad1)
        print('id1:',rendimiento1)

        print('id2:',ideditar2)
        print('id2:',excavadora2)
        print('id2:',cuchara2)
        print('id2:',material2)
        print('id2:',eactual2)
        print('id2:',econvertido2)
        print('id2:',capacidad2)
        print('id2:',rendimiento2)

        # # frame1 = Frame(comparar_frame, background='white')
        # # frame2 = Frame(comparar_frame, background='white')
        # # frame3 = Frame(comparar_frame, background='white')
        # # frame4 = Frame(comparar_frame, background='white')
        # # frame5 = Frame(comparar_frame, background='white')
        # # frame6 = Frame(comparar_frame, background='white')
        # # frame7 = Frame(comparar_frame, background='white')
        # # frame8 = Frame(comparar_frame, background='white')

        # # textvariable11 = StringVar(frame1)
        # # textvariable12 = StringVar(frame1)
        # # textvariable21 = StringVar(frame2)
        # # textvariable22 = StringVar(frame2)
        # # textvariable31 = StringVar(frame3)
        # # textvariable32 = StringVar(frame3)
        # # textvariable41 = StringVar(frame4)
        # # textvariable42 = StringVar(frame4)
        # # textvariable51 = StringVar(frame5)
        # # textvariable52 = StringVar(frame5)
        # # textvariable61 = StringVar(frame6)
        # # textvariable62 = StringVar(frame6)
        # # textvariable71 = StringVar(frame7)
        # # textvariable72 = StringVar(frame7)
        # # textvariable81 = StringVar(frame8)
        # # textvariable82 = StringVar(frame8)

        # textvariable11 = ideditar1
        # textvariable12 = ideditar2
        # textvariable21 = excavadora1
        # textvariable22 = excavadora2
        # textvariable31 = cuchara1
        # textvariable32 = cuchara2
        # textvariable41 = material1
        # textvariable42 = material2
        # textvariable51 = eactual1
        # textvariable52 = eactual2
        # textvariable61 = econvertido1
        # textvariable62 = econvertido2
        # textvariable71 = capacidad1
        # textvariable72 = capacidad2
        # textvariable81 = rendimiento1
        # textvariable82 = rendimiento2

        
        # frame1.pack(fill='x')
        # # id_label1 = Label(frame1, text='ID:', font=my_fontb, pady=10, padx=10, bg='white')
        # id_label1.pack(side='left')

        # # spacer1 = Label(frame1, width=15, bg='white')
        # spacer1.pack(side='left')
        
        # id_label2.config(text=textvariable11)
        # id_label2.pack(side='left')
        
        # id_label3.config(text=textvariable12)
        # id_label3.pack(side='left')

        
        # frame2.pack(fill='x')
        # # excavadora_label1 = Label(frame2, text='Excavadora:', font=my_fontb, pady=10, padx=10, bg='white')
        # excavadora_label1.pack(side='left')

        # # spacer2 = Label(frame2, width=6, bg='white')
        # spacer2.pack(side='left')
        
        # excavadora_label2.config(text=textvariable21)
        # excavadora_label2.pack(side='left')
        
        # excavadora_label3.config(text=textvariable22)
        # excavadora_label3.pack(side='left')

        
        # frame3.pack(fill='x')
        # # cuchara_label1 = Label(frame3, text='Cuchara:', font=my_fontb, pady=10, padx=10, bg='white')
        # cuchara_label1.pack(side='left')

        # # spacer3 = Label(frame3, width=9, bg='white')
        # spacer3.pack(side='left')
        
        # cuchara_label2.config(text=textvariable31)
        # cuchara_label2.pack(side='left')
        
        # cuchara_label3.config(text=textvariable32)
        # cuchara_label3.pack(side='left')

        
        # frame4.pack(fill='x')
        # # material_label1 = Label(frame4, text='Material:', font=my_fontb, pady=10, padx=10, bg='white')
        # material_label1.pack(side='left')

        # # spacer4 = Label(frame4, width=10, bg='white')
        # spacer4.pack(side='left')
        
        # material_label2.config(text=textvariable41)
        # material_label2.pack(side='left')
        
        # material_label3.config(text=textvariable42)
        # material_label3.pack(side='left')

        
        # frame5.pack(fill='x')
        # # eactual_label1 = Label(frame5, text='Estado actual:', font=my_fontb, pady=10, padx=10, bg='white')
        # eactual_label1.pack(side='left')

        # # spacer5 = Label(frame5, width=4, bg='white')
        # spacer5.pack(side='left')
        
        # eactual_label2.config(text=textvariable51)
        # eactual_label2.pack(side='left')
        
        # eactual_label3.config(text=textvariable52)
        # eactual_label3.pack(side='left')

        
        # frame6.pack(fill='x')
        # # econvertido_label1 = Label(frame6, text='Estado convertido:', font=my_fontb, pady=10, padx=10, bg='white')
        # econvertido_label1.pack(side='left')

        # # spacer6 = Label(frame6, width=0, bg='white')
        # spacer6.pack(side='left')
        
        # econvertido_label2.config(text=textvariable61)
        # econvertido_label2.pack(side='left')
        
        # econvertido_label3.config(text=textvariable62)
        # econvertido_label3.pack(side='left')

        
        # frame7.pack(fill='x')
        # # capacidad_label1 = Label(frame7, text='Capacidad:', font=my_fontb, pady=10, padx=10, bg='white')
        # capacidad_label1.pack(side='left')

        # # spacer7 = Label(frame7, width=6, bg='white')
        # spacer7.pack(side='left')
        
        # capacidad_label2.config(text=textvariable71)
        # capacidad_label2.pack(side='left')
        
        # capacidad_label3.config(text=textvariable72)
        # capacidad_label3.pack(side='left')

        
        # frame8.pack(fill='x')
        # # rendimiento_label1 = Label(frame8, text='Rendimiento:', font=my_fontb, pady=10, padx=10, bg='white')
        # rendimiento_label1.pack(side='left')

        # # spacer8 = Label(frame8, width=5, bg='white')
        # spacer8.pack(side='left')
        
        # rendimiento_label2.config(text=textvariable81)
        # rendimiento_label2.pack(side='left')
        
        # rendimiento_label3.config(text=textvariable82)
        # rendimiento_label3.pack(side='left')

        # Crear los labels para los nombres de los datos
        nombres_datos = ['id', 'excavadora', 'cuchara', 'material', 'eactual', 'econvertido', 'capacidad', 'rendimiento']
        for i, nombre in enumerate(nombres_datos):
            nombre_label = Label(comparar_frame, text=nombre, font=my_fontb, bg='white', relief='solid', borderwidth=1)
            nombre_label.grid(row=i, column=0, padx=5, pady=5, sticky='w')

        # Datos del primer grupo
        if excavadora1 == "Hyundai Robex 200LC-9SB":
            imagemaq1 = Image.open('Hyundai_Robex_200LC-9SB.jpg')
        elif excavadora1 == "Doosan DX225LCA":
            imagemaq1 = Image.open('Doosan_DX225LCA.jpg')
        imagemaqr1 = imagemaq1.resize((150,150))
        photoimagemaq1 = ImageTk.PhotoImage(imagemaqr1)

        if excavadora2 == "Hyundai Robex 200LC-9SB":
            imagemaq2 = Image.open('Hyundai_Robex_200LC-9SB.jpg')
        elif excavadora2 == "Doosan DX225LCA":
            imagemaq2 = Image.open('Doosan_DX225LCA.jpg')
        imagemaqr2 = imagemaq2.resize((150,150))
        photoimagemaq2 = ImageTk.PhotoImage(imagemaqr2)

        dato1_label = Label(comparar_frame, text=ideditar1, font=my_font, bg='white', relief='groove', borderwidth=1)
        dato1_label.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        dato1_labe2 = Label(comparar_frame, text=excavadora1, font=my_font, bg='white', relief='groove', borderwidth=1)
        dato1_labe2.grid(row=1, column=1, padx=5, pady=5, sticky='w')
        dato1_labe3 = Label(comparar_frame, text=cuchara1, font=my_font, bg='white', relief='groove', borderwidth=1)
        dato1_labe3.grid(row=2, column=1, padx=5, pady=5, sticky='w')
        dato1_labe4 = Label(comparar_frame, text=material1, font=my_font, bg='white', relief='groove', borderwidth=1)
        dato1_labe4.grid(row=3, column=1, padx=5, pady=5, sticky='w')
        dato1_labe5 = Label(comparar_frame, text=eactual1, font=my_font, bg='white', relief='groove', borderwidth=1)
        dato1_labe5.grid(row=4, column=1, padx=5, pady=5, sticky='w')
        dato1_labe6 = Label(comparar_frame, text=econvertido1, font=my_font, bg='white', relief='groove', borderwidth=1)
        dato1_labe6.grid(row=5, column=1, padx=5, pady=5, sticky='w')
        dato1_labe7 = Label(comparar_frame, text=capacidad1, font=my_font, bg='white', relief='groove', borderwidth=1)
        dato1_labe7.grid(row=6, column=1, padx=5, pady=5, sticky='w')
        dato1_labe8 = Label(comparar_frame, text=rendimiento1, font=my_font, bg='white', relief='groove', borderwidth=1)
        dato1_labe8.grid(row=7, column=1, padx=5, pady=5, sticky='w')
        dato1_labe9 = Label(comparar_frame, image=photoimagemaq1, font=my_font, bg='white', relief='groove', borderwidth=1)
        dato1_labe9.grid(row=8, column=1, padx=5, pady=5, sticky='w')
        dato1_labe9.image = photoimagemaq1

        dato2_label = Label(comparar_frame, text=ideditar2, font=my_font, bg='white', relief='groove', borderwidth=1)
        dato2_label.grid(row=0, column=2, padx=5, pady=5, sticky='w')
        dato2_labe2 = Label(comparar_frame, text=excavadora2, font=my_font, bg='white', relief='groove', borderwidth=1)
        dato2_labe2.grid(row=1, column=2, padx=5, pady=5, sticky='w')
        dato2_labe3 = Label(comparar_frame, text=cuchara2, font=my_font, bg='white', relief='groove', borderwidth=1)
        dato2_labe3.grid(row=2, column=2, padx=5, pady=5, sticky='w')
        dato2_labe4 = Label(comparar_frame, text=material2, font=my_font, bg='white', relief='groove', borderwidth=1)
        dato2_labe4.grid(row=3, column=2, padx=5, pady=5, sticky='w')
        dato2_labe5 = Label(comparar_frame, text=eactual2, font=my_font, bg='white', relief='groove', borderwidth=1)
        dato2_labe5.grid(row=4, column=2, padx=5, pady=5, sticky='w')
        dato2_labe6 = Label(comparar_frame, text=econvertido2, font=my_font, bg='white', relief='groove', borderwidth=1)
        dato2_labe6.grid(row=5, column=2, padx=5, pady=5, sticky='w')
        dato2_labe7 = Label(comparar_frame, text=capacidad2, font=my_font, bg='white', relief='groove', borderwidth=1)
        dato2_labe7.grid(row=6, column=2, padx=5, pady=5, sticky='w')
        dato2_labe8 = Label(comparar_frame, text=rendimiento2, font=my_font, bg='white', relief='groove', borderwidth=1)
        dato2_labe8.grid(row=7, column=2, padx=5, pady=5, sticky='w')
        dato2_labe9 = Label(comparar_frame, image=photoimagemaq2, font=my_font, bg='white', relief='groove', borderwidth=1)
        dato2_labe9.grid(row=8, column=2, padx=5, pady=5, sticky='w')
        dato2_labe9.image = photoimagemaq2

        comparar()

def seleccionar_por_valor(valor, combobox):
    indices = [idx for idx, val in enumerate(combobox["values"]) if val == valor]
    if indices:
        combobox.current(indices[0])

def configurar_imagen():
    imageinicio = Image.open('27-1.jpg')
    imageinicioqr = imageinicio.resize((150,150))
    photoimageq = ImageTk.PhotoImage(imageinicioqr)
    imagendeinicio.config(image=photoimageq)
    # imagendeinicio.image = photoimageq
    # imagendeinicio.pack()
    # imagendeinicio.pack_configure(side='top', padx=5, pady=5, anchor='nw', expand=False)

def configurar_nuevo():
    # mainwin.withdraw()
    # selwin=Toplevel()
    
    # selwin.title('Datos')
    global rendimiento

    def grabar_rend():
        global rendimiento
        db.insert(myCombo1.get(), myCombo2.get(), myCombo3.get(), myCombo4.get(), myCombo5.get(), ingresardat_text.get(), rendimiento)
        actualizar_lista()

    def calcular_datos():
        global varfac
        medida1.pack(side='left')

        def calcular_rend():
            global rendimiento
            global flag_ingresar_excavadora

            if ingresardat_text.get() == '' or myCombo1 == '' or myCombo2 == '' or myCombo3 == '' or myCombo4 == '' or myCombo5 == '':
                messagebox.showerror('Campos requeridos', 'Porfavor ingrese datos')
                return
            elif myCombo1.get() == "Hyundai Robex 200LC-9SB" and (float(ingresardat_text.get()) > 1.34 or float(ingresardat_text.get()) < 0.51):
                messagebox.showerror('Fuera de rango','Porfavor ingrese un numero entre 0.51 y 1.34')
                return
            elif myCombo1.get() == "Doosan DX225LCA" and (float(ingresardat_text.get()) > 1.4 or float(ingresardat_text.get()) < 0.92):
                messagebox.showerror('Fuera de rango','Porfavor ingrese un numero entre 0.92 y 1.4')
                return
            else:
                try:
                    print('calculo rendimiento')
                    print(thisid)
                    promed = (51.3 + 75.37 + 263.18 + 84.86 + 116.23) / 5.0
                    rendimiento = (3600 * float(ingresardat_text.get()) * float(varfac) * float(0.7) * float(0.9)) / float(promed)
                    visualizar_text.set(round(rendimiento, 2))
                    # volumen = float(alto_text.get()) * float(ancho_text.get()) * float(largo_text.get())
                    # sobreexcava = volumen*1.15
                    # tiempodecarga = float(db.fetchtiempocarga(thisid))
                    # numerocicloshora = 55.0/(tiempodecarga/60.0)
                    # capacidadporhora = numerocicloshora*float(db.fetchcapacidadneta(thisid))
                    # productividad = capacidadporhora
                    # rendimiento = productividad*8.0
                    # tiempoalquiler = sobreexcava/productividad
                    # alto, ancho, largo, volumen, sobreexcavacion, tiempoalquiler, numerocicloshora, productividad, rendimiento
                    # db.insertarexcava(thisid, alto_text.get(), ancho_text.get(), largo_text.get(), volumen, sobreexcava, tiempoalquiler, numerocicloshora, productividad, rendimiento)
                    
                    # db.insert(myCombo1.get(), myCombo2.get(), myCombo3.get(), myCombo4.get(), myCombo5.get(), ingresardat_text.get(), rendimiento)
                    
                    # volumen_text.set(round(volumen, 2))
                    # sobreexcava_text.set(round(sobreexcava, 2))
                    # tiempoalquiler_text.set(round(tiempoalquiler, 2))
                    # numerocicloshora_text.set(round(numerocicloshora, 2))
                    # productividad_text.set(round(productividad, 2))
                    # rendimiento_text.set(round(rendimiento, 2))
                    
                    flag_ingresar_excavadora = 0
                    global flag1
                    flag1 = 1
                    # small_populate_list()
                    
                except ValueError:
                    flag_ingresar_excavadora = 1
                    messagebox.showerror('No es un numero', 'Por favor ingrese un numero')

        if myCombo4.get() == "Banco (1)" and myCombo5.get() == "Natural":
            # varfac = 1.00
            messagebox.showerror('Seleccion invalida','No se puede convertir de banco a natural.')
            return
        elif myCombo4.get() == "Banco (1)" and myCombo5.get() == "Suelto":
            varfac = 1.10
        elif myCombo4.get() == "Banco (1)" and myCombo5.get() == "Compactado":
            varfac = 0.95
        elif myCombo4.get() == "Suelto (1)" and myCombo5.get() == "Natural":
            varfac = 0.99
        elif myCombo4.get() == "Suelto (1)" and myCombo5.get() == "Suelto":
            # varfac = 0.99
            messagebox.showerror('Seleccion invalida','No se puede convertir de suelto a suelto.')
            return
        elif myCombo4.get() == "Suelto (1)" and myCombo5.get() == "Compactado":
            varfac = 0.86
        elif myCombo4.get() == "Compactado (1)" and myCombo5.get() == "Natural":
            varfac = 1.06
        elif myCombo4.get() == "Compactado (1)" and myCombo5.get() == "Suelto":
            varfac = 1.17
        elif myCombo4.get() == "Compactado (1)" and myCombo5.get() == "Compactado":
            # varfac = 1.01
            messagebox.showerror('Seleccion invalida','No se puede convertir de compactado a compactado.')
            return
        elif myCombo4.get() == "Banco (2)" and myCombo5.get() == "Natural":
            # varfac = 1.00
            messagebox.showerror('Seleccion invalida','No se puede convertir de banco a natural.')
            return
        elif myCombo4.get() == "Banco (2)" and myCombo5.get() == "Suelto":
            varfac = 1.25
        elif myCombo4.get() == "Banco (2)" and myCombo5.get() == "Compactado":
            varfac = 0.90
        elif myCombo4.get() == "Suelto (2)" and myCombo5.get() == "Natural":
            varfac = 0.80
        elif myCombo4.get() == "Suelto (2)" and myCombo5.get() == "Suelto":
            # varfac = 1.00
            messagebox.showerror('Seleccion invalida','No se puede convertir de suelto a suelto.')
            return
        elif myCombo4.get() == "Suelto (2)" and myCombo5.get() == "Compactado":
            varfac = 0.72
        elif myCombo4.get() == "Compactado (2)" and myCombo5.get() == "Natural":
            varfac = 1.11
        elif myCombo4.get() == "Compactado (2)" and myCombo5.get() == "Suelto":
            varfac = 1.39
        elif myCombo4.get() == "Compactado (2)" and myCombo5.get() == "Compactado":
            # varfac = 1.00
            messagebox.showerror('Seleccion invalida','No se puede convertir de compactado a compactado.')
            return
        elif myCombo4.get() == "Banco (3)" and myCombo5.get() == "Natural":
            # varfac = 1.00
            messagebox.showerror('Seleccion invalida','No se puede convertir de banco a natural.')
            return
        elif myCombo4.get() == "Banco (3)" and myCombo5.get() == "Suelto":
            varfac = 1.43
        elif myCombo4.get() == "Banco (3)" and myCombo5.get() == "Compactado":
            varfac = 0.90
        elif myCombo4.get() == "Suelto (3)" and myCombo5.get() == "Natural":
            varfac = 0.70
        elif myCombo4.get() == "Suelto (3)" and myCombo5.get() == "Suelto":
            # varfac = 1.00
            messagebox.showerror('Seleccion invalida','No se puede convertir de suelto a suelto.')
            return
        elif myCombo4.get() == "Suelto (3)" and myCombo5.get() == "Compactado":
            varfac = 0.63
        elif myCombo4.get() == "Compactado (3)" and myCombo5.get() == "Natural":
            messagebox.showerror('Seleccion invalida','Del estado compactado al Natural no existe valor de conversion.')
            return
        elif myCombo4.get() == "Compactado (3)" and myCombo5.get() == "Suelto":
            messagebox.showerror('Seleccion invalida','Del estado compactado al Suelto no existe valor de conversion.')
            return
        elif myCombo4.get() == "Compactado (3)" and myCombo5.get() == "Compactado":
            # varfac = 1.00
            messagebox.showerror('Seleccion invalida','No se puede convertir de compactado a compactado.')
            return
        elif myCombo4.get() == "Banco (4)" and myCombo5.get() == "Natural":
            # varfac = 1.00
            messagebox.showerror('Seleccion invalida','No se puede convertir de banco a natural.')
            return
        elif myCombo4.get() == "Banco (4)" and myCombo5.get() == "Suelto":
            varfac = 1.25
        elif myCombo4.get() == "Banco (4)" and myCombo5.get() == "Compactado":
            varfac = 0.90
        elif myCombo4.get() == "Suelto (4)" and myCombo5.get() == "Natural":
            varfac = 0.80
        elif myCombo4.get() == "Suelto (4)" and myCombo5.get() == "Suelto":
            # varfac = 1.00
            messagebox.showerror('Seleccion invalida','No se puede convertir de suelto a suelto.')
            return
        elif myCombo4.get() == "Suelto (4)" and myCombo5.get() == "Compactado":
            varfac = 0.72
        elif myCombo4.get() == "Compactado (4)" and myCombo5.get() == "Natural":
            varfac = 1.11
        elif myCombo4.get() == "Compactado (4)" and myCombo5.get() == "Suelto":
            varfac = 1.39
        elif myCombo4.get() == "Compactado (4)" and myCombo5.get() == "Compactado":
            # varfac = 1.00
            messagebox.showerror('Seleccion invalida','No se puede convertir de compactado a compactado.')
            return

        calcular_rend()

    def actualizar_datos():
        global ideditar
        # db.update(id, excavadora, cuchara, material, eactual, econvertido, capacidad, rendimiento)
    
        if ingresardat_text.get() == '' or myCombo1 == '' or myCombo2 == '' or myCombo3 == '' or myCombo4 == '' or myCombo5 == '':
            messagebox.showerror('Campos requeridos', 'Porfavor ingrese datos')
            return
        elif myCombo1.get() == "Hyundai Robex 200LC-9SB" and (float(ingresardat_text.get()) > 1.34 or float(ingresardat_text.get()) < 0.51):
            messagebox.showerror('Fuera de rango','Porfavor ingrese un numero entre 0.51 y 1.34')
            return
        elif myCombo1.get() == "Doosan DX225LCA" and (float(ingresardat_text.get()) > 1.4 or float(ingresardat_text.get()) < 0.92):
            messagebox.showerror('Fuera de rango','Porfavor ingrese un numero entre 0.92 y 1.4')
            return
        else:
            try:
                db.update(ideditar, myCombo1.get(), myCombo2.get(), myCombo3.get(), myCombo4.get(), myCombo5.get(), ingresardat_text.get(), rendimiento)
                actualizar_lista()
                print('Datos actualizados')
            except ValueError:
                messagebox.showerror('No es un numero', 'Por favor ingrese un numero')

        
        
        

    # def on_closingselwin():
    #     global flag_ingresar_excavadora
    #     # if 'flag_ingresar_excavadora' in globals():
    #     #     if flag_ingresar_excavadora == 1:
    #     #         db.remove(thisid)
    #     #         flag_ingresar_excavadora = 0
    #     actualizar_lista()
    #     mainwin.deiconify()
    #     selwin.destroy()

    # def comboclick1(event):
    #     if myCombo1.get() == "Hyundai Robex 200LC-9SB":
    #         imagemaq = Image.open('Hyundai_Robex_200LC-9SB.jpg')
    #         # imagemaqr = imagemaq.resize((150,150))
    #     elif myCombo1.get() == "Doosan DX225LCA":
    #         imagemaq = Image.open('Doosan_DX225LCA.jpg')
            
    #     imagemaqr = imagemaq.resize((150,150))

    #     photoimagemaq = ImageTk.PhotoImage(imagemaqr)
    #     # imagenexca = Label(groupcombotop, image=photoimagemaq)
    #     imagenexca.config(image=photoimagemaq)
    #     imagenexca.image = photoimagemaq
    #     # imagenexca.grid(row=2, column=0)
    #     # imagenexca.pack()

    #     if myCombo1.get() == "Hyundai Robex 200LC-9SB":
    #         cuchoptions = [
    #             "SAE APILADO N01",
    #             "SAE APILADO N02",
    #             "SAE APILADO N03",
    #             "SAE APILADO N04",
    #             "SAE APILADO N05",
    #             "SAE APILADO N06",
    #             "SAE APILADO N07",
    #             "SAE APILADO N08",
    #         ]
    #     elif myCombo1.get() == "Doosan DX225LCA":
    #         cuchoptions = [
    #             "Cucharon de uso general",
    #             "Cucharon de servicio pesado",
    #             "Cucharon de servicio severo"
    #         ]
        
    #     # def comboclick2(event):
    #     #     if myCombo2.get() == "SAE APILADO N01":
    #     #         imagepal = Image.open('SAE_APILADO_N_01.jpg')
    #     #         imagepalr = imagepal.resize((150,150))
    #     #         capacidadcuchara = 0.51
    #     #         cuchara = "SAE APILADO N01"
    #     #     elif myCombo2.get() == "SAE APILADO N02":
    #     #         imagepal = Image.open('SAE_APILADO_N_02.jpg')
    #     #         imagepalr = imagepal.resize((150,150))
    #     #         capacidadcuchara = 0.80
    #     #         cuchara = "SAE APILADO N02"
    #     #     elif myCombo2.get() == "SAE APILADO N03":
    #     #         imagepal = Image.open('SAE_APILADO_N_03.jpg')
    #     #         imagepalr = imagepal.resize((150,150))
    #     #         capacidadcuchara = 1.10
    #     #         cuchara = "SAE APILADO N03"
    #     #     elif myCombo2.get() == "SAE APILADO N04":
    #     #         imagepal = Image.open('SAE_APILADO_N_04.jpg')
    #     #         imagepalr = imagepal.resize((150,150))
    #     #         capacidadcuchara = 1.34
    #     #         cuchara = "SAE APILADO N04"
    #     #     elif myCombo2.get() == "SAE APILADO N05":
    #     #         imagepal = Image.open('SAE_APILADO_N_05.jpg')
    #     #         imagepalr = imagepal.resize((150,150))
    #     #         capacidadcuchara = 0.74
    #     #         cuchara = "SAE APILADO N05"
    #     #     elif myCombo2.get() == "SAE APILADO N06":
    #     #         imagepal = Image.open('SAE_APILADO_N_06.jpg')
    #     #         imagepalr = imagepal.resize((150,150))
    #     #         capacidadcuchara = 0.87
    #     #         cuchara = "SAE APILADO N06"
    #     #     elif myCombo2.get() == "SAE APILADO N07":
    #     #         imagepal = Image.open('SAE_APILADO_N_07.jpg')
    #     #         imagepalr = imagepal.resize((150,150))
    #     #         capacidadcuchara = 0.75
    #     #         cuchara = "SAE APILADO N07"
    #     #     elif myCombo2.get() == "SAE APILADO N08":
    #     #         imagepal = Image.open('SAE_APILADO_N_08.jpg')
    #     #         imagepalr = imagepal.resize((150,150))
    #     #         capacidadcuchara = 0.52
    #     #         cuchara = "SAE APILADO N08"
    #     #     elif myCombo2.get() == "Cucharon de uso general":
    #     #         imagepal = Image.open('cucharon_de_uso_general.jpg')
    #     #         imagepalr = imagepal.resize((150,150))
    #     #         capacidadcuchara = 0.39
    #     #         cuchara = "Cucharon de uso general"
    #     #     elif myCombo2.get() == "Cucharon de servicio pesado":
    #     #         imagepal = Image.open('cucharon_de_servicio_pesado.jpg')
    #     #         imagepalr = imagepal.resize((150,150))
    #     #         capacidadcuchara = 0.60
    #     #         cuchara = "Cucharon de servicio pesado"
    #     #     elif myCombo2.get() == "Cucharon de servicio severo":
    #     #         imagepal = Image.open('cucharon_de_servicio_severo.jpg')
    #     #         imagepalr = imagepal.resize((150,150))
    #     #         capacidadcuchara = 0.91
    #     #         cuchara = "Cucharon de servicio severo"
    #     #     photoimagepal = ImageTk.PhotoImage(imagepalr)
    #     #     # imagenpala = Label(groupcombobot, image=photoimagepal)
    #     #     imagenpala.config(image=photoimagepal)
    #     #     imagenpala.image = photoimagepal
    #     #     global flag1
    #     #     flag1 = 0

    #     #     # def ingresaexca():
    #     #     #     global flag_ingresar_excavadora
    #     #     #     global thisid
    #     #     #     if not myCombo1.get() or not myCombo2.get() or excavacion_text.get() == '' or balanceo_text.get() == '' or carga_text.get() == '':
    #     #     #         messagebox.showerror('Required Fields', 'Please include all fields')
    #     #     #         return
    #     #     #     else:
    #     #     #         try:
    #     #     #             flag_ingresar_excavadora = 1
    #     #     #             db.insert('', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    #     #     #             thisid = thisid + 1
    #     #     #             print('nuevo thisid')
    #     #     #             print(thisid)
    #     #     #             eficiencia = 0.75
    #     #     #             tiempocarga = (float(excavacion_text.get()) + float(balanceo_text.get()) + float(carga_text.get()))/3.0
    #     #     #             capacidadneta = capacidadcuchara*eficiencia
    #     #     #             db.insertartiempocarga(thisid, myCombo1.get(), excavacion_text.get(), balanceo_text.get(), carga_text.get(), tiempocarga, cuchara, capacidadcuchara, eficiencia, capacidadneta)
    #     #     #             escojer1_btn["state"] = "normal"
    #     #     #             ingresarexca_btn["state"] = "disabled"
    #     #     #         except ValueError:
    #     #     #             flag_ingresar_excavadora = 0
    #     #     #             db.remove(thisid)
    #     #     #             thisid = thisid - 1
    #     #     #             messagebox.showerror('Not a number', 'Please insert a number')
            
    #     #     # ingresarexca_btn.configure(text='Ingresar excavadora', width=20, command=ingresaexca, font=my_fonts)

    #     # myCombo2.configure(value=cuchoptions, width=25, font=my_fonts)
    #     # myCombo2.current()
    #     # myCombo2.bind("<<ComboboxSelected>>", comboclick2)

    #     myCombo2.configure(value=cuchoptions)
        
    # def comboclick2(event):
    #     if myCombo2.get() == "SAE APILADO N01":
    #         imagepal = Image.open('SAE_APILADO_N_01.jpg')
    #         imagepalr = imagepal.resize((150,150))
    #         capacidadcuchara = 0.51
    #         cuchara = "SAE APILADO N01"
    #     elif myCombo2.get() == "SAE APILADO N02":
    #         imagepal = Image.open('SAE_APILADO_N_02.jpg')
    #         imagepalr = imagepal.resize((150,150))
    #         capacidadcuchara = 0.80
    #         cuchara = "SAE APILADO N02"
    #     elif myCombo2.get() == "SAE APILADO N03":
    #         imagepal = Image.open('SAE_APILADO_N_03.jpg')
    #         imagepalr = imagepal.resize((150,150))
    #         capacidadcuchara = 1.10
    #         cuchara = "SAE APILADO N03"
    #     elif myCombo2.get() == "SAE APILADO N04":
    #         imagepal = Image.open('SAE_APILADO_N_04.jpg')
    #         imagepalr = imagepal.resize((150,150))
    #         capacidadcuchara = 1.34
    #         cuchara = "SAE APILADO N04"
    #     elif myCombo2.get() == "SAE APILADO N05":
    #         imagepal = Image.open('SAE_APILADO_N_05.jpg')
    #         imagepalr = imagepal.resize((150,150))
    #         capacidadcuchara = 0.74
    #         cuchara = "SAE APILADO N05"
    #     elif myCombo2.get() == "SAE APILADO N06":
    #         imagepal = Image.open('SAE_APILADO_N_06.jpg')
    #         imagepalr = imagepal.resize((150,150))
    #         capacidadcuchara = 0.87
    #         cuchara = "SAE APILADO N06"
    #     elif myCombo2.get() == "SAE APILADO N07":
    #         imagepal = Image.open('SAE_APILADO_N_07.jpg')
    #         imagepalr = imagepal.resize((150,150))
    #         capacidadcuchara = 0.75
    #         cuchara = "SAE APILADO N07"
    #     elif myCombo2.get() == "SAE APILADO N08":
    #         imagepal = Image.open('SAE_APILADO_N_08.jpg')
    #         imagepalr = imagepal.resize((150,150))
    #         capacidadcuchara = 0.52
    #         cuchara = "SAE APILADO N08"
    #     elif myCombo2.get() == "Cucharon de uso general":
    #         imagepal = Image.open('cucharon_de_uso_general.jpg')
    #         imagepalr = imagepal.resize((150,150))
    #         capacidadcuchara = 0.39
    #         cuchara = "Cucharon de uso general"
    #     elif myCombo2.get() == "Cucharon de servicio pesado":
    #         imagepal = Image.open('cucharon_de_servicio_pesado.jpg')
    #         imagepalr = imagepal.resize((150,150))
    #         capacidadcuchara = 0.60
    #         cuchara = "Cucharon de servicio pesado"
    #     elif myCombo2.get() == "Cucharon de servicio severo":
    #         imagepal = Image.open('cucharon_de_servicio_severo.jpg')
    #         imagepalr = imagepal.resize((150,150))
    #         capacidadcuchara = 0.91
    #         cuchara = "Cucharon de servicio severo"
    #     photoimagepal = ImageTk.PhotoImage(imagepalr)
    #     # imagenpala = Label(groupcombobot, image=photoimagepal)
    #     imagenpala.config(image=photoimagepal)
    #     imagenpala.image = photoimagepal
    #     global flag1
    #     flag1 = 0
    
    # def comboclick3(event):
    #     if myCombo3.get() == "Arena":
    #         estadooptions = [
    #             "Banco (1)",
    #             "Suelto (1)",
    #             "Compactado (1)"
    #         ]
    #     elif myCombo3.get() == "Grava":
    #         estadooptions = [
    #             "Banco (2)",
    #             "Suelto (2)",
    #             "Compactado (2)",
    #         ]
    #     elif myCombo3.get() == "Arcilla":
    #         estadooptions = [
    #             "Banco (3)",
    #             "Suelto (3)",
    #             "Compactado (3)",
    #         ]
    #     elif myCombo3.get() == "Tierra comun":
    #         estadooptions = [
    #             "Banco (4)",
    #             "Suelto (4)",
    #             "Compactado (4)",
    #         ]

    #     myCombo4.configure(value=estadooptions)

    def trunc_text(text):
        return text[:2] # retorna los dos cinco caracteres

    # maqoptions = [
    #     "Hyundai Robex 200LC-9SB",
    #     "Doosan DX225LCA"
    # ]

    # cuchoptions = []

    # materialoptions = [
    #     "Arena",
    #     "Grava",
    #     "Arcilla",
    #     "Tierra comun"
    # ]

    # estadooptions = []

    # convertidooptions = [
    #     "Natural",
    #     "Suelto",
    #     "Compactado"
    # ]

    global flag1
    flag1 = 1
    # se cambio groupcombo de selwin a mainwin
    # groupcombo = Frame(mainwin, background='white')
    # groupcombotop = Frame(nuevo_frame, background='white')
    # groupcombobot = Frame(nuevo_frame, background='white')
    # comboframe1 = Frame(nuevo_frame, background='white')
    # comboframe2 = Frame(nuevo_frame, background='white')
    # comboframe3 = Frame(nuevo_frame, background='white')
    # comboframe4 = Frame(nuevo_frame, background='white')
    # comboframe5 = Frame(nuevo_frame, background='white')
    # groupingresa = Frame(nuevo_frame, background='white')
    # groupingresa2 = Frame(nuevo_frame, background='white')

    # groupcombo.pack()
    # groupcombo.pack_forget()
    groupcombotop.pack(side='top', fill='x')
    groupcombobot.pack(fill='x')
    comboframe1.pack(fill='x')
    comboframe2.pack(fill='x')
    comboframe3.pack(fill='x')
    comboframe4.pack(fill='x')
    comboframe5.pack(fill='x')
    groupingresa.pack(side='bottom', fill='x')
    groupingresa2.pack(side='left', fill='x')
    selex_label = Label(groupcombotop, text='Seleccionar modelo\nde excavadora:', font=my_fontb, pady=10, padx=10)
    selex_label.pack(side='left')

    spacer1 = Label(groupcombotop, width=9, bg='white')
    spacer1.pack(side='left')

    # myCombo1 = ttk.Combobox(groupcombotop, value=maqoptions, width=25, font = my_fonts)
    myCombo1.current()
    myCombo1.bind("<<ComboboxSelected>>", comboclick1)
    myCombo1.pack(side='left')

    # imagenexca = Label(groupcombotop, bg='white')
    imagenexca.pack(side='left')

    selcu_label = Label(groupcombobot, text='Seleccionar tipo\nde cucharón:', font=my_fontb, pady=10, padx=10)
    selcu_label.pack(side='left')

    spacer2 = Label(groupcombobot, width=13, bg='white')
    spacer2.pack(side='left')

    # myCombo2 = ttk.Combobox(groupcombobot, width=25, font=my_fonts)
    myCombo2.current()
    myCombo2.bind("<<ComboboxSelected>>", comboclick2)
    myCombo2.pack(side='left')

    # imagenpala = Label(groupcombobot, bg='white')
    imagenpala.pack(side='left')

    ingresarclase_material = Label(comboframe1, text='Tipo de material:', font=my_fontb, pady=10, padx=10, bg='white')
    ingresarclase_material.pack(side='left')

    spacer3 = Label(comboframe1, width=12, bg='white')
    spacer3.pack(side='left')

    # myCombo3 = ttk.Combobox(comboframe1, value=materialoptions, width=25, font=my_fonts)
    myCombo3.current()
    myCombo3.bind("<<ComboboxSelected>>", comboclick3)
    myCombo3.pack(side='left')

    ingresarestado_actual = Label(comboframe2, text='Estado de material inicial:', font=my_fontb, pady=10, padx=10, bg='white')
    ingresarestado_actual.pack(side='left')

    spacer4 = Label(comboframe2, width=3, bg='white')
    spacer4.pack(side='left')

    # myCombo4 = ttk.Combobox(comboframe2, value=estadooptions, width=25, font=my_fonts)
    myCombo4.current()
    myCombo4.bind("<<ComboboxSelected>>")
    myCombo4.pack(side='left')

    ingresarestado_convertido = Label(comboframe3, text='Estado de material final:', font=my_fontb, pady=10, padx=10, bg='white')
    ingresarestado_convertido.pack(side='left')

    spacer5 = Label(comboframe3, width=5, bg='white')
    spacer5.pack(side='left')

    # myCombo5 = ttk.Combobox(comboframe3, value=convertidooptions, width=25, font=my_fonts)
    myCombo5.current()
    myCombo5.bind("<<ComboboxSelected>>")
    myCombo5.pack(side='left')

    ingresardat_label = Label(comboframe4, text='Capacidad de cucharón:', font=my_fontb, pady=10, padx=10)
    ingresardat_label.pack(side='left')

    spacer6 = Label(comboframe4, width=5, bg='white')
    spacer6.pack(side='left')

    # ingresardat_text = StringVar(comboframe4, '', 'capacidadcucharon')
    # ingresardat_entry = Entry(comboframe4, textvariable=ingresardat_text, width=10, font=my_font)
    ingresardat_entry.pack(pady=10, side='left')

    rendimiento_label = Label(comboframe5, text='Rendimiento:', font=my_fontb, pady=10, padx=10, bg='white')
    rendimiento_label.pack(side='left')

    visualizar_text = StringVar(comboframe5)
    visualizar_label = Label(comboframe5, textvariable=visualizar_text, font=my_fontb, pady=10, padx=10, bg='white')
    visualizar_label.pack(side='left')

    # medida1 = Label(comboframe5, text='m³/h', width=4, bg='white', font=my_font)
    # medida1.pack(side='left')

    escojer1_btn = Button(groupingresa2, text='Calcular', width=15, command=calcular_datos, font=my_fonts)
    # escojer1_btn.pack(side='top', anchor='center', pady=10)
    escojer1_btn.pack(side='left',  pady=10, padx=10)
    # escojer1_btn["state"] = "disabled"

    grabar_btn = Button(groupingresa2, text='Grabar', width=15, command=grabar_rend, font=my_fonts)
    grabar_btn.pack(side='left', pady=10, padx=10)

    actualizar_btn = Button(groupingresa2, text='Actualizar', width=15, command=actualizar_datos, font=my_fonts)
    actualizar_btn.pack(side='right',  pady=10, padx=10)

    # selwin.protocol("WM_DELETE_WINDOW", on_closingselwin)
    selex_label.config(bg='white')
    selcu_label.config(bg='white')
    ingresardat_label.config(bg='white')
    # selwin.configure(bg='white')
    # selwin.mainloop()

# nuevos botones

def inicio():
    # imagendeinicio.pack()
    ocultar_nuevo()
    ocultar_registros()
    # ocultar_ayuda()
    ocultar_formulas()
    ocultar_comparar()
    inicio_frame.pack()
    comparar_btn.pack_forget()

def ocultar_inicio():
    # imagendeinicio.config(image=None)
    # imagendeinicio.pack_forget()
    inicio_frame.pack_forget()

def nuevo():
    ocultar_inicio()
    ocultar_registros()
    # ocultar_ayuda()
    ocultar_formulas()
    ocultar_comparar()
    nuevo_frame.pack()
    comparar_btn.pack_forget()

def ocultar_nuevo():
    nuevo_frame.pack_forget()

def registros():
    # tree.pack(side='left', fill='both', expand=True)
    # scrollbar.pack(side='right', fill='y')
    ocultar_inicio()
    ocultar_nuevo()
    # ocultar_ayuda()
    ocultar_formulas()
    ocultar_comparar()
    registros_frame.pack()
    eliminar_btn.pack(anchor='n', side='left', padx=5, pady=5)
    editar_btn.pack(anchor='n', side='left', padx=5, pady=5)
    comparar_btn.pack(anchor='n', side='left', padx=5, pady=5)
    # dato_eliminar_entry.pack(anchor='n', side='left', padx=5, pady=5)

def ocultar_registros():
    # tree.pack_forget()
    # scrollbar.pack_forget()
    eliminar_btn.pack_forget()
    editar_btn.pack_forget()
    # dato_eliminar_entry.pack_forget()
    registros_frame.pack_forget()
    
def formulas():
    ocultar_inicio()
    ocultar_nuevo()
    ocultar_registros()
    # ocultar_ayuda()
    ocultar_comparar()
    print("Formulas")
    formulas_frame.pack()
    comparar_btn.pack_forget()

def ocultar_formulas():
    formulas_frame.pack_forget()

# def ayuda():
#     print("Ayuda")
#     ocultar_inicio()
#     ocultar_nuevo()
#     ocultar_registros()
#     ocultar_formulas()
#     ocultar_comparar()
#     ayuda_frame.pack()
#     comparar_btn.pack_forget()

# def ocultar_ayuda():
#     ayuda_frame.pack_forget()
    
def comparar():
    print("Comparar")
    ocultar_inicio()
    ocultar_nuevo()
    ocultar_registros()
    ocultar_formulas()
    comparar_frame.pack()

def ocultar_comparar():
    comparar_frame.pack_forget()

def abrir_pdf():
    # forma1: detectada por antivirus
    # ruta_pdf = os.path.abspath('manual.pdf')
    # os.startfile(ruta_pdf)
    # forma2:
    # ruta_pdf = 'manual.pdf'
    # webbrowser.open_new(ruta_pdf)
    # forma3:
    # ruta_pdf = 'manual.pdf'
    # QDesktopServices.openUrl(QUrl.fromLocalFile(ruta_pdf))
    # forma4:
    ruta_pdf = 'manual.pdf'
    subprocess.Popen([ruta_pdf], shell=True)

def on_select(event):
    # selection = tree.selection()
    selection = event.widget.selection()
    if selection:
        # id = tree.item(selection[0])['values'][0]
        id = tree.item(selection)['values'][0]
        print('id seleccionado:', id)



# asociar eleiminar a tree
tree.bind('<<TreeviewSelect>>', on_select)

# iniciar_btn = Button(table_frame_buttons, text='Iniciar', width=6, command=escoger_excavadora, font=my_fonts)
eliminar_btn = Button(table_frame_buttons, text='Eliminar', width=7, command=eliminar_id, font=my_fonts, bg='#FFEF9F')
editar_btn = Button(table_frame_buttons, text='Editar', width=7, command=editar_id, font=my_fonts, bg='#FFEF9F')
comparar_btn = Button(table_frame_buttons, text='Comparar', width=7, command=comparar_id, font=my_fonts, bg='#FFEF9F')
# dato_eliminar_text = StringVar(table_frame_buttons, '', 'Datoaeliminar')
# dato_eliminar_entry = Entry(table_frame_buttons, textvariable=dato_eliminar_text, width=5, fon=my_font)

# boton_pdf = Button(ayuda_frame, text='Guia de usuario', command=abrir_pdf, font=my_fonts)
# boton_pdf.pack(padx=20, pady=20)

inicio_btn = Button(table_frame_buttons, text='Inicio', width=7, command=inicio, font=my_fonts, bg='white')
nuevo_btn = Button(table_frame_buttons, text='Nuevo', width=7, command=nuevo, font=my_fonts, bg='white')
registros_btn = Button(table_frame_buttons, text='Registros', width=7, command=registros, font=my_fonts, bg='white')
formulas_btn = Button(table_frame_buttons, text='Formulas', width=7, command=formulas, font=my_fonts, bg='white')
ayuda_btn = Button(table_frame_buttons, text='Ayuda', width=7, command=abrir_pdf, font=my_fonts, bg='white')

# iniciar_btn.pack(anchor='n', side='left', padx=5, pady=5)


inicio_btn.pack(anchor='n', side='left', padx=5, pady=5)
nuevo_btn.pack(anchor='n', side='left', padx=5, pady=5)
registros_btn.pack(anchor='n', side='left', padx=5, pady=5)
formulas_btn.pack(anchor='n', side='left', padx=5, pady=5)
ayuda_btn.pack(anchor='n', side='left', padx=5, pady=5)
eliminar_btn.pack(anchor='n', side='left', padx=5, pady=5)
editar_btn.pack(anchor='n', side='left', padx=5, pady=5)
comparar_btn.pack(anchor='n', side='left', padx=5, pady=5)
# dato_eliminar_entry.pack(anchor='n', side='left', padx=5, pady=5)
eliminar_btn.pack_forget()
editar_btn.pack_forget()
comparar_btn.pack_forget()
# dato_eliminar_entry.pack_forget()

# configurar_imagen()
configurar_nuevo()
small_populate_list()
# populate_list()

mainwin.mainloop()