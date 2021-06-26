from django.shortcuts import redirect, render
import random
from random import randint
from time import strftime, localtime
import locale
locale.setlocale(locale.LC_ALL, 'es-ES')

def index(request):
    if "gold" not in request.session:
        request.session["gold"]=0
    context={
        "gold" : request.session["gold"],
    }
    return render(request, "index.html", context)


def reset(request):
    if request.method == "GET":
        request.session["gold"]=0
    return redirect("/")


def process_money(request):
    if request.method == "POST":
        if "activities" not in request.session:
            request.session["activities"]=[]
        time= strftime("%d de %B de %Y %H:%M:%S %p", localtime())
        lugar=request.POST["button"]
        if lugar == "farm":
            earnings = random.randint(10, 20)
            request.session["gold"] = request.session["gold"] + earnings
            result = (f"Earned {earnings} golds from {lugar}! {time}" )
            request.session["activities"].append(result)
            print(result)
        elif lugar == "cave":
            earnings = random.randint(5, 10)
            request.session["gold"] = request.session["gold"] + earnings
            result = (f"Earned {earnings} golds from {lugar}! {time}" )
            print(result)
        elif lugar == "house":
            earnings = random.randint(2, 5)
            request.session["gold"] = request.session["gold"] + earnings
            result = (f"Earned {earnings} golds from {lugar}! {time}" )
            print(result)
        elif lugar == "casino":
            earnings = random.randint(-50, 50)
            request.session["gold"] = request.session["gold"] + earnings
            result = (f"Earned {earnings} golds from {lugar}! {time}" )
            print(result)
    context={
        "gold" : request.session["gold"],
        "result" : request.session["activities"],
    }
    return render(request, "index.html", context)