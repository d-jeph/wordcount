from django.http import HttpResponse
from django.shortcuts import render
from operator import itemgetter

def home(request):
    return render(request,'home.html')

def count(request):
    text= request.GET['text']
    wordlist = text.split()
    worddict={}
    for word in wordlist:
        if word in worddict:
            #increase count
            worddict[word] += 1
        else:
            #add to dict
            worddict[word]=1
    sorteddict=sorted(worddict.items(), key = itemgetter(1), reverse = True)
    return render(request,'count.html',{'text':text,'textcount':len(wordlist),'sorteddict':sorteddict[:10]})


def about(request):
    return render(request,'about.html')
