from tkinter import *
from db import Database

win=Tk()
win.geometry('700x500')

def escojer_excavadora():
    print('excavadora1')

    def calcular_rend():
            prod = float(tiempo_total_text.get())*float(volumen_text.get())
            rend = prod*8.0
            productividad_text.set(prod)
            rendimiento_text.set(rend)
            print('productividad')
            print(prod)
            print('rendimiento')
            print(rend)

    app = Tk()

    # Tiempo de ciclo
    tiempo1_text = StringVar(app,'','tiempo1')
    tiempo1_label = Label(app, text='Tiempo 1', font=('bold',14), pady=10)
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

    tiempo_total_text = StringVar(app,'','tiempototal')
    tiempo_total_label = Label(app, text='Tiempo Total', font=('bold',14), pady=10)
    tiempo_total_label.grid(row=1, column=0, sticky=W)
    tiempo_total_entry = Entry(app, textvariable=tiempo_total_text)
    tiempo_total_entry.grid(row=1, column=1)

    # Volumen
    volumen_text = StringVar(app,'','volumen')
    volumen_label = Label(app, text='Volumen', font=('bold',14), pady=10)
    volumen_label.grid(row=2, column=0, sticky=W)
    volumen_entry = Entry(app, textvariable=volumen_text)
    volumen_entry.grid(row=2, column=1)

    # Productividad
    productividad_text = StringVar(app,'','prod')
    productividad_label = Label(app, text='Productividad', font=('bold',14), pady=10)
    productividad_label.grid(row=4, column=0, sticky=W)
    productividad_output = Label(app, textvariable=productividad_text, relief=RAISED, font=('bold',14))
    productividad_output.grid(row=4, column=1)

    # Rendimiento
    rendimiento_text = StringVar(app,'','rend')
    rendimiento_label = Label(app, text='Rendimiento', font=('bold',14), pady=10)
    rendimiento_label.grid(row=5, column=0, sticky=W)
    rendimiento_output = Label(app, textvariable=rendimiento_text, relief=RAISED, font=('bold',14))
    rendimiento_output.grid(row=5, column=1)

    # Buttons
    calcular_btn = Button(app, text='Calcular rendimiento', width=20, command=calcular_rend)
    calcular_btn.grid(row=3, column=0, pady=10, padx=3)

    app.title('Rendimiento')
    app.geometry('700x400')

    app.mainloop()

# Buttons
escojer1_btn = Button(win, text='Excavadora1', width=20, command=escojer_excavadora)
escojer1_btn.grid(row=0, column=0, pady=10, padx=3)

win.mainloop()