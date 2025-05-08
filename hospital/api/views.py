from rest_framework import generics
from .models import Paciente, Doctor, Especialidad, DoctorEspecialidad, Cita
from .serializers import *

class PacienteListCreate(generics.ListCreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class PacienteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class DoctorListCreate(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class EspecialidadListCreate(generics.ListCreateAPIView):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer

class EspecialidadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer

class DoctorEspecialidadListCreate(generics.ListCreateAPIView):
    queryset = DoctorEspecialidad.objects.all()
    serializer_class = DoctorEspecialidadSerializer

class DoctorEspecialidadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DoctorEspecialidad.objects.all()
    serializer_class = DoctorEspecialidadSerializer

class CitaListCreate(generics.ListCreateAPIView):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer

class CitaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer
