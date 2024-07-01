from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- ŞİFRE KAYDEDİCİ------------------------------- #

#Random Şifre oluşturma
def sifre_olusturma():
    harf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numara = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    sembol = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    sifre_harf = [choice(harf) for _ in range(randint(8, 10))]
    sifre_sembol = [choice(sembol) for _ in range(randint(2, 4))]
    sifre_numara = [choice(numara) for _ in range(randint(2, 4))]

    sifre = sifre_harf + sifre_sembol + sifre_numara
    shuffle(sifre)

    karisan_sifre = "".join(sifre)
    sifre_entry.insert(0, karisan_sifre)
    pyperclip.copy(karisan_sifre)

# ---------------------------- şifre kayıt ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    sifre = sifre_entry.get()

    if len(website) == 0 or len(sifre) == 0:
        messagebox.showinfo(title="Oops", message="Lütfen hiçbir alanı boş bırakmadığınızdan emin olun.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Bu girilen bilgiler kayıt edilecektir: "
                                                              f"\nEmail: {email} \nŞifre: {sifre} \nKayıt edilsin mi?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {sifre}\n")
                website_entry.delete(0, END)
                sifre_entry.delete(0, END)



# ---------------------------- GUI Kısmı ------------------------------- #

pencere = Tk()
pencere.title("Şifre Kaydedici")
pencere.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labellar
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email :")
email_label.grid(row=2, column=0)

sifre_label = Label(text="Şifre:")
sifre_label.grid(row=3, column=0)

#Entryler
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "harunxemin@gmail.com")

sifre_entry = Entry(width=23)
sifre_entry.grid(row=3, column=1)

#Butonlar
sifre_olusturma_button = Button(text="Şifre Olustur", command=sifre_olusturma)
sifre_olusturma_button.grid(row=3, column=2)

ekle = Button(text="Ekle", width=34, command=save)
ekle.grid(row=4, column=1, columnspan=2)

pencere.mainloop()