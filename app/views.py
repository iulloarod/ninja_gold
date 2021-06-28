from django.shortcuts import redirect, render
import random
from random import randint
from time import strftime, localtime
import locale
locale.setlocale(locale.LC_ALL, 'es-ES')

def index(request):
#creo una variable "gold" donde guardo el valor del oro obtenido en el proceso y le doy valor "0"´para comenzar. 
# Lo dejo en "context" para poder llamarlo en el index
    if "gold" not in request.session:
        request.session["gold"]=0
    if "activities" not in request.session:
        request.session["activities"]=[]
    context={
        "gold" : request.session["gold"],
        "activities" : request.session["activities"],
    }
    return render(request, "index.html", context)


def process_money(request):
    time= strftime("%d of %B of %Y %H:%M:%S %p", localtime())
    place=request.POST["button"]
    if place == "farm":
        earnings = random.randint(10, 20)
        request.session["gold"] = request.session["gold"] + earnings
        result = (f"Earned {earnings} gold from {place}! {time}" )
        request.session["activities"].append(result)
    elif place == "cave":
        earnings = random.randint(5, 10)
        request.session["gold"] = request.session["gold"] + earnings
        result = (f"Earned {earnings} gold from {place}! {time}" )
        request.session["activities"].append(result)
    elif place == "house":
        earnings = random.randint(2, 5)
        request.session["gold"] = request.session["gold"] + earnings
        result = (f"Earned {earnings} gold from {place}! {time}" )
        request.session["activities"].append(result)
    elif place == "casino":
        earnings = random.randint(-50, 50)
        request.session["gold"] = request.session["gold"] + earnings
        result = (f"Earned {earnings} gold from {place}! {time}" )
        request.session["activities"].append(result)
    return redirect("/")

def reset(request):
    if "gold" in request.session:
        del request.session["gold"]
    if "activities" in request.session:
        del request.session["activities"]
    return redirect("/")