def set_pdf_path():
    """
    Define o diretório de checagem para os arquivos PDF
    Returns:
        str: origem
    """
    pdf_repository = './pdfs'
    #pdf_repository = r'/mnt/c/Documents and Settings/Abla 01/Documents/Python/Scraper-Prefeituras-Licitacoes/leitura_pdf/pdfs'
    return pdf_repository

def set_tesseract_path():
    """
    Define o caminho para dependencia
    Returns:
        str: origem do tesseract.exe
    """
    path_tesseract = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    #'/mnt/c/Program Files/Tesseract-OCR/tesseract.exe'
    return path_tesseract

def set_poppler_dir():
    """
    Define o caminho para dependencia
    Returns:
        str: origem do poppler
    """
    poppler_dir = 'C:\\Program Files\\poppler-0.68.0\\bin'
    return poppler_dir

def path_to_database():
    """
    Define o caminho para busca dos paths dentro do banco de dados
    """
    db_connection = '../Scraper/data_collection/querido-diario.db'
    return db_connection

def path_to_data_collection():
    """
    Define o caminho para a pasta data (contém o resultado do querido diário)
    """
    path_to_data_collection = '../Scraper/data_collection/data/'
    return path_to_data_collection