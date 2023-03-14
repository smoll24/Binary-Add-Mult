#Binary Addition

# Importation des modules utiles
from tkinter import messagebox
import tkinter as tk

#Definition des fonctions
def add(num1,num2):
    """Add function, takes in and returns string"""
    
    
    #Enleve les 0 au debut
    if num1[0] == "0":
        num1 = num1[1:]
    
    if num2[0] == "0":
        num2 = num2[1:]
    
    #make so occupy same number of bits
    if len(num1) > len(num2):
        num2 = num2.zfill(len(num1))
    if len(num1) < len(num2):
        num1 = num1.zfill(len(num2))
    
    print("num1 :",num1,", num 2 :",num2)
    
    carry = 0
    result = ""
    i = len(num1)-1
    while i!=-1:
        if carry == 0:
            if (num1[i] == "0") and (num2[i] == "0"):
                result = "0"+result
                carry = 0
            elif (num1[i] == "1") and (num2[i] == "1"):
                result = "0"+result
                carry = 1
            elif ((num1[i] == "1") and (num2[i] == "0")) or ((num1[i] == "0") and (num2[i] == "1")) :
                result = "1"+result
                carry = 0
                
        elif carry == 1:
            if (num1[i] == "0") and (num2[i] == "0"):
                result = "1"+result
                carry = 0
            elif (num1[i] == "1") and (num2[i] == "1"):
                result = "1"+result
                carry = 1
            elif ((num1[i] == "1") and (num2[i] == "0")) or ((num1[i] == "0") and (num2[i] == "1")) :
                result = "0"+result
                carry = 1
        i -= 1
        print(result)
    
    if carry == 1:
        result = "1"+result
    
    while result[0] != "1":
        result = result[1:]
        
    while len(result) != len(num1):
        num1 = "0"+num1
        num2 = "0"+num2
        
    print("result of addition:",result)
    return result,num1,num2


def calculate():
    #Gets entries from user
    num1 = champSaisie_num1.get()
    num2 = champSaisie_num2.get()
    
    try:
        for i in range(len(num1)):
            assert num1[i] == "0" or num1[i] == "1"
        for i in range(len(num2)):
            assert num2[i] == "0" or num2[i] == "1"
            
        result,num1,num2 = add(num1,num2)
        
    except Exception as e:
        messagebox.showerror(title='Erreur de saisis', message='Erreur de saisis. \nSaisissez un nombre valide.')
        print (e)
    
    #Changes text in the base fields
    if champSaisie_num1.index("end") != 0:
        champSaisie_num1.delete(0,"end")
    champSaisie_num1.insert(0,num1)
    
    if champSaisie_num2.index("end") != 0:
        champSaisie_num2.delete(0,"end")
    champSaisie_num2.insert(0,num2)
    
    #Configure la boite du resultat pour que l'utilisateur ne puisse pas la modifier
    text_resultat.configure(state="normal")
    text_resultat.delete("1.0","end")
    
    text_resultat.insert("end",result)
    
    text_resultat.tag_add("all", "1.0", "end")
    text_resultat.tag_config("all",justify="center")
    
    text_resultat.configure(state="disabled")


# Création de la fenêtre tkinter
def create_window():
  global champSaisie_num1, champSaisie_num2, text_resultat, root, fenetre
  
  root = tk.Tk()
  root.geometry('400x250')
  root.title('Addition Binaire')
  root.configure(background='#e4e4e4')
  
  # Création d'une autre frame pour la centrer
  fenetre = tk.Frame(root)
  fenetre.pack()
  fenetre.configure(background='#e4e4e4')
  
  #CREATION DES BOUTONS
  bouton_quitter = tk.Button(fenetre, text='Quitter', command=root.destroy)
  bouton_quitter.grid(row=5, column=1, padx=6, pady=6, ipadx=5)
  
  bouton_calculer = tk.Button(fenetre, text='Calculer', command=calculate)
  bouton_calculer.grid(row=3, column=1, padx=6, pady=6, ipadx=5)
  
  #CREATIONS DES ZONES DE TEXTE
  entete = tk.Label(fenetre, text='Addition Binaire', font=('Arial', 14, 'bold'), fg='#0c6bab', bg='#e4e4e4')
  entete.grid(row=0, column=1, pady=10)
  
  plus_label = tk.Label(fenetre, text='+', bg='#e4e4e4')
  plus_label.grid(row=2, column=0)
  
  equal_label = tk.Label(fenetre, text='=', bg='#e4e4e4')
  equal_label.grid(row=4, column=0)
  
  #CREATION DES CHAMPS DE SAISIE
  champSaisie_num1 = tk.Entry(fenetre, font='12', width=15, justify="center")
  champSaisie_num1.grid(row=1, column=1)
  
  champSaisie_num2 = tk.Entry(fenetre, font='12', width=15, justify="center")
  champSaisie_num2.grid(row=2, column=1)
  
  text_resultat = tk.Text(fenetre, font='12', width=15, height="1")
  text_resultat.grid(row=4, column=1)
  
  text_resultat.configure(state="disabled")
  
  # Programme principal 
  fenetre.mainloop()    # Boucle d'attente des événements

def quitter():
    global root
    try:
        root.destroy()
    except:
        pass

def main():
    quitter()
    create_window()

if __name__ == "__main__":
    main()
