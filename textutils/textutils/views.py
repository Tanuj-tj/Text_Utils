# This file is created by me ""views.py"

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):

    # Get the text
    dj_text = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercounter = request.POST.get('charactercounter', 'off')
    analyzed = ""

    # Check which checkbox is om
    if removepunc == "on":
        punctuations = ''' !()-[]{};:'"\,<>./?@#$%^&*_~ '''
        analyzed = ""
        for char in dj_text:
            if char  not in punctuations:
                analyzed+=char
        params = {'purpose':'Remove Punctuations', 'analyzed_text':analyzed}
        dj_text = analyzed
        #return render(request,"analyze.html",params)

    if newlineremover == "on":
        analyzed = ""
        for char in dj_text:
            if char !="\n" and char !="\r":
                analyzed += char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        dj_text = analyzed
        #return render(request, "analyze.html", params)

    if extraspaceremover == "on":
        analyzed = ""
        for index,char in enumerate(dj_text):
            if not (dj_text[index] == " " and dj_text[index+1] == " "):
                analyzed += char

        params = {'purpose': 'Extra space remove', 'analyzed_text': analyzed}
        dj_text = analyzed
        #return render(request, "analyze.html", params)

    if charactercounter == "on":
        analyzed = 0
        for char in dj_text:
            analyzed += 1

        params = {'purpose': 'Count the no. of characters', 'analyzed_text': analyzed}
        dj_text = analyzed
        #return render(request, "analyze.html", params)

    if fullcaps=="on" :
        analyzed = ""
        for char in dj_text:
            analyzed += char.upper()
        params = {'purpose': 'Change to Uppercase', 'analyzed_text': analyzed}
        #return render(request, "analyze.html", params)


    if removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and charactercounter != "on" and fullcaps!="on":
        return HttpResponse("Error")

    return render(request, "analyze.html", params)

def aboutus(request):
    pass

def contactus(request):
    pass
