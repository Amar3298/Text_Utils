from ctypes import sizeof
from django.shortcuts import render,HttpResponse
def home(request):
    return render(request,"index.html")

def analyse(request):
    getTexta = request.POST.get("getT")
    # print(getTexta)
    checkRadio = request.POST.get("removepuc",'off')
    fullcaps = request.POST.get("fullcapsH",'off')
    lowercase = request.POST.get("lowercase",'off')
    newlineRemover = request.POST.get("newlineRemover",'off')
    extraSpaceh = request.POST.get("extraSpaceh",'off')
    countChar = request.POST.get("countChar",'off')
    # print(checkRadio)
    if(checkRadio!="off"):
        punct = ''' !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~ '''
        analysed = ""
        for char in getTexta:
            if char not in punct:
                analysed = analysed + char
        dic1 = {
            "Purpose":"Removal of Punctuation",
            "analyze":analysed
        }
        # return render(request,"analyze.html",dic1)
        getTexta = analysed
        
    if(fullcaps!="off"):
        analysed = ""
        for char in getTexta:
            analysed = analysed + char.upper()
        dic1 = {
        "Purpose":"Coverting to uppercase",
        "analyze":analysed
        }
        # return render(request,"analyze.html",dic1) 
        getTexta = analysed

    if(lowercase!="off"):
        analysed = ""
        for char in getTexta:
            analysed = analysed + char.lower()
        dic1 = {
        "Purpose":"Coverting to uppercase",
        "analyze":analysed
        }
        # return render(request,"analyze.html",dic1)
        getTexta = analysed 

    if(newlineRemover!="off"):
        analysed = ""
        for char in getTexta:
            if char!="\n" and char!="\r":
                analysed = analysed + char
        dic1 = {
        "Purpose":"Coverting to uppercase",
        "analyze":analysed
        }
        # return render(request,"analyze.html",dic1)
        getTexta = analysed 

    if(extraSpaceh!="off"):
        analysed = ""
        for index,char in enumerate(getTexta):
            if getTexta[index]==" " and  getTexta[index+1]==" ":
                pass
            else:
                analysed  = analysed + char
        dic1 = {
        "Purpose":"Coverting to uppercase",
        "analyze":analysed
        }
        # return render(request,"analyze.html",dic1)
        getTexta = analysed 
    if(countChar!="off"):
        analysed = len(getTexta)
        # print(analysed)
        dic1 = {
        "Purpose":"Coverting to uppercase",
        "analyze":analysed
        }
    
    if(checkRadio!="off" and fullcaps!="off" and lowercase!="off" and newlineRemover!="off" and extraSpaceh!="off" and countChar!="off"):
        return HttpResponse("Error")
    
    return render(request,"analyze.html",dic1) 

