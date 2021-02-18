import conn_db as db
import data_process as dp
import pdf_to_ocr as ocr
import setup as st

path_to_data_collection = st.path_to_data_collection()

bd_connection = db.Connection_db(st.path_to_database())

returned_rows = bd_connection.select_all_links()

for row in returned_rows:
    try:
        row = row[0]
        dt_proc = dp.Pdf_data_reader(path_to_data_collection + str(row))
        dt_proc.request_pdf_content()
    except ValueError as e:
        print('O row ' + str(row) + ' não pode ser completo' + str(e))
        try:
            tesseract = ocr.Ocr_data_image(path_to_data_collection + str(row))
            tesseract.create_image_from_pdf()
        except ValueError as t:
            print('Tentativa com OCR falhou')

