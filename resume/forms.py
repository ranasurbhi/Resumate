from django import forms
from .models import Resume, Achievement, Experience, Education, Project, Skill

# class ResumeForm(forms.ModelForm):
#     class Meta:
#         model = Resume
#         fields = [
#             'firstname', 'middlename', 'lastname', 'designation', 
#             'address', 'email', 'phoneno', 'summary'
#         ]
#         widgets = {
#             'firstname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
#             'middlename': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Middle Name'}),
#             'lastname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
#             'designation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Designation'}),
#             'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
#             'phoneno': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
#             'summary': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Summary', 'rows': 3}),
#         }

# class AchievementForm(forms.ModelForm):
#     class Meta:
#         model = Achievement
#         fields = ['title', 'description']
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Achievement Title'}),
#             'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
#         }

# class ExperienceForm(forms.ModelForm):
#     class Meta:
#         model = Experience
#         fields = ['title', 'organization', 'location', 'start_date', 'end_date', 'description']
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Job Title'}),
#             'organization': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Organization'}),
#             'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
#             'start_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Start Date', 'type': 'date'}),
#             'end_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'End Date', 'type': 'date'}),
#             'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
#         }

# class EducationForm(forms.ModelForm):
#     class Meta:
#         model = Education
#         fields = ['school', 'degree', 'city', 'start_date', 'graduation_date', 'description']
#         widgets = {
#             'school': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'School'}),
#             'degree': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Degree'}),
#             'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
#             'start_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Start Date', 'type': 'date'}),
#             'graduation_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Graduation Date', 'type': 'date'}),
#             'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
#         }

# class ProjectForm(forms.ModelForm):
#     class Meta:
#         model = Project
#         fields = ['title', 'link', 'description']
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project Title'}),
#             'link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Project Link'}),
#             'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
#         }

# class SkillForm(forms.ModelForm):
#     class Meta:
#         model = Skill
#         fields = ['name']
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Skill Name'}),
#         }

# ats
from django import forms

from django import forms

class ResumeUploadForm(forms.Form):
    resume = forms.FileField(label="Upload Your Resume (PDF)")
    job_description = forms.CharField(widget=forms.Textarea(attrs={'rows': 6}), label="Paste Job Description")


# forms.py
from django import forms
from .models import Resume, Achievement, Experience, Education, Project, Skill

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['firstname', 'middlename', 'lastname', 'designation', 'address', 'email', 'phoneno', 'summary']

class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = ['title', 'description']

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['title', 'organization', 'location', 'start_date', 'end_date', 'description']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['school', 'degree', 'city', 'start_date', 'graduation_date', 'description']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'link', 'description']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name']