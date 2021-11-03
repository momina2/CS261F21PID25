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
#Functions For Contains with contains 
def filter(FirstFilter,SecondText,Combo1,Combo2,Combo3,Combo4):
    # print(FirstFilter,SecondText,Combo1,Combo2,Combo3,Combo4)
    x=0
    if Combo1=="Contains" and Combo2 == "Add" and Combo3 == "Starts With":
        for i in range(0, len(SongsList.Namelist)):
            if(SongsList.Namelist[i].__contains__(FirstFilter) and SongsList.Namelist[i][x].__contains__(SecondText) ):
                print(SongsList.Namelist[i])
                Algorithm.indexArray.append(i) #storing index of values that in filtered
            addFilteredList()

#AND Filter with contains
def andFilter(FirstFilter,SecondText,Combo1,Combo2,Combo3,Combo4):
    if Combo1 =="Contains" and Combo2 == "Add" and Combo3 == "Contains":
        for i in range(0, len(SongsList.Namelist)):
            if (SongsList.Namelist[i].__contains__(FirstFilter) and SongsList.Namelist[i].__contains__(SecondText)):
                print(SongsList.Namelist[i])
                Algorithm.indexArray.append(i) 
        addFilteredList()

#OR Filter with conatins    
def orFilter(FirstFilter,SecondText,Combo1,Combo2,Combo3,Combo4):
    if Combo1 =="Contains" and Combo2 == "Or" and Combo3 == "Contains":
        for i in range(0, len(SongsList.Namelist)):
            if (SongsList.Namelist[i].__contains__(FirstFilter) or SongsList.Namelist[i].__contains__(SecondText)):
                print(SongsList.Namelist[i])
                Algorithm.indexArray.append(i) 
        addFilteredList()

#FUNCTIONS WITH CONTAINS AND/OR EQUALS TO
def contains_or_EqualTo(FirstFilter,SecondText,Combo1,Combo2,Combo3,Combo4):
    x=0
    if Combo1 =="Contains" and Combo2 == "Or" and Combo3 == "is Equal to":
        for i in range(0, len(SongsList.Namelist)):
            if (SongsList.Namelist[i].__contains__(FirstFilter) or SongsList.Namelist[i] == SecondText):
                print(SongsList.Namelist[i])
                Algorithm.indexArray.append(i) 
        addFilteredList()
        
def contains_and_EqualTo(FirstFilter,SecondText,Combo1,Combo2,Combo3,Combo4):
    x=0
    if Combo1 =="Contains" and Combo2 == "Add" and Combo3 == "is Equal to":
        for i in range(0, len(SongsList.Namelist)):
            if (SongsList.Namelist[i].__contains__(FirstFilter) and SongsList.Namelist[i] == SecondText):
                print(SongsList.Namelist[i])
                Algorithm.indexArray.append(i) 
        addFilteredList()

#FUNCTIONS WITH CONTAINS AND/OR EQUALS TO
def contains_or_notEqual(FirstFilter,SecondText,Combo1,Combo2,Combo3,Combo4):
    x=0
    if Combo1 =="Contains" and Combo2 == "Add" and Combo3 == "is not Equal to":
        for i in range(0, len(SongsList.Namelist)):
            if (SongsList.Namelist[i].__contains__(FirstFilter) and SongsList.Namelist[i] != SecondText):
                print(SongsList.Namelist[i])
                Algorithm.indexArray.append(i) 
        addFilteredList()

def contains_and_notEqual(FirstFilter,SecondText,Combo1,Combo2,Combo3,Combo4):
    x=0
    if Combo1 =="Contains" and Combo2 == "Or" and Combo3 == "is not Equal to":
        for i in range(0, len(SongsList.Namelist)):
            if (SongsList.Namelist[i].__contains__(FirstFilter) or SongsList.Namelist[i] != SecondText):
                print(SongsList.Namelist[i])
                Algorithm.indexArray.append(i) 
        addFilteredList()

#FUNCTIONS WITH CONTAINS AND/OR Does not Contains
def contains_or_notEqual(FirstFilter,SecondText,Combo1,Combo2,Combo3,Combo4):
    x=0
    if Combo1 =="Contains" and Combo2 == "Add" and Combo3 == "Does not Contains":
        for i in range(0, len(SongsList.Namelist)):
            if (SongsList.Namelist[i].__contains__(FirstFilter) and SongsList.Namelist[i].__contains__(SecondText)):
                print(SongsList.Namelist[i])
                Algorithm.indexArray.append(i) 
        addFilteredList()

