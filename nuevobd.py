from tkinter import *
from tkinter import ttk

mainwin=Tk()
mainwin.geometry('700x500')

def escoger_excavadora():
    mainwin.withdraw()
    selwin=Tk()
    selwin.geometry('700x500')

    def calcular_datos():
        print('excavadora1')
        selwin.withdraw()
        def calcular_rend():
            if tiempo1_text.get() != '' or tiempo2_text.get() != '' or tiempo3_text.get() != '':
                calt = float(tiempo1_text.get()) + float(tiempo2_text.get()) + float(tiempo3_text.get())
                prod = float(calt)*float(volumen_text.get())
                rend = prod*8.0
                productividad_text.set(prod)
                rendimiento_text.set(rend)
            print('productividad')
            print(prod)
            print('rendimiento')
            print(rend)

        def on_closingapp():
            selwin.deiconify()
            app.destroy()

        app = Tk()

        # Tiempo de ciclo
        tiempo1_text = StringVar(app,'','tiempo1')
        tiempo1_label = Label(app, text='Tiempo 1', font=('bold',14), pady=10, padx=10)
        tiempo1_label.grid(row=0, column=0, sticky=W)
        tiempo1_entry = Entry(app, textvariable=tiempo1_text)
        tiempo1_entry.grid(row=0, column=1)

        tiempo2_text = StringVar(app,'','tiempo2')
        tiempo2_label = Label(app, text='Tiempo 2', font=('bold',14))
        tiempo2_label.grid(row=0, column=2, sticky=W)
        tiempo2_entry = Entry(app, textvariable=tiempo2_text)
        tiempo2_entry.grid(row=0, column=3)

        tiempo3_text = StringVar(app,'','tiempo3')
        tiempo3_label = Label(app, text='Tiempo 3', font=('bold',14))
        tiempo3_label.grid(row=0, column=4, sticky=W)
        tiempo3_entry = Entry(app, textvariable=tiempo3_text)
        tiempo3_entry.grid(row=0, column=5)

        # Volumen
        volumen_text = StringVar(app,'','volumen')
        volumen_label = Label(app, text='Volumen', font=('bold',14), pady=10, padx=10)
        volumen_label.grid(row=2, column=0, sticky=W)
        volumen_entry = Entry(app, textvariable=volumen_text)
        volumen_entry.grid(row=2, column=1)

        # Productividad
        productividad_text = StringVar(app,'','prod')
        productividad_label = Label(app, text='Productividad', font=('bold',14), pady=10, padx=10)
        productividad_label.grid(row=4, column=0, sticky=W)
        productividad_output = Label(app, textvariable=productividad_text, relief=RAISED, font=('bold',14))
        productividad_output.grid(row=4, column=1)

        # Rendimiento
        rendimiento_text = StringVar(app,'','rend')
        rendimiento_label = Label(app, text='Rendimiento', font=('bold',14), pady=10, padx=10)
        rendimiento_label.grid(row=5, column=0, sticky=W)
        rendimiento_output = Label(app, textvariable=rendimiento_text, relief=RAISED, font=('bold',14))
        rendimiento_output.grid(row=5, column=1)

        # Buttons
        calcular_btn = Button(app, text='Calcular rendimiento', width=20, command=calcular_rend)
        calcular_btn.grid(row=3, column=0, pady=10, padx=10)

        app.title('Rendimiento')
        app.geometry('700x500')

        app.protocol("WM_DELETE_WINDOW", on_closingapp)
        app.mainloop()
        
    def on_closingselwin():
        mainwin.deiconify()
        selwin.destroy()

    def comboclick1(event):
        imagenexca = Label(selwin, text=myCombo1.get(), font=('bold',14), pady=10, padx=10)
        imagenexca.grid(row=2, column=0, sticky=W)

    def comboclick2(event):
        imagenexca = Label(selwin, text=myCombo2.get(), font=('bold',14), pady=10, padx=10)
        imagenexca.grid(row=5, column=0, sticky=W)

    options = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    selex_label = Label(selwin, text='Seleccionar Excavadora', font=('bold',14), pady=10, padx=10)
    selex_label.grid(row=0, column=0, sticky=W)

    myCombo1 = ttk.Combobox(selwin, value=options)
    myCombo1.current(0)
    myCombo1.bind("<<ComboboxSelected>>", comboclick1)
    myCombo1.grid(row=1, column=0, sticky=W, pady=10, padx=10)

    selcu_label = Label(selwin, text='Seleccionar cucharon', font=('bold',14), pady=10, padx=10)
    selcu_label.grid(row=3, column=0, sticky=W)

    myCombo2 = ttk.Combobox(selwin, value=options)
    myCombo2.current(0)
    myCombo2.bind("<<ComboboxSelected>>", comboclick2)
    myCombo2.grid(row=4, column=0, sticky=W, pady=10, padx=10)

    # Buttons
    escojer1_btn = Button(selwin, text='Ingresar excavacion', width=20, command=calcular_datos)
    escojer1_btn.grid(row=6, column=0, pady=10)

    selwin.protocol("WM_DELETE_WINDOW", on_closingselwin)
    selwin.mainloop()


iniciar_btn = Button(mainwin, text='Escoger excavadora', width=20, command=escoger_excavadora)
iniciar_btn.grid(row=0, column=0, pady=10, padx=10)

mainwin.mainloop()