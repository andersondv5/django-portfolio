from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),  # Página inicial
    path('contato/', views.contato_view, name='contato'),
    path('contato/sucesso/', views.contato_sucesso, name='contato_sucesso'),
    path('projetos/', views.projetos_view, name='projetos'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]