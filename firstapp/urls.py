from . import views
from django.urls import path
# Create your views here.
urlpatterns = [
    path('check/', views.check),
]
