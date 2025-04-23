from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import ResumeForm, AchievementForm, ExperienceForm, EducationForm, ProjectForm, SkillForm
from .models import Resume, UserProfile

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('resume_view')
    else:
        form = AuthenticationForm()

    return render(request, 'resume/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'resume/register.html', {'form': form})

# @login_required
# def resume_view(request):
#     try:
#         resume = Resume.objects.get(user_profile__user=request.user)
#     except Resume.DoesNotExist:
#         resume = None

#     if request.method == 'POST':
#         form = ResumeForm(request.POST, request.FILES, instance=resume)
#         if form.is_valid():
#             resume = form.save(commit=False)
#             resume.user_profile = UserProfile.objects.get(user=request.user)
#             resume.save()
#             return redirect('resume_view')  # Redirect to a success page or the same form

#     else:
#         form = ResumeForm(instance=resume) if resume else ResumeForm()

#     return render(request, 'resume/resume.html', {'form': form})

# views.py
from django.shortcuts import render, redirect
from .forms import ResumeForm, AchievementForm, ExperienceForm, EducationForm, ProjectForm, SkillForm
from .models import Resume, Achievement, Experience, Education, Project, Skill
from django.contrib.auth.decorators import login_required

@login_required
def resume_view(request):
    # Get the user's profile
    user_profile = request.user.userprofile

    # Get or create the resume for the user
    resume, created = Resume.objects.get_or_create(user_profile=user_profile)

    if request.method == 'POST':
        resume_form = ResumeForm(request.POST, instance=resume)
        if resume_form.is_valid():
            resume_form.save()
            return redirect('resume_view')  # Redirect to the same page or another page
    else:
        resume_form = ResumeForm(instance=resume)

    # Handle achievements, experiences, education, projects, and skills
    achievements = AchievementForm(prefix='achievement')
    experiences = ExperienceForm(prefix='experience')
    educations = EducationForm(prefix='education')
    projects = ProjectForm(prefix='project')
    skills = SkillForm(prefix='skill')

    return render(request, 'resume/resume.html', {
        'resume_form': resume_form,
        'achievements': achievements,
        'experiences': experiences,
        'educations': educations,
        'projects': projects,
        'skills': skills,
    })

def logout_view(request):
    logout(request)
    return redirect('index')

from django.shortcuts import render

def index_view(request):
    return render(request, 'resume/index.html')  




    # trying ats
# import io
# import google.generativeai as genai
# from django.shortcuts import render
# from django.conf import settings
# from django.contrib.auth.decorators import login_required
# from PyPDF2 import PdfReader
# from .forms import ResumeUploadForm

import io
import google.generativeai as genai
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from PyPDF2 import PdfReader
from .forms import ResumeUploadForm
@login_required
def ats_score(request):
    generated_text = None
    ats_score = None
    matching_skills = []
    suggestions = ""

    if request.method == 'POST':
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            job_description = form.cleaned_data['job_description']
            resume_file = request.FILES['resume']

            try:
                # Read PDF content
                pdf = PdfReader(resume_file)
                resume_text = ""
                for page in pdf.pages:
                    resume_text += page.extract_text() or ""

                # Configure Gemini with your API key
                genai.configure(api_key=settings.GENERATIVE_API_KEY)

                # Load the model
                model = genai.GenerativeModel("gemini-1.5-flash")

                # Provide generation config during generate_content()
                generation_config = {
                    "temperature": 0.7,
                    "top_p": 1,
                    "top_k": 1,
                    "max_output_tokens": 2048,
                }

                # Prompt
                prompt = f"""
You are an expert in resume analysis and ATS (Applicant Tracking System) scoring.
Analyze the following resume in relation to the provided job description and provide:

1. ATS match score out of 100  
2. Matching skills and keywords (comma-separated)  
3. Suggestions for improvement  

Resume:
{resume_text}

Job Description:
{job_description}
"""

                # Generate content with generation config
                response = model.generate_content(prompt, generation_config=generation_config)
                generated_text = response.text

                # Split the generated text into components
                lines = generated_text.splitlines()
                if len(lines) >= 3:
                    ats_score = lines[0].strip()  # ATS match score
                    matching_skills = [skill.strip() for skill in lines[1].split(',')]  # Skills
                    suggestions = lines[2].strip()  # Suggestions

            except Exception as e:
                generated_text = f"Error during processing: {str(e)}"
    else:
        form = ResumeUploadForm()

    return render(request, 'resume/ats_score.html', {
        'form': form,
        'ats_score': ats_score,
        'matching_skills': matching_skills,
        'suggestions': suggestions,
        'generated_text': generated_text
    })
