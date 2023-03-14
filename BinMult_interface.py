#Binary Multiplication

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
    return result

def mult(num1,num2):
    """Multiplication function, takes in and returns string"""
    
    #Enleve les 0 au debut
    if num1[0] == "0":
        num1 = num1[1:]
    
    if num2[0] == "0":
        num2 = num2[1:]
    
    #Create list of doubles of second number given
    i = 0
    l_doubles = [num2]
    for i in range(len(num1)):
        l_doubles.append(l_doubles[i]+"0")
        i += 1
    print("doubles:",l_doubles)
    
    #Create list of indexes using first number given (index of each 1 in the string)
    i=0
    l_indexes = []
    for i in range(len(num1)):
        if num1[i] == "1":
            l_indexes.append(len(num1)-i-1)
        i += 1
    print("indexes:",l_indexes)
    
    #add each double with the position of the indexes
    somme = l_doubles[l_indexes[0]]
    
    i = 0
    if len(l_indexes) > 1:
        for i in range(len(l_indexes)-1):
            add_num = l_doubles[l_indexes[i+1]]
            somme = add(somme,add_num)
            i += 1
         
    while len(somme) != len(num1):
        num1 = "0"+num1
        num2 = "0"+num2 
    
    print("result of multiplication:",somme)
    return somme,num1,num2,l_doubles,l_indexes


def calculate():
    #Gets entries from user
    num1 = champSaisie_num1.get()
    num2 = champSaisie_num2.get()
    
    try:
        for i in range(len(num1)):
            assert num1[i] == "0" or num1[i] == "1"
        for i in range(len(num2)):
            assert num2[i] == "0" or num2[i] == "1"
            
        result,num1,num2,doubles,indexes = mult(num1,num2)
        
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
    
    #Configure la boite du resultat
    text_resultat.configure(state="normal")
    text_resultat.delete("1.0","end")
    text_resultat.insert("end","= "+result)
    text_resultat.tag_add("all", "1.0", "end")
    text_resultat.tag_config("all",justify="center")
    text_resultat.configure(state="disabled")
         
    #Configure la boite gauche de la methode egyptienne
    text_calc1.configure(state="normal")
    text_calc1.delete("1.0","end")
    
    i=(len(num1))-1
    while i!=0:
        tag = "rouge" if num1[i]=="1" else ""
        text_calc1.insert("end",num1[i]+"\n",(tag))
        i-=1
    text_calc1.tag_config("rouge",foreground="red")  
    
    text_calc1.tag_add("all", "1.0", "end")
    text_calc1.tag_config("all",justify="center")
    text_calc1.configure(state="disabled")
                    
    #Configure la boite droite de la methode egyptienne
    
    text_calc2.configure(state="normal")
    text_calc2.delete("1.0","end")
    
    i=(len(num1))-1
    a=0
    while i!=0:
        tag = "rouge" if num1[i]=="1" else ""
        text_calc2.insert("end",doubles[a]+"\n",(tag))
        i-=1
        a+=1
    text_calc2.tag_config("rouge",foreground="red")  
    
    text_calc2.tag_add("all", "1.0", "end")
    text_calc2.tag_config("all",justify="center")


# Création de la fenêtre tkinter
def create_window():
  global champSaisie_num1, champSaisie_num2, text_resultat, root, fenetre, text_calc1, text_calc2
  
  root = tk.Tk()
  root.geometry('400x400')
  root.title('Multiplication Binaire')
  root.configure(background='#e4e4e4')
  
  # Création d'une autre frame pour la centrer
  fenetre = tk.Frame(root)
  fenetre.pack()
  fenetre.configure(background='#e4e4e4')

  #CREATIONS DES ZONES DE TEXTE
  entete = tk.Label(fenetre, text='Multiplication Binaire', font=('Arial', 14, 'bold'), fg='#0c6bab', bg='#e4e4e4')
  entete.grid(row=0, column=0, columnspan=3, pady=10)
  
  times_label = tk.Label(fenetre, text=' x ', bg='#e4e4e4')
  times_label.grid(row=1, column=1)
  
  res_label = tk.Label(fenetre, text='\nResultat', bg='#e4e4e4')
  res_label.grid(row=5, column=0, columnspan=3)
  
  #CREATION DES CHAMPS DE SAISIE
  champSaisie_num1 = tk.Entry(fenetre, font='12', width=15, justify="center")
  champSaisie_num1.grid(row=1, column=0)
  
  champSaisie_num2 = tk.Entry(fenetre, font='12', width=15, justify="center")
  champSaisie_num2.grid(row=1, column=2)
  
  text_resultat = tk.Text(fenetre, font='12', width=15, height="1")
  text_resultat.grid(row=6, column=0, columnspan=3)
  text_resultat.configure(state="disabled")
  
  text_calc1 = tk.Text(fenetre, font='12', width=15, height=1)
  text_calc1.grid(row=4, column=0)
    
  text_calc2 = tk.Text(fenetre, font='12', width=15, height=1)
  text_calc2.grid(row=4, column=2)
  
  #CREATION DES BOUTONS
  bouton_quitter = tk.Button(fenetre, text='Quitter', command=root.destroy)
  bouton_quitter.grid(row=7, column=0, columnspan=3, padx=6, pady=6, ipadx=5)
  
  bouton_calculer = tk.Button(fenetre, text='Calculer', command=calculate)
  bouton_calculer.grid(row=2, column=0, columnspan=3, padx=6, pady=6, ipadx=5)
  
  #CREATION DES BOITES
  eg_label = tk.Label(fenetre, text='\nMethode egyptienne', bg='#e4e4e4')
  eg_label.grid(row=3, column=0, columnspan=3)
     
  text_calc1 = tk.Text(fenetre, font='12', width=15, height=5)
  text_calc1.grid(row=4, column=0)
  text_calc1.configure(state="disabled")
    
  text_calc2 = tk.Text(fenetre, font='12', width=15, height=5)
  text_calc2.grid(row=4, column=2)
  text_calc2.configure(state="disabled")
  
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

