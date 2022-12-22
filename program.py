from tkinter import *

# def calcular_tiempo():
#     tiemp = float(tiempo1_text.get()) + float(tiempo2_text.get()) + float(tiempo3_text.get())

# def calcular_rend():
#     prod = float(tiempo_total_text.get())*float(volumen_text.get())
#     rend = prod*8.0
#     sprod = prod
#     productividad_text.set(sprod)
#     rendimiento_text.set(rend)
#     print('productividad')
#     print(prod)
#     print('rendimiento')
#     print(rend)

app = Tk()
frameapp = Frame(app)
frameapp.pack(side='top',  fill='both',  padx=10,  pady=5,  expand=True)

labelframe = Frame(frameapp, width=50, height=50)
labelframe.pack(side='left', fill='both', padx=5, pady=5, expand=True)
entryframe = Frame(frameapp, width=50, height=50)
entryframe.pack(side='right', fill='both', padx=5, pady=5, expand=True)

# Tiempo de ciclo
tiempo1_text = StringVar()
tiempo1_label = Label(labelframe, text='Tiempo 1', font=('bold',7))
tiempo1_label.pack()
tiempo1_entry = Entry(entryframe, textvariable=tiempo1_text)
tiempo1_entry.pack()

tiempo2_text = StringVar()
tiempo2_label = Label(labelframe, text='Tiempo 2', font=('bold',7))
tiempo2_label.pack()
tiempo2_entry = Entry(entryframe, textvariable=tiempo2_text)
tiempo2_entry.pack()

tiempo3_text = StringVar()
tiempo3_label = Label(labelframe, text='Tiempo 3', font=('bold',7))
tiempo3_label.pack()
tiempo3_entry = Entry(entryframe, textvariable=tiempo3_text)
tiempo3_entry.pack()

tiempo_total_text = StringVar()
tiempo_total_label = Label(labelframe, text='Tiempo Total', font=('bold',7))
tiempo_total_label.pack()
tiempo_total_entry = Entry(entryframe, textvariable=tiempo_total_text)
tiempo_total_entry.pack()

# # Volumen
# volumen_text = StringVar()
# volumen_label = Label(app, text='Volumen', font=('bold',14))

# volumen_entry = Entry(app, textvariable=volumen_text)


# # Buttons
# calcular_btn = Button(app, text='Calcular rendimiento', width=20, command=calcular_rend)


# # Productividad
# productividad_text = StringVar()
# productividad_label = Label(app, text='Productividad', font=('bold',14))
# productividad_label.grid(row=4, column=0, sticky=W)
# productividad_output = Label(app, textvariable=productividad_text, relief=RAISED, font=('bold',14))


# # Rendimiento
# rendimiento_text = StringVar()
# rendimiento_label = Label(app, text='Rendimiento', font=('bold',14))
# rendimiento_label.grid(row=5, column=0, sticky=W)
# rendimiento_output = Label(app, textvariable=rendimiento_text, relief=RAISED, font=('bold',14))


app.title('Rendimiento')
app.geometry('700x400')

# Start program
app.mainloop()