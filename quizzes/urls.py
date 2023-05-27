from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',quiz_create),
    path('active/',get_active_quiz),
    path('<int:quiz_id>/result/',get_result),
    path('all/',quiz_list),

    
]