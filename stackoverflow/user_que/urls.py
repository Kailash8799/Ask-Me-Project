from django.urls import path
from . import views

urlpatterns = [
    path('allque',views.showallque,name='all_que')
]
