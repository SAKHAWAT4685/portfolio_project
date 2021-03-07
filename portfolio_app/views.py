from django.shortcuts import render
# Create your views here.
from .models import *

def home(request, name):
    user = User.objects.get(username = name)
    social = Social.objects.get(user = user)
    activate='home'
    context={'activate': activate , 'social': social}
    return render(request,'home.html', context)

def about(request , name):
    user = User.objects.get(username = name)
    social = Social.objects.get(user = user)
    activate = 'about'
    about_me = AboutMe.objects.get(user = user)
    skills = Skill.objects.filter(user = user)
    context = {'about_me':about_me, 'skills':skills, 'activate': activate , 'social': social}
    return render (request, 'about.html', context)

def resume(request , name):
    user = User.objects.get(username = name)
    social=Social.objects.get(user = user)
    pro_exp= ProfessionalExperience.objects.filter(user = user)
    education = Education.objects.filter(user = user)
    summary = Summary.objects.get(user = user)
    about_me = AboutMe.objects.get(user = user)
    activate='resume'
    context={'activate': activate , 'social': social, 'pro_exp': pro_exp, 'education': education, 'summary' : summary , 'about_me': about_me}
    return render(request,'resume.html', context)

def service(request , name):
    user = User.objects.get(username = name)
    services = Service.objects.filter(user = user)
    social=Social.objects.get(user = user)
    activate='service'
    context={'activate': activate , 'social': social, 'services': services}
    return render(request,'service.html', context)

def portfolio(request , name):
    user = User.objects.get(username = name)
    project = Project.objects.filter(user = user)
    social=Social.objects.get(user = user)
    activate='portfolio'
    context={'activate': activate , 'social': social, 'project': project}
    return render(request,'portfolio.html', context)

def contact(request , name):
    user = User.objects.get(username = name)
    social=Social.objects.get(user = user)
    activate='contact'
    context={'activate': activate , 'social': social}
    return render(request,'contact.html', context)


def project_details(request ,id):
    project = Project.objects.get(id=id )
    context={'project': project}
    return render(request,'project_details.html', context)
