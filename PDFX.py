import PyPDF2
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        fileentry.delete(0, END)
        fileentry.insert(0, file_path)

def encrypt_pdf():
    filepath = fileentry.get()
    password = passwordentry.get()

    if filepath and password:
        with open(filepath, "rb") as file:
            pdf = PyPDF2.PdfReader(file)
            if not pdf.is_encrypted:
                output_pdf = PyPDF2.PdfWriter()
                for page in pdf.pages:
                    output_pdf.add_page(page)

                output_pdf.encrypt(password)

                output_filepath = filedialog.asksaveasfilename(defaultextension=".pdf")
                if output_filepath:
                    with open(output_filepath, "wb") as output_file:
                        output_pdf.write(output_file)

                    fileentry.delete(0, END)
                    passwordentry.delete(0, END)

                    messagebox.showinfo("Encryption Complete", "PDF file encrypted successfully!")
                else:
                    messagebox.showinfo("Information", "Encryption canceled.")
            else:
                messagebox.showerror("Error", "The selected PDF file is already encrypted.")
    else:
        messagebox.showerror("Error", "Please select a file and enter a password.")

def decrypt_pdf():
    file_path = fileentry.get()
    password = passwordentry.get()

    if file_path and password:
        with open(file_path, "rb") as file:
            pdf = PyPDF2.PdfReader(file)
            if pdf.is_encrypted:
                if pdf.decrypt(password):
                    output_pdf = PyPDF2.PdfFileWriter()
                    for page in pdf.pages:
                        output_pdf.add_page(page)

                    output_filepath = filedialog.asksaveasfilename(defaultextension=".pdf")
                    if output_filepath:
                        with open(output_filepath, "wb") as output_file:
                            output_pdf.write(output_file)

                        fileentry.delete(0, END)
                        passwordentry.delete(0, END)

                        messagebox.showinfo("Decryption Complete", "PDF file decrypted successfully!")
                    else:
                        messagebox.showinfo("Information", "Decryption canceled.")
                else:
                    messagebox.showerror("Error", "Invalid password. Please enter the correct password.")
            else:
                messagebox.showerror("Error", "The selected PDF file is not encrypted.")
    else:
        messagebox.showerror("Error", "Please select a file and enter a password.")

root = Tk()
root.title('FileX :- PDF Encrypter and Decrypter')
root.geometry("600x200")

filelabel = Label(root, text="Select PDF File")
filelabel.pack()

fileentry = Entry(root, width=50)
fileentry.pack()

browsebutton = Button(root, text="Browse", command=select_file)
browsebutton.pack()

passwordlabel = Label(root, text="Enter Password")
passwordlabel.pack()

passwordentry = Entry(root, width=50, show="*")
passwordentry.pack()

encryptbutton = Button(root, text="Encrypt", command=encrypt_pdf)
encryptbutton.pack()

decryptbutton = Button(root, text="Decrypt", command=decrypt_pdf)
decryptbutton.pack()

root.mainloop()
