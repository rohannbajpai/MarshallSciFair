from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import projects, event, schedule
from django.urls import reverse
import operator
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
        "judge": request.session["judge"],
        "schedule": schedule.objects.get(judge = request.session['judge'])
    })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            request.session["judge"] = request.POST['username']
            return render(request, "evaluator/home.html", {
            "projectid":  None,
            "projects": projects.objects.all(),
            "judge": request.session["judge"],
            "schedule": schedule.objects.get(judge = request.session['judge'])
        })

def search(request):
    return render(request, "evaluator/search.html", {
    "projectid":  None,
    "projects": projects.objects.all(),
    "judge": request.session["judge"] 
    })
  
def results(request):
    try:
        project = projects.objects.get(a_id = int(request.POST['projects']), judge = request.session["judge"])
        return render(request, "evaluator/search.html", {
            "project": project,
            "projectid":  project.a_id,
            "projects": projects.objects.all(),
            "judge": request.session["judge"],
            "message": ""
        })
    except:
        return render(request, "evaluator/search.html", {
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
def scores(request):
    #todo, page for Dr. T (possibly competitors) to see live results
    sorted_scores = projects.objects.order_by('a_id')
    #sorted_scores = sorted(unsorted_scores, key=operator.attrgetter('a_id')) 
    scores_iterator = sorted_scores.iterator()
    graded_projects = {}
    prevproject = None
    nums = 0
    while True:
        try:
            project = next(scores_iterator)
            if nums == 0:
                total_research_question = project.research_question
                total_dam = project.dam
                total_execution = project.execution
                total_creativity = project.creativity
                total_presentation = project.presentation
                nums = 1
                prevproject = project

            elif prevproject.a_id == project.a_id:
                prevproject = project
                total_research_question+=project.research_question
                total_dam+=project.dam
                total_execution+= project.execution
                total_creativity+= project.creativity
                total_presentation+= project.presentation
                nums += 1
            else:
                
                subscores = {}
                subscores["research_question"] = total_research_question/nums
                subscores["design_and_methodology"] = total_dam/nums
                subscores["execution"] = total_execution/nums
                subscores["creativity"] = total_creativity/nums
                subscores["presentation"] = total_presentation/nums
                graded_projects[prevproject.a_id] = subscores
                total_research_question = project.research_question
                total_dam = project.dam
                total_execution = project.execution
                total_creativity = project.creativity
                total_presentation = project.presentation
                prevproject = project
                nums = 1

        except StopIteration:
            subscores = {}
            subscores["research_question"] = total_research_question/nums
            subscores["design_and_methodology"] = total_dam/nums
            subscores["execution"] = total_execution/nums
            subscores["creativity"] = total_creativity/nums
            subscores["presentation"] = total_presentation/nums
            graded_projects[project.a_id] = subscores
            break

    return render(request, "evaluator/scores.html", {
        "projects": graded_projects,
        "sorted": sorted_scores


    })

def realhome(request):
    #todo: rename old home function to search, rename search to results, rename this function to home
    #todo: this function should display the schedule of the judge
    #todo: completed projects should be a different color than incomplete projects
    pass