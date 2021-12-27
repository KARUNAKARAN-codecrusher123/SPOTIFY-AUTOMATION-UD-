import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import wikipedia
from datetime import datetime
from geopy.geocoders import Nominatim
import os
import psutil
import json
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import requests
import youtube_dl
from secrets import spotify_token, spotify_user_id






listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()





hi = 0

if hi == 0:
    talk('hello iam kkavi')
    print('hello iam kavi Voice assistant')
    talk('How are you buddy!!!')
    print('How are you buddy!!!')
    talk('doing good right?????')
    print('doing good right?????')
    talk('think so good')
    print('think so good')
    talk('what can i do for you buddy')
    print('what can i do for you buddy')
else:
    print('listening')


def take_command():
    try:
        with sr.Microphone() as source:
            talk('listening.....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'kavi' in command:
                command = command.replace('kavi', '')
                print(command)
    except:
        pass
    return command



def run_kavi():
    command = take_command()
    print(command)
    if 'play' in command:
        talk('playing')
        print('playing')
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'whatsapp' in command:
        pywhatkit.sendwhatmsg("+91 93611 40968", "hello iam kavi,my boss has told me to text any important info",
                              13, 58)
        print("Successfully Sent!")
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M:%S')
        print(time)
        talk('current time is' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        source = wikipedia.summary(person, 100)
        print(source)
        talk(source)
    elif 'search' in command:
        info = command.replace('search', '')
        general = wikipedia.search(info, 100)
        print(general)
        talk(general)
    elif 'history' in command:
        gen = command.replace('history, battle, movie review', '')
        small = wikipedia.summary(gen, 100)
        print(small)
        talk(small)
    elif 'date' in command:
        date = datetime.date.today()
        print(date)
        talk(date)
    elif 'health' in command:
        load1, load5, load15 = psutil.getloadavg()
        cpu_usage = (load15 / os.cpu_count()) * 100
        print("The CPU usage is : ", cpu_usage)
        talk(cpu_usage)
    elif 'memory size' in command:
        print('RAM memory % used:', psutil.virtual_memory()[2])
    elif 'location' in command:
        loc = Nominatim(user_agent="GetLoc")
        getloc = loc.geocode("Coimbatore")
        print(getloc.address)
        talk(getloc)
    elif 'movie review' in command:
        movie = command.replace('movie review', '')
        small = wikipedia.summary(movie, 10)
        print(small)
        talk(small)
    elif 'are you single' in command:
        talk('no......um.i am in relationship with wireless devices')
    elif 'do you like me' in command:
        talk('yes boss definitely')
    elif 'what is your name' in command:
        talk('My devloper karunakran has named me kkavi')
    elif 'cringe' in command:
        talk('alright........her name is janani,she was greatest,legend and gethu janani,foodie and more,her petname is cringe child')
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif 'spotify player' in command:
class CreatePlaylist:
            def __init__(self):
                self.youtube_client = self.get_youtube_client()
                self.all_song_info = {}
def get_youtube_client(self):
                os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

                api_service_name = "youtube"
                api_version = "v3"
                client_secrets_file = "client_secret.json"

                # Get credentials and create an API client
                scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
                flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
                    client_secrets_file, scopes)
                credentials = flow.run_console()

                youtube_client = googleapiclient.discovery.build(
                    api_service_name, api_version, credentials=credentials)

                return youtube_client
def get_liked_videos(self):
                request = self.youtube_client.videos().list(
                    part="snippet,contentDetails,statistics",
                    myRating="like"
                )
                response = request.execute()

                for item in response["items"]:
                    video_title = item["snippet"]["title"]
                    youtube_url = "https://www.youtube.com/watch?v={}".format(
                        item["id"])

                    video = youtube_dl.YoutubeDL({}).extract_info(
                        youtube_url, download=False)
                    song_name = video["track"]
                    artist = video["artist"]

                    if song_name is not None and artist is not None:
                        self.all_song_info[video_title] = {
                            "youtube_url": youtube_url,
                            "song_name": song_name,
                            "artist": artist,
                            "spotify_uri": self.get_spotify_uri(song_name, artist)

                        }
def create_playlist(self):
                """Create A New Playlist"""
                request_body = json.dumps({
                    "name": "Youtube Liked Vids",
                    "description": "All Liked Youtube Videos",
                    "public": True
                })

                query = "https://api.spotify.com/v1/users/{}/playlists".format(
                    spotify_user_id)
                response = requests.post(
                    query,
                    data=request_body,
                    headers={
                        "Content-Type": "application/json",
                        "Authorization": "Bearer {}".format(spotify_token)
                    }
                )
                response_json = response.json()

                return response_json["id"]

def get_spotify_uri(self, song_name, artist):

                query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20".format(
                    song_name,
                    artist
                )
                response = requests.get(
                    query,
                    headers={
                        "Content-Type": "application/json",
                        "Authorization": "Bearer {}".format(spotify_token)
                    }
                )
                response_json = response.json()
                songs = response_json["tracks"]["items"]

                uri = songs[0]["uri"]

                return uri

def add_song_to_playlist(self):
                self.get_liked_videos()

                uris = [info["spotify_uri"]
                        for song, info in self.all_song_info.items()]

                playlist_id = self.create_playlist()

                request_data = json.dumps(uris)

                query = "https://api.spotify.com/v1/playlists/{}/tracks".format(
                    playlist_id)

                response = requests.post(
                    query,
                    data=request_data,
                    headers={
                        "Content-Type": "application/json",
                        "Authorization": "Bearer {}".format(spotify_token)
                    }
                )

                if response.status_code != 200:
                    raise ResponseException(response.status_code)

                    response_json = response.json()
                    return response_json

                talk(Create playlist)

    else:
        talk('cant get it....please say it again')


while True:
    run_kavi()