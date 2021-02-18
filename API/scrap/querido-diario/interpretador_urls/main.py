import conn_db as db
import data_process as dp
import pdf_to_ocr as ocr

path_to_data_collection = '../Scraper/data_collection/data/'

bd_connection = db.Connection_db('../Scraper/data_collection/querido-diario.db')

returned_rows = bd_connection.select_all_links()

for row in returned_rows:
    try:
        row = row[0]
        tesseract = ocr.Ocr_data_image(path_to_data_collection + str(row))
        tesseract.create_image_from_pdf()
    except ValueError as e:
        print('O row ' + str(row) + ' não pode ser completo' + str(e))
    