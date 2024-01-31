from .models import Receta, RecetaFavorita
from .serializers import RecetaSerializer, RecetaFavoritaSerializer

from django.shortcuts import get_object_or_404

from rest_framework import viewsets, views, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class ListarPeliculasFavoritas(views.APIView):
    # Clase para listar las recetas favoritas
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        recetas_favoritas = RecetaFavorita.objects.filter(usuario=request.user)
        serializer = RecetaFavoritaSerializer(recetas_favoritas, many=True)
        return Response(serializer.data)


class MarcarRecetaFavorita(views.APIView):
    # Clase para gestionar el favoritos en las recetas
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        receta = get_object_or_404(Receta, id=self.request.data.get('id', 0))
        favorita, created = RecetaFavorita.objects.get_or_create(
            receta=receta,
            usuario=request.user
        )
        # Si se ha creado se le asigna favorita True
        content = {
            'id': receta.id,
            'favorita': True
        }
        # Si ya existe se pasa favorita a False
        if not created:
            favorita.delete()
            content['favorita'] = False
        return Response(content)


#class RecetaViewSet(viewsets.ModelViewSet):
 #   queryset = Receta.objects.all()
  #  serializer_class = RecetaSerializer

class RecetaViewSet(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre']
    ordering_fields = ['favoritos']
