from django.contrib import admin
from .models import UserProfile, Resume, Achievement, Experience, Education, Project, Skill

# Register your models here
admin.site.register(UserProfile)
admin.site.register(Resume)
admin.site.register(Achievement)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Project)
admin.site.register(Skill)