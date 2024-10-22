from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Usuario, InfoHorno, InfoProduccion
from .serializers import UserSerializer, InfoHornoSerializer, InfoProduccionSerializer

class UserListView(APIView):
    permission_classes = [permissions.IsAuthenticated]  # Requiere autenticación

    def get(self, request):
        users = Usuario.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data['password'])  # Hashea la contraseña
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class InfoHornoListView(APIView):
    # permission_classes = [permissions.IsAuthenticated]  # Solo usuarios autenticados
    permission_classes = [permissions.AllowAny]  # Permitir acceso a todos
  

    def get(self, request):
        # Verifica cuántos registros devuelve la consulta
        hornos = InfoHorno.objects.all()
        print(f"Registros encontrados: {hornos.count()}")  # Debugging
        
        # Serializa los datos
        serializer = InfoHornoSerializer(hornos, many=True)
        return Response(serializer.data)
    
class InfoProduccionListView(APIView):
    # permission_classes = [permissions.IsAuthenticated]  # Solo usuarios autenticados
    permission_classes = [permissions.AllowAny]  # Permitir acceso a todos
  

    def get(self, request):
        # Verifica cuántos registros devuelve la consulta
        hornos = InfoProduccion.objects.all()
        print(f"Registros encontrados: {hornos.count()}")  # Debugging
        
        # Serializa los datos
        serializer = InfoProduccionSerializer(hornos, many=True)
        return Response(serializer.data)
    

    