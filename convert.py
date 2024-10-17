#конвертировать в pdf
import os
from docx2pdf import convert

# Путь к папке, где находятся файлы Word
path_to_folder = "1"

# Перебираем все файлы .docx в папке
for filename in os.listdir(path_to_folder):
    if filename.endswith('.docx'):
        # Конвертируем файл .docx в .pdf
        convert(os.path.join(path_to_folder, filename))
