import tkinter as tk
from tkinter import messagebox
import random

# --- Logique du jeu ---
def verifier_nombre():
    try:
        essai = int(entree_nombre.get())
        global tentatives
        tentatives += 1

        if essai < nombre_mystere:
            label_resultat.config(text="C'est plus grand ! ⬆️", fg="blue")
        elif essai > nombre_mystere:
            label_resultat.config(text="C'est plus petit ! ⬇️", fg="orange")
        else:
            messagebox.showinfo("Victoire !", f"Bravo ! Vous avez trouvé le nombre en {tentatives} essais.")
            reinitialiser()
    except ValueError:
        label_resultat.config(text="Erreur : Veuillez entrer un nombre valide.", fg="red")

def reinitialiser():
    global nombre_mystere, tentatives
    nombre_mystere = random.randint(1, 100)
    tentatives = 0
    label_resultat.config(text="Jeu réinitialisé. Bonne chance !", fg="black")
    entree_nombre.delete(0, tk.END)

# --- Interface Graphique (Tkinter) ---
fenetre = tk.Tk()
fenetre.title("Le Nombre Mystère")
fenetre.geometry("350x250")
fenetre.resizable(False, False)

# Initialisation des variables
nombre_mystere = random.randint(1, 100)
tentatives = 0

# Éléments de l'interface (Widgets)
titre = tk.Label(fenetre, text="Devinez le nombre mystère\n(entre 1 et 100)", font=("Helvetica", 12, "bold"))
titre.pack(pady=15)

entree_nombre = tk.Entry(fenetre, font=("Helvetica", 14), width=10, justify="center")
entree_nombre.pack(pady=5)

bouton_valider = tk.Button(fenetre, text="Vérifier", command=verifier_nombre, font=("Helvetica", 12), bg="lightgray")
bouton_valider.pack(pady=10)

label_resultat = tk.Label(fenetre, text="Entrez un nombre pour commencer.", font=("Helvetica", 10))
label_resultat.pack(pady=5)

bouton_reset = tk.Button(fenetre, text="Recommencer", command=reinitialiser, font=("Helvetica", 9))
bouton_reset.pack(side=tk.BOTTOM, pady=10)

# Lancement de l'application
fenetre.mainloop()