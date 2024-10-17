#объединить pdf
import glob
from PyPDF2 import PdfMerger

pdf_files = glob.glob('p1//*.pdf') //папка с pdf файлами
merger = PdfMerger()
a=1
for pdf in pdf_files:
    merger.append(pdf)
    print(a)
    a+=1

merger.write('p1.pdf')
merger.close()




