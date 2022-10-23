import json
import requests
import html
from bs4 import BeautifulSoup


head =  {
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'
    }

def get_youtube_music_results(query):

    query = query.replace(' ','+')
    response = requests.get("https://music.youtube.com/search?q="+query, headers=head).text

    result = response.encode().decode("unicode-escape")
    result = html.unescape(result)

    soup = BeautifulSoup(result, 'html.parser').find(lambda tag:tag.name=="script" and "initialData" in tag.text).text
    script = soup.split(";")[2].removesuffix(')').removeprefix('initialData.push(').split("'")[5]
    yee = json.loads(script)['contents']['tabbedSearchResultsRenderer']['tabs'][0]
    yee2 = yee['tabRenderer']['content']['sectionListRenderer']['contents']
    
    for content in yee2:
        musicShelfRendererContents = content['musicShelfRenderer']['contents']
        for musicShelfRendererContent in musicShelfRendererContents:
            musicResponsiveListItemRenderer = musicShelfRendererContent['musicResponsiveListItemRenderer']
            try:
                print(musicResponsiveListItemRenderer['playlistItemData'])
                print(musicResponsiveListItemRenderer['playlistItemData']['videoId'])
            except:
                pass

result = get_youtube_music_results('ud gaye')