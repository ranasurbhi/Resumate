from django.urls import path
from .views import index_view,resume_view, login_view, logout_view, register_view,ats_score
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index_view, name='index'),  # This will be your index page
    path('resume/', resume_view, name='resume_view'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('ats-score/', ats_score, name='ats_score'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)