from PyPDF2 import PdfWriter

merger = PdfWriter
pdfs= []
n = int(input("How many pdfs?"))
for i in range(n):
    name = input(f"Enter file {i+1} name: ")
    pdfs.append(name)
for pdf in pdfs:
    merger.append(pdf)

merger.write(f"output.pdf")
merger.close()