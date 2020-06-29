from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'home.html')

def survey_page(request):
    return render(request, 'survey_page.html')

def new_survey(request):
    
    return redirect ('/survey_page')

def about(request):
    return render(request, 'about.html')

def interesting_finds(request):
    return render(request, 'interesting_finds.html')

def portfolio(request):
    return render(request, 'portfolio.html')

