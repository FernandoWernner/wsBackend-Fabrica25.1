from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CharacterViewSet, character_list, EpisodeViewSet

router = DefaultRouter()
router.register(r'Personagens', CharacterViewSet)
router.register(r'Episódios', EpisodeViewSet)

urlpatterns = [
    path('', include(router.urls)), 
    path('personagens/html/', character_list, name='character_list'),  
    path('api/', include(router.urls)),

]