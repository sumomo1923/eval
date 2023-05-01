from django.urls import path
from . import views

app_name = 'eval'

urlpatterns = [
    path('', views.home, name='home'),
    path('test_info/', views.test_info, name='test_info'),
    path('list/', views.student_list, name='student_list'),
    path('<int:item_id>/', views.audio_list, name='audio_list'),
    path('vote/', views.vote, name='vote'),
]