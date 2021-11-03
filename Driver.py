import pandas as pd


class SongsList():
 
  def __init__(self, name, album, genre, artist, likes, timesPlayed, duration, comment, year):
       self.name = name
       self.album = album
       self.genre = genre
       self.artist = artist
       self.likes = likes
       self.timesPlayed = timesPlayed
       self.duration = duration
       self.comment = comment
       self.year = year
  Namelist =[]
  albumlist = []
  genrelist = []
  artistslist = []
  Likeslist = []
  TimesPlayedlist = []
  durationlist = []
  Commentslist = []
  yearlist = []
def addToList():
    df = pd.read_csv ('data.csv')
    df = df.rename(columns={'duration ': 'duration'})
    SongsList.Namelist = df["name"].tolist()
    SongsList.albumlist = df["album"].tolist()
    SongsList.genrelist = df["genre"].tolist()
    SongsList.artistslist = df["artists"].tolist()
    SongsList.Likeslist = df["Likes"].tolist()
    SongsList.TimesPlayedlist = df["TimesPlayed"].tolist()
    SongsList.durationlist = df["duration"].tolist()
    SongsList.Commentslist = df["Comments"].tolist()
    SongsList.yearlist = df["year"].tolist()
  
if __name__ == "__main__":
    songs=SongsList("", "", "", "", "", "", "", "", "")   
    addToList()
    # for j in range (len(songs.list)):
    #    print(songs.list[j].name)
    
   


