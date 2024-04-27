from .serializers import EmpleadoSerializer
from .models import Empleados
from rest_framework import viewsets, permissions

class ApiViewSet(viewsets.ModelViewSet):
    queryset = Empleados.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EmpleadoSerializer