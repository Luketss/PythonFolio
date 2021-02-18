#import magic
from tika import parser


class Pdf_data_reader:
    def __init__(self, gazzete_file_path):
        self.gazzete_file_path = gazzete_file_path

    def request_pdf_content(self):
        try:
            file_data = parser.from_file(self.gazzete_file_path)
            text = file_data['content']

            final_file = str(self.gazzete_file_path.replace('.pdf','.txt'))
            with open(final_file, 'w', encoding='utf-8') as f:
                f.write(str(text).replace('\n', ' '))
        except ValueError as e:
            print('path returned in BD has no folder in DATA FOLDER')

    def get_row(self):
        return self.gazzete_file_path

    
