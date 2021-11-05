from PyQt5.QtWidgets import QTableWidget
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
   
    if Combo1=="Contains":
        ContainsFun(FirstFilter,0)
    if Combo1=="Starts With":
        startaWith(FirstFilter.upper(),0)
    if(Combo2=='Or'):
         if Combo3=="Contains":
          ContainsFun(SecondText,0)
         if Combo3=="Starts With": 
          startaWith(SecondText.upper(),0)
    else:
        if Combo3=="Contains":
          ContainsFun(SecondText,1)
        if Combo3=="Starts With": 
          startaWith(SecondText.upper(),1)
    
 

def startaWith(text,flag):
    x=0
    for i in range(0, len(SongsList.Namelist)):
        if(SongsList.Namelist[i][x].startswith(text) ):
            print(SongsList.Namelist[i])
            Algorithm.indexArray.append(i) #storing index of values that in filtered
    addFilteredList()
    # if(flag==1):
    #     Algorithm.indexArray=[]
    #     for i in range(0, len(nList)):
    #         if(Algorithm.nlist[i].startswith(text) ):
    #            print(Algorithm.nlist[i])
    #            Algorithm.indexArray.append(i)
    #     addFilteredList()

def ContainsFun(text,flag):
    
    for i in range(0, len(SongsList.Namelist)):
        if(SongsList.Namelist[i].__contains__(text) ):
            print(SongsList.Namelist[i])
            Algorithm.indexArray.append(i)
    addFilteredList()
    # if(flag==1):
    #     Algorithm.indexArray=[]
    #     for i in range(0, len(nList)):
    #         if(Algorithm.nlist[i].startswith(text) ):
    #            print(Algorithm.nlist[i])
    #            Algorithm.indexArray.append(i)
    #     addFilteredList()


      
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
    # print(df["album"])

def insertionSort(Array):
    for i in range(1,len(Array)):
        key=Array[i]
        j=i-1
        while j>=0 and key<Array[j]:
            Array[j+1]=Array[j]
            j=j-1
        Array[j+1]=key
    print(Array)
#Selection Sort
def SelectionSort(arr):
        for i in range(len(arr)):
            min = i
            for j in range(i+1, len(arr)):
                if arr[min] > arr[j]:
                    min = j   
            arr[i], arr[min] = arr[min], arr[i]
#bubble sort 
def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # sorting by using simultaneous assignment in python
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
#  Quicksort
def partition(arr,l,h): 
	i = ( l-1 )	
	pivot = arr[h]	 # pivot 

	for j in range(l , h):  
		if arr[j] <= pivot: 
			i = i+1
			arr[i],arr[j] = arr[j],arr[i] 

	arr[i+1],arr[h] = arr[h],arr[i+1] 
	return ( i+1 ) 

# Function to do Quick sort 
def quickSort(arr,l,h): 
	if l < h:  
		pi = partition(arr,l,h) 
		quickSort(arr, l, pi-1) 
		quickSort(arr, pi+1, h) 

#radix sort
def radixCountSort(array, size, col, base):

  output   = [0] * size
  count    = [0] * (base + 1) 
  basecount = ord('a') - 1 

  for item in array: 
    index = ord(item[col]) - basecount if col < len(item) else 0
    count[index] += 1

  for i in range(len(count)-1):  
      count[i + 1] += count[i]

  for item in reversed(array):
    index = ord(item[col]) - basecount if col < len(item) else 0
    output[count[index] - 1] = item
    count[index] -= 1

  return output

def RadixSort(array ):
  cols = None
  if not cols:
    cols = len(max(array, key = len)) 

  for col in range(cols-1, -1, -1): 
    array = radixCountSort(array, len(array), col, 26)

  return array 

#counting sort
def countSort(arr):
    # characters and initialize output array as 0
	output = [0 for i in range(len(arr))]
    # characters and initialize count array as 0
	count = [0 for i in range(256)]
	#Empty Sorted Array
	SortedArray = ["" for _ in arr]
    # Store count of each character
	for i in arr:
		count[ord(i)] += 1
	for i in range(256):
		count[i] += count[i-1]
	for i in range(len(arr)):
		output[count[ord(arr[i])]-1] = arr[i]
		count[ord(arr[i])] -= 1

	for i in range(len(arr)):
		SortedArray[i] = output[i]
	return SortedArray

#heap sort

def HeapInterval(arr, n, i):
	largest = i 
	l = 2 * i + 1	 
	r = 2 * i + 2	

	# greater than root
	if l < n and arr[i] < arr[l]:
		largest = l

	# greater than root
	if r < n and arr[largest] < arr[r]:
		largest = r

	# Change root
	if largest != i:
		arr[i],arr[largest] = arr[largest],arr[i] # swap
		HeapInterval(arr, n, largest)

def HeapSort(arr):
	n = len(arr)
    # Build a maxheap.
	for i in range(n // 2 - 1, -1, -1):
		HeapInterval(arr, n, i)

	# One by one extract elements
	for i in range(n-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i] # swap
		HeapInterval(arr, i, 0)

#shell sort

def shellSort(array, n):
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2


#implementing algorithms
def algorithms(Combo4, arr):
    low = 0
    high = len(arr)
    switcher = {
        0: "Merge Sort",
        1: insertionSort(arr),
        2: SelectionSort(arr),
        3: BubbleSort(arr),
        4: quickSort(arr, low, high),
        5: HeapSort(arr),
        6: countSort(arr),
        7: shellSort(arr),
        8: RadixSort(arr),
    }
    return switcher.get(Combo4, "nothing")


if __name__ == "__main__":
    addToList()
    # orFilter("a","a","a","a","a","a")
    filter("a","a","a","a","a","a")
    
    

    
