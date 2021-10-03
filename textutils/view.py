from django.http import HttpResponse
from django.shortcuts import render

def index(request):
   return  render(request,'index.html')


def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc =request.POST.get('removepunc','off')
    fullcaps =request.POST.get('fullcaps','off')
    newlineremove=request.POST.get('newlineremove','off')
    extraspaceremove=request.POST.get('extraspaceremove','off')
    charcount=request.POST.get('charcount','off')

    if removepunc=="on":
        punctuations='''!()-[]{}:;'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose' : 'Removed Puntuations','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)

    if fullcaps=="on":
        analyzed=""
        analyzed=djtext.upper()
        params = {'purpose': 'Change to Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)

    if newlineremove=="on":
        analyzed=""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed=analyzed+char
        params = {'purpose': 'Remove new line', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)

    if extraspaceremove=="on":
        analyzed=""
        for index,char in enumerate(djtext):
            if (not(djtext[index]==" " and djtext[index+1]==" ")):
               analyzed=analyzed+char
        params = {'purpose': 'Remove extra spaces', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if charcount=="on":
        count=0
        analyzed=djtext
        for char in djtext:
            if char !=" ":
               count=count+1
        params = {'purpose': 'Count the Character', 'analyzed_text': analyzed,'countchar':count}
        # return render(request, 'analyze.html', params)

    if (removepunc=="on"or fullcaps=="on"or  newlineremove=="on"or extraspaceremove=="on"or  charcount=="on"):
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Punctuation not solved :"+ djtext)



