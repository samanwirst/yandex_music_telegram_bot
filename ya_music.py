from yandex_music import Client, track
from config import YANDEX_USER_TOKEN
class ya_music(): # Код из официальной документации, который был немного адаптирован для использования из класса
    global client
    client = Client(YANDEX_USER_TOKEN).init()

    type_to_name = {
    'track': 'трек',
    'artist': 'исполнитель',
    'album': 'альбом',
    'playlist': 'плейлист',
    'video': 'видео',
    'user': 'пользователь',
    'podcast': 'подкаст',
    'podcast_episode': 'эпизод подкаста',
    }

    def get_music_by_name(query):
        search_result = client.search(query)
        best_result_text = ''
        if search_result.best:
            type_ = search_result.best.type
            best = search_result.best.result
            if type_ in ['track', 'podcast_episode']:
                artists = ''
                if best.artists:
                    artists = ' - ' + ', '.join(artist.name for artist in best.artists)
                best_result_text = best.title + artists
            elif type_ == 'artist':
                best_result_text = best.name
            elif type_ in ['album', 'podcast']:
                best_result_text = best.title
            elif type_ == 'playlist':
                best_result_text = best.title
            elif type_ == 'video':
                best_result_text = f'{best.title} {best.text}'

            response = (f'Нашел: {best_result_text}\n')
            try:
                return [response, best.id, best.albums[0].id, best.title, artists.replace(' - ', '')]
            except:
                return False