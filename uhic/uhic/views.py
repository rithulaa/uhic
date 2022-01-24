from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def login(request):
    return render(request, "login.html")


def signup(request):
    return render(request, "signup.html")


def input1(request):
    return render(request, "input1.html")


def register(request):
    return render(request, "register.html")


def report(request):
    return render(request, "card.html")


def input2(request):
    return render(request, "input2.html")


def input3(request):
    return render(request, "input3.html")
