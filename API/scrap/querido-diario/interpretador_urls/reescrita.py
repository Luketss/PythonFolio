'''from setup import set_tesseract_path, set_poppler_dir
from pdf2image import convert_from_path

from PIL import Image
import pytesseract
import sys
import re
import os

pytesseract.pytesseract.tesseract_cmd = set_tesseract_path()

class Ocr_data_image:
    def __init__(self, file_path):
        self.file_path = file_path
        self.extension = './pdf/'

    def create_image_from_pdf(self)
        final_file = str(self.file_path.replace('.pdf','.txt'))
        pdf_pages_in_image = convert_from_path(self.file_path, 400, poppler_path= set_poppler_dir())
        
        limit_file_img = 1
        for page in pdf_pages_in_image:
            image_name = 'Page_' + str(limit_file_img) + '.jpg'
            page.save(self.extension + image_name, 'JPEG')
            limit_file_img += 1
        limit_file_img -= 1

        self.append_data_to_file(limit_file_img)

    def append_data_to_file(self, limit_file_img):
        with open(str(self.file_path.replace('.pdf','.txt')), 'a+') as fdata:
            for jpg in os.listdir(self.extension):
                if jpg.endswith('.jpg'):
                    filename = self.extension + jpg
                    #remover antes do commit
                    print(filename)
                    text_from_pdf = apply_tesseract_to_image(filename)
                    
                    self.remove_file_from_path(filename)

                    text_from_pdf = self.filter_text_file(text_from_pdf)

                    fdata.write(text_from_pdf)

    def apply_tesseract_to_image(self, filename):
        text_from_pdf = str((pytesseract.image_to_string(Image.open(filename))))
        text_from_pdf = text_from_pdf.replace('\n', ' ')
        
        return text_from_pdf
    
    def remove_file_from_path(self, filename):
        os.remove(filename)

    def filter_text_file(self, text_from_pdf):
        """
        Aplica dentro do texto recebido um regex para extração dos pontos chaves
        Args:
            text_from_pdf (str): texto retirado do PDF
        """

        result = ''
        pattern = re.compile('(.bjeto.*\w*\.*)')
        regex_result = pattern.findall(text_from_pdf)

        pattern = re.compile('(...e*culo.*\w*\.*)')

        for match in regex_result:
            result += str(match) + '\n'

        return(result)'''
'''
import re
from setup import set_tesseract_path, set_poppler_dir
from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import sys
import os

pytesseract.pytesseract.tesseract_cmd = set_tesseract_path()
extension = './pdf/'
def transform_OCR(pdf_path):
    out_file = str(pdf_path.replace('.pdf','')) + '.txt'
    pages = convert_from_path(pdf_path, 400, poppler_path= set_poppler_dir())

    filelimit = 1
    
    for page in pages:
        image_name = 'Page_' + str(filelimit) + '.jpg'
        page.save(extension + image_name, 'JPEG')
        filelimit += 1

    filelimit -= 1

    append_data_to_file(filelimit, out_file)

def append_data_to_file(filelimit, out_file):

    file_output = open(out_file, 'a+') 
    
    for jpg in os.listdir('./pdf'):
        if jpg.endswith('.jpg'):
            filename = extension+jpg
            print(filename)
            text_from_pdf = str((pytesseract.image_to_string(Image.open(filename))))
            text_from_pdf = text_from_pdf.replace('\n', ' ')
            remove_file_from_path(filename)
        
            text_from_pdf = filter_text_file(text_from_pdf)

            file_output.write(text_from_pdf)

    file_output.close()

def remove_file_from_path(filename):
    os.remove(filename)

def filter_text_file(text_from_pdf):
    """
    Aplica dentro do texto recebido um regex para extração dos pontos chaves
    Args:
        text_from_pdf (str): texto retirado do PDF
    """

    result = ''
    pattern = re.compile('(.bjeto.*\w*\.*)')
    regex_result = pattern.findall(text_from_pdf)

    pattern = re.compile('(...e*culo.*\w*\.*)')

    for match in regex_result:
        result += str(match) + '\n'

    return(result)

def parse_dataPdf_to_dict():
    pass
        

    

'''