def contains_and_notEqual(FirstFilter,SecondText,Combo1,Combo2,Combo3,Combo4):
    x=0
    if Combo1 =="Contains" and Combo2 == "Or" and Combo3 == "Does not Contains":
        for i in range(0, len(SongsList.Namelist)):
            if (SongsList.Namelist[i].__contains__(FirstFilter) or SongsList.Namelist[i] != SecondText):
                print(SongsList.Namelist[i])
                Algorithm.indexArray.append(i) 
        addFilteredList()
    
#FUNCTIONS WITH NOT EQUAL TO AND/OR IS EQUAL TO
def equal_and_notEqual(FirstFilter,SecondText,Combo1,Combo2,Combo3,Combo4):
    x=0
    if Combo1 !="is not Equal to" and Combo2 == "Add" and Combo3 == "is Equal to":
        for i in range(0, len(SongsList.Namelist)):
            if (SongsList.Namelist[i] == FirstFilter and SongsList.Namelist[i] != SecondText):
                print(SongsList.Namelist[i])
                Algorithm.indexArray.append(i) 
        addFilteredList()
 
def equal_or_notEqual(FirstFilter,SecondText,Combo1,Combo2,Combo3,Combo4):
    x=0
    if Combo1 =="is not Equal to" and Combo2 == "Or" and Combo3 == "is Equal to":
        for i in range(0, len(SongsList.Namelist)):
            if (SongsList.Namelist[i]!= FirstFilter or SongsList.Namelist[i] == SecondText):
                print(SongsList.Namelist[i])
                Algorithm.indexArray.append(i) 
        addFilteredList()        

#FUNCTIONS WITH NOT EQUAL TO AND/OR NOT EQUAL TO
def notEqual_and_notEqual(FirstFilter,SecondText,Combo1,Combo2,Combo3,Combo4):
    x=0
    if Combo1 =="is not Equal to" and Combo2 == "Add" and Combo3 == "is not Equal to":
        for i in range(0, len(SongsList.Namelist)):
            if (SongsList.Namelist[i] != FirstFilter and SongsList.Namelist[i] != SecondText):
                print(SongsList.Namelist[i])
                Algorithm.indexArray.append(i) 
        addFilteredList()

def notEqual_and_notEqual(FirstFilter,SecondText,Combo1,Combo2,Combo3,Combo4):
    x=0
    if Combo1 =="is not Equal to" and Combo2 == "Or" and Combo3 == "is not Equal to":
        for i in range(0, len(SongsList.Namelist)):
            if (SongsList.Namelist[i] != FirstFilter or SongsList.Namelist[i] != SecondText):
                print(SongsList.Namelist[i])
                Algorithm.indexArray.append(i) 
        addFilteredList()
        

#FUNCTION FOR NOT EQUAL TO AND/OR CONTAINS
def notEqual_or_Contains(FirstFilter,SecondText,Combo1,Combo2,Combo3,Combo4):
    x=0
    if Combo1 =="is not Equal to" and Combo2 == "Or" and Combo3 == "Contains":
        for i in range(0, len(SongsList.Namelist)):
            if (SongsList.Namelist[i] != FirstFilter or SongsList.Namelist[i].__contains__(SecondText)):
                print(SongsList.Namelist[i])
                Algorithm.indexArray.append(i) 
        addFilteredList()

def notEqual_and_Contains(FirstFilter,SecondText,Combo1,Combo2,Combo3,Combo4):
    x=0
    if Combo1 =="is not Equal to" and Combo2 == "Add" and Combo3 == "Contains":
        for i in range(0, len(SongsList.Namelist)):
            if (SongsList.Namelist[i] != FirstFilter and SongsList.Namelist[i].__contains__(SecondText)):
                print(SongsList.Namelist[i])
                Algorithm.indexArray.append(i) 
        addFilteredList()
        
