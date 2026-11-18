from django.urls import path
from . import views

urlpatterns = [
    path('', views.HolomemListView.as_view(), name='home'),
    path('miembros/agregar/', views.HolomemCreateView.as_view(), name='agregar_miembro'),
    path('miembros/<int:pk>/', views.HolomemDetailView.as_view(), name='detalle_miembro'),
    path('miembros/<int:pk>/editar/', views.HolomemUpdateView.as_view(), name='editar_miembro'),
    path('miembros/<int:pk>/eliminar/', views.HolomemDeleteView.as_view(), name='eliminar_miembro'),
]