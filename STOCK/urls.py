from django.urls import path
from .views import home  # Importez la vue que vous avez créée

urlpatterns = [
   path('', home, name='home'),  # La vue home sera accessible à la racine de l'application
]
   