#FUNCTION FOR NOT EQUAL AND/OR STARTS WITH
def notEqual_or_startswith(FirstFilter,SecondText,Combo1,Combo2,Combo3,Combo4):
    x=0
    if Combo1 =="is not Equal to" and Combo2 == "Add" and Combo3 == "Starts With":
        for i in range(0, len(SongsList.Namelist)):
            if (SongsList.Namelist[i] != FirstFilter and SongsList.Namelist[i][x].__contains__(SecondText)):
                print(SongsList.Namelist[i])
                Algorithm.indexArray.append(i) 
        addFilteredList()
    
def notEqual_and_startswith(FirstFilter,SecondText,Combo1,Combo2,Combo3,Combo4):
    x=0
    if Combo1 =="is not Equal to" and Combo2 == "Or" and Combo3 == "Contains":
        for i in range(0, len(SongsList.Namelist)):
            if (SongsList.Namelist[i] != FirstFilter or SongsList.Namelist[i][x].__contains__(SecondText)):
                print(SongsList.Namelist[i])
                Algorithm.indexArray.append(i) 
        addFilteredList()
    
#FUNCTIONS FOR STARTS WITH AND/OR CONTAINS
def startswith_and_contains(FirstFilter,SecondText,Combo1,Combo2,Combo3,Combo4):
    x=0
    if Combo1 =="Starts With" and Combo2 == "Add" and Combo3 == "Starts With":
        for i in range(0, len(SongsList.Namelist)):
            if (SongsList.Namelist[i][x].__contains__(FirstFilter) and SongsList.Namelist[i].__contains__(SecondText)):
                print(SongsList.Namelist[i])
                Algorithm.indexArray.append(i) 
        addFilteredList()
    
def startswith_or_contains(FirstFilter,SecondText,Combo1,Combo2,Combo3,Combo4):
    x=0
    if Combo1 =="Starts With" and Combo2 == "Or" and Combo3 == "Contains":
        for i in range(0, len(SongsList.Namelist)):
            if (SongsList.Namelist[i][x].__contains__(FirstFilter) or SongsList.Namelist[i].__contains__(SecondText)):
                print(SongsList.Namelist[i])
                Algorithm.indexArray.append(i) 
        addFilteredList()

#FUNCTIONS FOR STARTS WITH AND/OR EQUAL TO
def StartsWith_OR_equal(FirstFilter,SecondText,Combo1,Combo2,Combo3,Combo4):
    x=0
    if Combo1 =="Starts With" and Combo2 == "Or" and Combo3 == "is Equal to":
        for i in range(0, len(SongsList.Namelist)):
            if (SongsList.Namelist[i][x].__contains__(FirstFilter) or SongsList.Namelist[i] == SecondText):
                print(SongsList.Namelist[i])
                Algorithm.indexArray.append(i) 
        addFilteredList()
        
def StartsWith_AND_equal(FirstFilter,SecondText,Combo1,Combo2,Combo3,Combo4):
    x=0
    if Combo1 =="Starts With" and Combo2 == "Add" and Combo3 == "is Equal to":
        for i in range(0, len(SongsList.Namelist)):
            if (SongsList.Namelist[i][x].__contains__(FirstFilter) and SongsList.Namelist[i] == SecondText):
                print(SongsList.Namelist[i])
                Algorithm.indexArray.append(i) 
        addFilteredList()
        
#FUNCTIONS FOR STARTS WITH AND/OR NOT EQUAL TO
def StartsWith_OR_NotEqual(FirstFilter,SecondText,Combo1,Combo2,Combo3,Combo4):
    x=0
    if Combo1 =="Starts With" and Combo2 == "Or" and Combo3 == "is not Equal to":
        for i in range(0, len(SongsList.Namelist)):
            if (SongsList.Namelist[i][x].__contains__(FirstFilter) or SongsList.Namelist[i] != SecondText):
                print(SongsList.Namelist[i])
                Algorithm.indexArray.append(i) 
        addFilteredList()
        
def StartsWith_AND_equal(FirstFilter,SecondText,Combo1,Combo2,Combo3,Combo4):
    x=0
    if Combo1 =="Starts With" and Combo2 == "Add" and Combo3 == "is not Equal to":
        for i in range(0, len(SongsList.Namelist)):
            if (SongsList.Namelist[i][x].__contains__(FirstFilter) and SongsList.Namelist[i] != SecondText):
                print(SongsList.Namelist[i])
                Algorithm.indexArray.append(i) 
        addFilteredList()
        
