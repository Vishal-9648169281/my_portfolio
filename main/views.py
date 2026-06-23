from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile, Skill, Project, Experience, Education, Contact


def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    educations = Education.objects.all()

    skill_categories = {
        'frontend': skills.filter(category='frontend'),
        'backend': skills.filter(category='backend'),
        'database': skills.filter(category='database'),
        'tools': skills.filter(category='tools'),
    }

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if name and email and subject and message:
            Contact.objects.create(name=name, email=email, subject=subject, message=message)
            messages.success(request, 'Message sent successfully! I will get back to you soon.')
        else:
            messages.error(request, 'Please fill all fields.')
        return redirect('home')

    context = {
        'profile': profile,
        'skills': skills,
        'skill_categories': skill_categories,
        'projects': projects,
        'experiences': experiences,
        'educations': educations,
    }
    return render(request, 'main/index.html', context)
