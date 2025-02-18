import tkinter as tk
from tkinter import filedialog, messagebox
from tkinterdnd2 import TkinterDnD, DND_FILES
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
from PIL import Image

def merge_pdfs(pdf_list, output):
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output)
    merger.close()

def images_to_pdf(image_list, output):
    images = [Image.open(image).convert('RGB') for image in image_list]
    images[0].save(output, save_all=True, append_images=images[1:])

def compress_pdf(input_pdf, output_pdf):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    with open(output_pdf, 'wb') as f:
        writer.write(f)

class PDFManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ghost Document Manager")
        self.root.geometry("450x550")  

        self.pdf_list = []
        self.image_list = []
        self.selected_pdf = None

        
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        
        self.frame = tk.Frame(root, padx=20, pady=20)
        self.frame.grid(row=0, column=0, sticky="nsew")

        self.title_label = tk.Label(self.frame, text="Ghost Document Manager", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        self.merge_button = tk.Button(self.frame, text="Merge PDFs", command=self.select_merge)
        self.merge_button.pack(pady=10, fill=tk.X)

        self.images_to_pdf_button = tk.Button(self.frame, text="Convert Images to PDF", command=self.select_images_to_pdf)
        self.images_to_pdf_button.pack(pady=10, fill=tk.X)

        self.compress_button = tk.Button(self.frame, text="Compress PDF", command=self.select_compress)
        self.compress_button.pack(pady=10, fill=tk.X)

        self.add_file_button = tk.Button(self.frame, text="Add File", command=self.add_file, state=tk.DISABLED)
        self.add_file_button.pack(pady=10, fill=tk.X)

        self.process_button = tk.Button(self.frame, text="Process", command=self.process_files, state=tk.DISABLED)
        self.process_button.pack(pady=10, fill=tk.X)

        self.drop_label = tk.Label(self.frame, text="Select an action first", relief=tk.SOLID, pady=10)
        self.drop_label.pack(pady=20, fill=tk.BOTH)
        self.drop_label.drop_target_register(DND_FILES)
        self.drop_label.dnd_bind('<<Drop>>', self.drop_files)

        self.file_list_text = tk.Text(self.frame, height=12)  
        self.file_list_text.pack(pady=10, fill=tk.BOTH, expand=True)

       
        self.footer_frame = tk.Frame(root)
        self.footer_frame.grid(row=1, column=0, sticky="ew")

       
        self.footer_label = tk.Label(self.footer_frame, text="© 2025 Ghost Document Manager", font=("Helvetica", 10))
        self.footer_label.pack()

        self.selected_function = None

    def select_merge(self):
        self.selected_function = 'merge'
        self.drop_label.config(text="Drag and drop PDF files here to merge")
        self.enable_action_buttons()

    def select_images_to_pdf(self):
        self.selected_function = 'images_to_pdf'
        self.drop_label.config(text="Drag and drop image files here to convert to PDF")
        self.enable_action_buttons()

    def select_compress(self):
        self.selected_function = 'compress'
        self.drop_label.config(text="Drag and drop a PDF file here to compress")
        self.enable_action_buttons()

    def enable_action_buttons(self):
        self.add_file_button.config(state=tk.NORMAL)
        self.process_button.config(state=tk.NORMAL)

    def add_file(self):
        if self.selected_function == 'merge':
            file = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
            if file:
                self.pdf_list.append(file)
                self.update_file_list_text()
                messagebox.showinfo("File Added", f"Added {file}")

        elif self.selected_function == 'images_to_pdf':
            file = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png;*.bmp")])
            if file:
                self.image_list.append(file)
                self.update_file_list_text()
                messagebox.showinfo("File Added", f"Added {file}")

        elif self.selected_function == 'compress':
            file = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
            if file:
                self.selected_pdf = file
                self.update_file_list_text()
                messagebox.showinfo("File Added", f"Added {file}")

    def update_file_list_text(self):
        self.file_list_text.delete(1.0, tk.END)
        if self.selected_function == 'merge':
            for file in self.pdf_list:
                self.file_list_text.insert(tk.END, f"{file}\n")
        elif self.selected_function == 'images_to_pdf':
            for file in self.image_list:
                self.file_list_text.insert(tk.END, f"{file}\n")
        elif self.selected_function == 'compress' and self.selected_pdf:
            self.file_list_text.insert(tk.END, f"{self.selected_pdf}\n")

    def process_files(self):
        if self.selected_function == 'merge':
            if len(self.pdf_list) < 2:
                messagebox.showwarning("Warning", "Please add at least two PDF files to merge.")
                return
            output = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
            if output:
                merge_pdfs(self.pdf_list, output)
                messagebox.showinfo("Success", "PDFs merged successfully!")
                self.clear_files()

        elif self.selected_function == 'images_to_pdf':
            if len(self.image_list) == 0:
                messagebox.showwarning("Warning", "Please add at least one image file to convert to PDF.")
                return
            output = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
            if output:
                images_to_pdf(self.image_list, output)
                messagebox.showinfo("Success", "Images converted to PDF successfully!")
                self.clear_files()

        elif self.selected_function == 'compress':
            if not self.selected_pdf:
                messagebox.showwarning("Warning", "Please add a PDF file to compress.")
                return
            output = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
            if output:
                compress_pdf(self.selected_pdf, output)
                messagebox.showinfo("Success", "PDF compressed successfully!")
                self.clear_files()

    def drop_files(self, event):
        files = self.root.tk.splitlist(event.data)
        if self.selected_function == 'merge':
            pdf_list = [f for f in files if f.endswith('.pdf')]
            self.pdf_list.extend(pdf_list)
            self.update_file_list_text()
            messagebox.showinfo("Files Added", "PDF files added for merging")

        elif self.selected_function == 'images_to_pdf':
            image_list = [f for f in files if f.lower().endswith(('.jpg', '.png', '.bmp'))]
            self.image_list.extend(image_list)
            self.update_file_list_text()
            messagebox.showinfo("Files Added", "Image files added for conversion to PDF")

        elif self.selected_function == 'compress':
            pdf_file = [f for f in files if f.endswith('.pdf')]
            if len(pdf_file) != 1:
                messagebox.showwarning("Warning", "Please drag and drop exactly one PDF file to compress.")
                return
            self.selected_pdf = pdf_file[0]
            self.update_file_list_text()
            messagebox.showinfo("File Added", "PDF file added for compression")

    def clear_files(self):
        self.pdf_list = []
        self.image_list = []
        self.selected_pdf = None
        self.update_file_list_text()

if __name__ == "__main__":
    root = TkinterDnD.Tk()
    app = PDFManagerApp(root)
    root.mainloop()
