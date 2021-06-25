from django.shortcuts import redirect, render
import random


def index(request):
    if "gold" not in request.session:
        request.session["gold"]=0
    context={
        "gold" : request.session["gold"],
    }
    return render(request, "index.html", context)


def process_money(request):
    ran_val = random.randint(0, 50)
    if request.method == "POST":
        request.session["gold"] = request.session["gold"] + ran_val
    return redirect("/")


def reset(request):
    if request.method == "GET":
        request.session["gold"]=0
    return redirect("/")