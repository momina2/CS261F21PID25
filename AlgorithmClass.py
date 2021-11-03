from numpy import imag
from NextScreen import *
from Driver import *
class Algorithm():
    indexArray=[]
nList=[]
aList=[]
gList=[]
arList=[]
lList=[]
YList=[]
TPList=[]
DList=[]
CList=[]   

#filtering Funtion

def filter(FirstFilter,SecondText,Combo1,Combo2,Combo3,Combo4):
    # print(FirstFilter,SecondText,Combo1,Combo2,Combo3,Combo4)
    # if Combo1=="Contains":
    x=0
    for i in range(0, len(SongsList.Namelist)):
        if(SongsList.Namelist[i][x].__contains__('G')):
            print(SongsList.Namelist[i])
            Algorithm.indexArray.append(i) #storing index of values that in filtered
    addFilteredList()

#filtered data in to seperate list
def addFilteredList():
   
    for i in range(0, len(Algorithm.indexArray)):
        nList.append(SongsList.Namelist[Algorithm.indexArray[i]])
        aList.append(SongsList.albumlist[Algorithm.indexArray[i]])
        gList.append(SongsList.genrelist[Algorithm.indexArray[i]])
        arList.append(SongsList.artistslist[Algorithm.indexArray[i]])
        lList.append(SongsList.Likeslist[Algorithm.indexArray[i]])
        YList.append(SongsList.yearlist[Algorithm.indexArray[i]])
        TPList.append(SongsList.TimesPlayedlist[Algorithm.indexArray[i]])
        DList.append(SongsList.durationlist[Algorithm.indexArray[i]])
        CList.append(SongsList.Commentslist[Algorithm.indexArray[i]])
    listtodataframe()
#List to DataFrame
def listtodataframe():
    df = pd.DataFrame(list(zip(nList, aList, gList, arList, lList, YList, TPList, DList, CList)),
    columns =['name', 'album', 'genre', 'artists', 'Likes', 'year', 'TimesPlayed', 'duration','Comments'])
    print(df["album"])



if __name__ == "__main__":
    addToList()
    filter("a","a","a","a","a","a",)
    
    

    