#FUNCTIONS FOR STARTS WITH AND/OR STARTS WITH
def StartsWith_OR_equal(FirstFilter,SecondText,Combo1,Combo2,Combo3,Combo4):
    x=0
    if Combo1 =="Starts With" and Combo2 == "Or" and Combo3 == "Starts With":
        for i in range(0, len(SongsList.Namelist)):
            if (SongsList.Namelist[i][x].__contains__(FirstFilter) or SongsList.Namelist[i][x].__contains__(SecondText)):
                print(SongsList.Namelist[i])
                Algorithm.indexArray.append(i) 
        addFilteredList()
        
def StartsWith_AND_equal(FirstFilter,SecondText,Combo1,Combo2,Combo3,Combo4):
    x=0
    if Combo1 =="Starts With" and Combo2 == "Add" and Combo3 == "Starts With":
        for i in range(0, len(SongsList.Namelist)):
            if (SongsList.Namelist[i][x].__contains__(FirstFilter) and SongsList.Namelist[i][x].__contains__(SecondText)):
                print(SongsList.Namelist[i])
                Algorithm.indexArray.append(i) 
        addFilteredList()
        

#FUNCTIONS WITH EQUAL TO AND/OR CONTAINS
def contains_or_notEqual(FirstFilter,SecondText,Combo1,Combo2,Combo3,Combo4):
    x=0
    if Combo1 =="Contains" and Combo2 == "Or" and Combo3 == "is not Equal to":
        for i in range(0, len(SongsList.Namelist)):
            if (SongsList.Namelist[i]== FirstFilter or SongsList.Namelist[i].__contains__(SecondText)):
                print(SongsList.Namelist[i])
                Algorithm.indexArray.append(i) 
        addFilteredList()

def contains_and_notEqual(FirstFilter,SecondText,Combo1,Combo2,Combo3,Combo4):
    x=0
    if Combo1 =="Contains" and Combo2 == "Add" and Combo3 == "is not Equal to":
        for i in range(0, len(SongsList.Namelist)):
            if (SongsList.Namelist[i]== FirstFilter and SongsList.Namelist[i].__contains__(SecondText)):
                print(SongsList.Namelist[i])
                Algorithm.indexArray.append(i) 
        addFilteredList()

#FUNCTIONS WITH EQUAL TO AND/OR NOT EQUAL
def equal_or_notEqual(FirstFilter,SecondText,Combo1,Combo2,Combo3,Combo4):
    x=0
    if Combo1 =="is Equal to" and Combo2 == "Or" and Combo3 == "is not Equal to":
        for i in range(0, len(SongsList.Namelist)):
            if (SongsList.Namelist[i]== FirstFilter or SongsList.Namelist[i] != SecondText):
                print(SongsList.Namelist[i])
                Algorithm.indexArray.append(i) 
        addFilteredList()

def equal_and_notEqual(FirstFilter,SecondText,Combo1,Combo2,Combo3,Combo4):
    x=0
    if Combo1 =="Contains" and Combo2 == "Add" and Combo3 == "is not Equal to":
        for i in range(0, len(SongsList.Namelist)):
            if (SongsList.Namelist[i]== FirstFilter and SongsList.Namelist[i]!=SecondText):
                print(SongsList.Namelist[i])
                Algorithm.indexArray.append(i) 
        addFilteredList()



#FUNCTIONS WITH EQUAL TO AND/OR STARTS WITH
def equal_or_notEqual(FirstFilter,SecondText,Combo1,Combo2,Combo3,Combo4):
    x=0
    if Combo1 =="is Equal to" and Combo2 == "Or" and Combo3 == "Starts With":
        for i in range(0, len(SongsList.Namelist)):
            if (SongsList.Namelist[i]== FirstFilter or SongsList.Namelist[i][x].__contains__(SecondText)):
                print(SongsList.Namelist[i])
                Algorithm.indexArray.append(i) 
        addFilteredList()

def equal_and_notEqual(FirstFilter,SecondText,Combo1,Combo2,Combo3,Combo4):
    x=0
    if Combo1 =="Contains" and Combo2 == "Add" and Combo3 == "is not Equal to":
        for i in range(0, len(SongsList.Namelist)):
            if (SongsList.Namelist[i]== FirstFilter and SongsList.Namelist[i][x].__contains__(SecondText)):
                print(SongsList.Namelist[i])
                Algorithm.indexArray.append(i) 
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
    
    

    
