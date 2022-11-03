from flask import Flask, render_template, request
from time import time
from datetime import datetime
import random

#https://coderslegacy.com/python/heap-sort-algorithm/
#https://www.programiz.com/dsa/heap-sort
#https://www.geeksforgeeks.org/python-program-for-quicksort/
#https://www.programiz.com/dsa/quick-sort
#https://stackabuse.com/quicksort-in-python/


app = Flask(__name__)
app.secret_key = "asdgfjhsdgfjhsdgryaesjtrjyetrjyestrajyrtesyjrtdyjrtasdyrtjsejrtestrerty"
header_html = '<html> <head></head> <body> <h1> </h1> <br />'

def bblSort(array):
    start_time = datetime.now()
    for i in range(len(array)-1):
        exchange = False
        for j in range(len(array) - 1 -i):
            if array[j] > array[j+1]:
                exchange = True
                t = array[j]
                array[j]=array[j+1]
                array[j+1] = t
    end_time = datetime.now()
    qtime = end_time - start_time
    return array,qtime

def selectionSort(array):
    start_time = datetime.now()
    for i in range(len(array)-1):
        min = array[i]
        pos = i
        for j in range(i+1, len(array)):
            if array[j]<min:
                min = array[j]
                pos = j
        array[pos] = array[i]
        array[i]=min
    end_time = datetime.now()
    qtime = end_time - start_time
    return array,qtime
def insertionSort(array):
    start_time = datetime.now()
    for i in range(1,len(array)):
        val = array[i]
        j=i-1
        while j>=0 and val < array[j]:
            array[j+1] = array[j]
            j-=1
        array[j+1] = val
    end_time = datetime.now()
    qtime = end_time - start_time
    return array,qtime
def mergeSort(array):
    start_time = datetime.now()
    if len(array) > 1:
        m = len(array)//2 #dividing the array
        lb = array[:m]  #dividing the array element
        rb = array[m:]
        mergeSort(lb) #sorting the 1st half
        mergeSort(rb) #sorting the 2nd half
        i = j = k = 0
        while i < len(lb) and j < len(rb): #comparing both arrays
            if lb[i] < rb[j]:
                array[k] = lb[i]
                i +=1
            else :
                array[k] = rb[j]
                j +=1
            k +=1
        while i < len(lb):
            array[k] = lb[i]
            i +=1
            k +=1
        while j < len(rb):
            array[k] = rb[j]
            j +=1
            k +=1
    end_time = datetime.now()
    qtime = end_time - start_time
    return array, qtime

def heapfiy(array, n, i):
    leftNode = (2*i) + 1
    rightNode = (2*i) +2
    if(leftNode < n and array[leftNode]> array[i]):
        largeElement = leftNode
    else:
        largeElement = i
    if(rightNode < n and array[rightNode]>array[largeElement]):
        largeElement = rightNode
    if(largeElement !=i):
        array[i], array[largeElement] = array[largeElement], array[i]
        heapfiy(array, n, largeElement)
def buildHeap(array):
    start_time=datetime.now()
    for i in range (len(array), -1, -1):
        heapfiy(array, len(array), i)
    for i in range(len(array)-1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heapfiy(array, i, 0)
    end_time=datetime.now()
    qtime = end_time-start_time
    return array, qtime

def partition(array, low, high):
    p = array[high] #pivot
    i=low-1 #smaller element index
    
    for j in range(low, high):
        if array[j] <= p:
            i=i+1
            array[i], array[j]=array[j], array[i]
            
    array[i+1], array[high] = array[high], array[i+1]
    return(i+1)
def quickSort1(array, low, high):
    start_time=datetime.now()
    if len(array) == 1:
        return array
    if low<high:
        p1 = partition(array, low, high)
        quickSort1(array, low, p1-1)
        quickSort1(array, p1+1, high)
    end_time=datetime.now()
    qtime = end_time-start_time    
    return array, qtime

def quickSort2(L, ascending= True):
    quicksorthelp(L, 0, len(L), ascending)

def quicksorthelp(L, low, high, ascending = True):
    result = 0
    if low < high:
        pivot_location, result = Partition(L, low, high, ascending)
        result += quicksorthelp(L, low, pivot_location, ascending)
        result += quicksorthelp(L, pivot_location + 1, high, ascending)
    return result

def Partition(L, low, high, ascending = True):
    result = 0
    pivot, pidx = median_of_three(L, low, high)
    L[low], L[pidx] = L[pidx], L[low]
    i = low + 1
    for j in range(low+1, high, 1):
        result += 1
        if (ascending and L[j] < pivot) or (not ascending and L[j] > pivot):
            L[i], L[j] = L[j], L[i]
            i += 1
    L[low], L[i-1] = L[i-1], L[low]
    return i - 1, result

def median_of_three(L, low, high):
    mid = (low+high-1)//2
    a = L[low]
    b = L[mid]
    c = L[high-1]
    if a <= b <= c:
        return b, mid
    if c <= b <= a:
        return b, mid
    if a <= c <= b:
        return c, high-1
    if b <= c <= a:
        return c, high-1
    return a, low


@app.route('/', methods=['GET','POST'])
def index():
    data = None
    qtime = None
    if request.method == "POST":
        input1 = request.form['input1']
        input2 = request.form['input2']
        if input1 and input2:
            rand_number = lambda x:[random.randint(1,5000) for i in range(x)]
            array = rand_number(int(input2))
            if input1 == '1':
                data,qtime = bblSort(array)
            elif input1 == '2':
                data,qtime = selectionSort(array)
            elif input1 == '3':
                data,qtime = insertionSort(array)
            elif input1 == '4':
                data, qtime = mergeSort(array)
            elif input1 == '5':
                data, qtime = buildHeap(array)
            elif input1 == '6':
                data, qtime = quickSort1(array, 0, len(array)-1)
            elif input1 == '7':
                tmp = array
                tic = datetime.now()
                quickSort2(tmp)
                toc = datetime.now()
                data = tmp
                qtime = toc-tic
    return header_html+render_template("index.html",data=data,qtime=qtime)

if __name__ == '__main__':
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)