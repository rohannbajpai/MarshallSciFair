from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import projects
from django.urls import reverse
# Create your views here.
def signin(request):
    return render(request, "evaluator/login.html", {
        "logout":False
        
    })
def home(request):
    if "judge" in request.session: 
        return render(request, "evaluator/home.html", {
        "projectid":  None,
        "projects": projects.objects.all(),
        "judge": request.session["judge"] 
    })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            request.session["judge"] = request.POST['username']
            return render(request, "evaluator/home.html", {
            "projectid":  None,
            "projects": projects.objects.all(),
            "judge": request.session["judge"] 
        })
def search(request):
    try:
        project = projects.objects.get(a_id = int(request.POST['projects']), judge = request.session["judge"])
        return render(request, "evaluator/home.html", {
            "project": project,
            "projectid":  project.a_id,
            "projects": projects.objects.all(),
            "judge": request.session["judge"],
            "message": ""
        })
    except:
        return render(request, "evaluator/home.html", {
            "project": None,
            "projectid": None,
            "projects": projects.objects.all(),
            "judge": request.session["judge"],
            "message": "No projects found. Try again."
        })
def save_points(request): 
    judge = request.session["judge"] 
    project = projects.objects.get(a_id = int(request.POST['projID']), judge = judge)
    project.research_question = int(request.POST['researchQuestion'])
    project.dam = int(request.POST['DAM'])
    project.execution = int(request.POST['execution'])
    project.creativity = int(request.POST['creativity'])
    project.presentation = int(request.POST['presentation'])
    project.judge = judge
    project.save()
    return render(request, "evaluator/confirm.html", {
            "project": project,
            "projectid":  project.a_id,
            "projects": projects.objects.all(),
            "judge": request.session["judge"] 
    })
def signout(request):
    logout(request)
    return render(request, "evaluator/login.html", {
        "logout": True
    })
def results(request):
    #todo, page for Dr. T (possibly competitors) to see live results
    pass
def realhome(request):
    #todo: rename old home function to search, rename search to results, rename this function to home
    #todo: this function should display the schedule of the judge
    #todo: completed projects should be a different color than incomplete projects
    pass