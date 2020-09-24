class Spotifi():

  auth = "API_URL_KEY"

  def __init__(self, user_id, busca1, busca2):
    self.user_id = user_id
    self.busca1 = busca1
    self.busca2 = busca2


  def get_spotify_playlist(self):
    limit = 10
    offset = 5

    endpoint_url = 'https://api.spotify.com/v1/users/{}/playlists?'.format(self.user_id)

    query = '{}limit={}&offset={}'.format(endpoint_url, limit, offset)

    response = requests.get(query, headers={"Content-Type":"application/json",
                                            "Authorization":"Bearer {}".format(Spotifi.auth)})

    #print(response.json())

  def search_in_spotify(self):
    primeira_palavra = self.busca1
    segunda_palavra = self.busca2
    limit = 5
    songs = {
        
    }
    busca_type = "track"
    endpoint_url = 'https://api.spotify.com/v1/search?'

    query = '{}q={}%20{}&type={}&limit={}'.format(endpoint_url, primeira_palavra, segunda_palavra, busca_type, limit)

    response = requests.get(query, headers={"Content-Type":"application/json",
                                            "Authorization":"Bearer {}".format(Spotifi.auth)})
    response_json = response.json()

    for item in response_json['tracks']['items']:
                songs.update({item['uri']: item['popularity']})

    return songs


  def create_playlist_in_spotify(self):
    request_body = json.dumps({
        "name": "CRIADO PELA API",
        "description": "PUTZ, DEU CERTO, TOMARA QUE Ñ BUGUE",
        "public": True
    })

    endpoint_url = 'https://api.spotify.com/v1/users/{}/playlists'.format(self.user_id)

    response = requests.post(
        endpoint_url,
        data=request_body,
        headers={
            "Content-Type":"application/json",
            "Authorization":"Bearer {}".format(Spotifi.auth)
        }
    )
    response_json = response.json()
    #print(response_json)
    #Id
    return response_json['id']

  def add_song_to_playlist(self, playlist_id, songs):

    
    endpoint_url = "https://api.spotify.com/v1/playlists/{}/tracks?".format(playlist_id)
    query_stin = ""
    for uris in songs.keys():
      query_stin = uris + "," + query_stin
      print(query_stin)
    query = '{}&uris={}'.format(endpoint_url, query_stin)
    response = requests.post(
        query,
        headers={
            "Content-Type":"application/json",
            "Authorization":"Bearer {}".format(Spotifi.auth)
        }
    )
    print(response)


if __name__ == "__main__":
  obj1 = Spotifi("luketsl", "MC", "POZI")
  # print(obj1.__dict__)
  # id_playlist = obj1.create_playlist_in_spotify()
  # print(id_playlist)
  musics = obj1.search_in_spotify()
  playlist_id = obj1.create_playlist_in_spotify()
  print(playlist_id)
  obj1.add_song_to_playlist(playlist_id, musics)
  print(musics)
