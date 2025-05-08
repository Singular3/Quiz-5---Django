from rest_framework import serializers
from .models import Paciente, Doctor, Especialidad, DoctorEspecialidad, Cita

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = '__all__'

class DoctorEspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorEspecialidad
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    especialidades = EspecialidadSerializer(many=True, read_only=True)

    class Meta:
        model = Doctor
        fields = '__all__'

class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = '__all__'

    def validate(self, data):
        if data['fecha'] is None or data['hora'] is None:
            raise serializers.ValidationError("La fecha y hora son obligatorias.")
        return data
