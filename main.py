from tkinter import Button, Menu, Tk, Frame, Entry, Label, ttk
from tkinter.constants import CENTER, DISABLED, NO
from tkinter.scrolledtext import ScrolledText
import sqlite3
from typing import Collection

class App:
    def __init__(self,master):
        #Inicialization
        self.master=master
        self.master.geometry("1024x720")
        self.master.title("Report of Machinery")
        self.master.configure(bg="black")
        self.master.resizable(width=0, height=0)

        #Main frame creation
        self.main_frame=Frame(self.master)
        self.main_frame.place(relx=.005,rely=.005,relheight=.15,relwidth=.99)

        #Observation frame creation
        self.observation_frame=Frame(self.master)
        self.observation_frame.place(relx=.005,rely=.16,relheight=.25,relwidth=.99)

        #Buttons frame creation
        self.buttons_frame=Frame(self.master)
        self.buttons_frame.place(relx=.005,rely=.42,relheight=0.05,relwidth=.99)

        #Table frame creation
        self.table_frame=Frame(self.master)
        self.table_frame.place(relx=.005,rely=.48,relheight=0.51,relwidth=.99)

        #Menu declaration
        menu_bar=Menu(self.master)
        options_menu=Menu(menu_bar,tearoff=0)
        options_menu.add_command(label="Exportar a Excel")
        options_menu.add_separator()
        options_menu.add_command(label="Representantes")
        options_menu.add_command(label="Conductores")
        menu_bar.add_cascade(label="Opciones",menu=options_menu)
        self.master.config(menu=menu_bar)

        #Widgets

        #Main frame
        Label(self.main_frame,text="Representante").grid(row=0,column=0,pady=5,padx=5)
        self.represent_entry=ttk.Combobox(self.main_frame,width=50)
        self.represent_entry.grid(row=0,column=1,columnspan=2)
        Label(self.main_frame,text="Conductor/a").grid(row=0,column=3,pady=5,padx=5)
        self.driver_entry=ttk.Combobox(self.main_frame,width=50)
        self.driver_entry.grid(row=0,column=4,columnspan=2)
        Label(self.main_frame,text="Obra").grid(row=1,column=0,padx=5,pady=5)
        self.work_number=Entry(self.main_frame)
        self.work_number.grid(row=1,column=1,sticky='w')
        Label(self.main_frame,text="Horas acumuladas").grid(row=2,column=0,padx=5,pady=5)
        self.acumulated_hours=Entry(self.main_frame)
        self.acumulated_hours.grid(row=2,column=1,sticky='w')
        Label(self.main_frame,text="Maquina").grid(row=1,column=2,padx=5,pady=5)
        self.machine=ttk.Combobox(self.main_frame)
        self.machine.grid(row=1,column=3,sticky='w')
        Label(self.main_frame,text="Combustible").grid(row=2,column=2,padx=5,pady=5)
        self.fuel=Entry(self.main_frame)
        self.fuel.grid(row=2,column=3,sticky='w')
        Label(self.main_frame,text="Hora entrada").grid(row=1,column=4,padx=5,pady=5)
        self.in_hour=Entry(self.main_frame)
        self.in_hour.grid(row=1,column=5,sticky='w')
        Label(self.main_frame,text="Hora salida").grid(row=2,column=4,padx=5,pady=5)
        self.out_hour=Entry(self.main_frame)
        self.out_hour.grid(row=2,column=5,sticky='w')

        #Observation frame
        Label(self.observation_frame,text="Observaciones:").pack(padx=5,pady=5)
        self.observation=ScrolledText(self.observation_frame,width=100)
        self.observation.pack(fill='y')

        #Buttons frame
        append_button=Button(self.buttons_frame,text="Ingresar",width=20).grid(row=0,column=0,padx=5,pady=5)
        clean_button=Button(self.buttons_frame,text="Limpiar",width=20).grid(row=0,column=1,padx=5,pady=5)

        #Table frame
        table=ttk.Treeview(self.table_frame,height=100)
        table.pack(padx=5,pady=5)

        table['columns']=("Fecha","Conductor/a","Maquina","H. Entrada","H. Salida","H. Trabajadas","Obra","H. Acumuladas","Representante","Observacion")

        table.column('#0', width=0, stretch=NO)
        table.column('Fecha', anchor=CENTER, width=100)
        table.column('Conductor/a', anchor=CENTER, width=175)
        table.column('Maquina', anchor=CENTER, width=80)
        table.column('H. Entrada', anchor=CENTER, width=70)
        table.column('H. Salida', anchor=CENTER, width=70)
        table.column('H. Trabajadas', anchor=CENTER, width=80)
        table.column('Obra', anchor=CENTER, width=80)
        table.column('H. Acumuladas', anchor=CENTER, width=90)
        table.column('Representante', anchor=CENTER, width=175)
        table.column('Observacion', anchor=CENTER, width=60)

        table.heading('#0', text='', anchor=CENTER)
        table.heading('Fecha', text='Fecha', anchor=CENTER)
        table.heading('Conductor/a', text='Conductor/a', anchor=CENTER)
        table.heading('Maquina', text='Maquina', anchor=CENTER)
        table.heading('H. Entrada', text='H. Entrada', anchor=CENTER)
        table.heading('H. Salida', text='H. Salida', anchor=CENTER)
        table.heading('H. Trabajadas', text='H. Trabajadas', anchor=CENTER)
        table.heading('Obra', text='Obra', anchor=CENTER)
        table.heading('H. Acumuladas', text='H. Acumuladas', anchor=CENTER)
        table.heading('Representante', text='Representante', anchor=CENTER)
        table.heading('Observacion', text='Obs', anchor=CENTER)

        #Insert data: table.insert(parent='', index=0, iid=0, text='', values=('','',''))
        
        

if __name__=="__main__":
    root=Tk()
    App(root)
    root.mainloop()
        