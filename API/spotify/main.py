import requests
import json

with open('auth.txt') as f:
    auth_key = f.read()

class Spotify():
    
    def __init__(self, user_id_in_spotify, word_for_search):
        self.user_id_in_spotify = user_id_in_spotify
        self.word_for_search = word_for_search

    def create_playlist_in_spotify(self):
        request_body = json.dumps({
            "name": "Top5 Musics",
            "description": "Essa playlist contém as 5 melhores músicas de um array de palavras chaves rodenado pelo uri",
            "public": True
        })

        endpoint_url = 'https://api.spotify.com/v1/users/{}/playlists'.format(self.user_id_in_spotify)

        response = requests.post(
            endpoint_url,
            data=request_body,
            headers={
                "Content-Type":"application/json",
                "Authorization":"Bearer {}".format(auth_key)
            }
        )

        response_json = response.json()
        id_playlist = response_json['id']
        
        return id_playlist

    def search_in_spotify(self, id_playlist):
        id_playlist = playlist_id
        busca_type =  'track'
        endpoint_url = 'https://api.spotify.com/v1/search?'
        songs = {
        
        }

        for value in self.word_for_search:
            limit = input('Quantas músicas quer adicionar? ')
            query = '{}q={}&type={}&limit={}'.format(endpoint_url, value, busca_type, limit)

            response = requests.get(query, headers={"Content-Type":"application/json",
                                                    "Authorization":"Bearer {}".format(auth_key)})
            response_json = response.json()

            for item in response_json['tracks']['items']:
                        songs.update({item['uri']: item['popularity']})
            
        obj1.add_song_to_playlist(playlist_id, songs)

    def add_song_to_playlist(self, playlist_id, songs):
        endpoint_url = "https://api.spotify.com/v1/playlists/{}/tracks?".format(playlist_id)
        query_stin = ""
        for uris in songs.keys():
            query_stin = uris + "," + query_stin
        query = '{}&uris={}'.format(endpoint_url, query_stin)
        response = requests.post(
            query,
            headers={
                "Content-Type":"application/json",
                "Authorization":"Bearer {}".format(auth_key)
            }
        )

if __name__ == "__main__":
    busca = ["Billie Elish", "MC Pozi", "Shawn Mendes"]

    obj1 = Spotify("luketsl", busca)

    playlist_id = obj1.create_playlist_in_spotify()
    obj1.search_in_spotify(playlist_id)
