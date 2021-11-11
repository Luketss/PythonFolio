import os
import pytube

# 'https://www.youtube.com/watch?v=Wg7EuMtk7FE&t=1015s&ab_channel=Rocketseat'

class YouTube:
    def __init__(self, url):
        self.url = url

class Download(YouTube):
    def __init__(self, url, choice):
        super().__init__(url)
        self.choice = choice

    def video(self):
        video =  pytube.YouTube(self.url)
        source = video.streams.get_highest_resolution()
        self.core(video, source)

    def audio(self):
        video =  pytube.YouTube(self.url)
        source = video.streams.filter(only_audio=True).first()
        self.core(video, source)
    
    def core(self, video, source):
        print(f'\033[1;41m [{video.title} -- {video.author}]\033[0;0m')
        print('\033[1;31m \n Fazendo o download, espere um pouco...')
        destino = source.download(output_path='C:\\pjus\\vd')
        base, ext = os.path.splitext(destino)
        if self.choice == 'a':
            new_file = f'{base}.mp3'
        else:
            new_file = f'{base}.mp4'
        os.rename(destino, new_file)
        print('\033[1;33m \n Concluído!\n')

if __name__ == '__main__':
    while True:
        os.system('cls')
        print('DOWNLOADS COM PYTUBE - Aúdio [a] | Vídeos [v]')
        choice = ' '
        while choice not in 'av':
            choice = input('\n> ')
        dw = Download('https://www.youtube.com/watch?v=XWngf_2mgWQ&t=1s&ab_channel=Rocketseat', choice)
        if choice == 'a':
            dw.audio()
        elif choice == 'v':
            dw.video()
        else:
            print('\nerro inesperado')

        repeat = input('\nDeseja fazer outro download? [s][n]> ')
        if repeat != 's':
            print('Programa finalizado')
            break