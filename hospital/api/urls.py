from django.urls import path
from . import views

urlpatterns = [
    path('pacientes/', views.PacienteListCreate.as_view()),
    path('pacientes/<int:pk>/', views.PacienteDetail.as_view()),
    path('doctores/', views.DoctorListCreate.as_view()),
    path('doctores/<int:pk>/', views.DoctorDetail.as_view()),
    path('especialidades/', views.EspecialidadListCreate.as_view()),
    path('especialidades/<int:pk>/', views.EspecialidadDetail.as_view()),
    path('doctor-especialidades/', views.DoctorEspecialidadListCreate.as_view()),
    path('doctor-especialidades/<int:pk>/', views.DoctorEspecialidadDetail.as_view()),
    path('citas/', views.CitaListCreate.as_view()),
    path('citas/<int:pk>/', views.CitaDetail.as_view()),
]

