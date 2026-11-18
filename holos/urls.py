from django.urls import path
from . import views

urlpatterns = [
    path('', views.HolomemListView.as_view(), name='home'),
    path('miembros/<uuid:uuid>/', views.HolomemDetailView.as_view(), name='detalle_miembro'),
]