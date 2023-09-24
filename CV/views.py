from django.shortcuts import render
from django.views.generic import View
from .models import *
# Create your views here.

def profile(request):
    profile_data = ProfileModel.objects.all()
    hobbie_data = HobbiesModel.objects.all()
    philosophy = PhilosophyModel.objects.all()
    points = Points.objects.all()
    context={ 
        'profile_data': profile_data,
        'philosophy': philosophy,
        'points': points,
        'hobbie_data' : hobbie_data,
    }
    return render(request, "mainu/profile.html",context)

def education(request):
    edu=EducationModel.objects.all()
    for ed in edu:
        if ed.id == 1:
            ssc= ed
        elif ed.id == 2:
            hsc= ed
        else:
            bach = ed

    context={
            'bachelor': bach,
            'hsc': hsc,
            'ssc': ssc,
    }
    return render(request, "mainu/education.html",context)

def skills(request):
    prog_lang=ProgramingLanguage.objects.all()
    framework=FrameworksModel.objects.all()
    scr_lng=ScriptingLanguages.objects.all()
    dbtech=DatabaseTechnologies.objects.all()
    softskills=SoftSkills.objects.all()
    context={
        'prog_lang':prog_lang,
        'framework':framework,
        'scr_lng':scr_lng,
        'dbtech':dbtech,
        'softskills':softskills,
    }        
    return render(request, "mainu/skills.html",context)

def experience(request):
    experience = WorkExperience.objects.all()
    duration = WorkDuration.objects.all()
    for d in duration:
        if d.id == 1:
            dura1=d
        else:
            dura2=d

    for ex in experience:
        if ex.id == 1:
            exp1=ex
        else:
            exp2=ex

    context={
        'exp1':exp1,
        'dura1':dura1,
        'exp2':exp2,
        'dura2':dura2,
    }
    return render(request, "mainu/experience.html", context)
    

def project(request):
    project = ProjctsModel.objects.all()
    for proj in project:
        if proj.id ==1:
            project1 = proj
        if proj.id == 2:
            project2 = proj
    
    context={
        'project1':project1,
        'project2':project2,
    }
    return render(request, "mainu/project.html",context)

def accomplishment(request):
    accomplish = AccomplishmentModel.objects.all()
    context={'accomplish':accomplish}
    return render(request, "mainu/accomplishment.html",context)
