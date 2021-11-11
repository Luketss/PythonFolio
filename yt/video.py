import pytube
import os

def video():
    link = 'https://www.youtube.com/watch?v=Wg7EuMtk7FE&t=1015s&ab_channel=Rocketseat'
    video =  pytube.YouTube(link)
    source = video.streams.get_highest_resolution()
    print('\033[1;31m \n Fazendo o download...')
    destino = source.download(output_path='C:\\pjus\\vd')
    base, ext = os.path.splitext(destino)
    new_file = base + '.mp4'
    os.rename(destino, new_file)
    print('\033[1;33m \n Concluído!\n')