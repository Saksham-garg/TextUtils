from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def removepunc(request):
    djtext = request.POST.get("text", "default")
    removepunc = request.POST.get("removepunc", 'off')
    newline = request.POST.get("newline", 'off')
    charcount = request.POST.get("charcount", 'off')
    analyzer = ""
    punctutaion = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    if (removepunc == 'on'):
        for char in djtext:
            if char not in punctutaion:
                analyzer = analyzer + char
        params = {"text": analyzer, "purpose": "Remove Punctutaion"}
        djtext = analyzer
    
    if (newline == "on"):
        analyzer = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzer = analyzer + char
        params = {"text": analyzer, "purpose": "Remove Punctutaion"}
        djtext = analyzer
    
    if (charcount == "on"):
        count = 0
        for char in djtext:
            if char not in punctutaion:
                count = count+1
        params = {"text": analyzer + ",Character Count :"+str(count), "purpose": "Remove Punctutaion"}
        djtext = analyzer
    
    if(charcount == "off" and newline == "off" and removepunc == "off"):
        return HttpResponse("Error")
    
    return render(request, "removepuc.html", params)
    