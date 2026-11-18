from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .models import Generacion, Holomem
from .forms import HolomemForm

class HolomemListView(ListView):
    model = Holomem
    template_name = 'lista_holomems.html'
    context_object_name = 'holomems'

    def get_queryset(self):
        queryset = Holomem.objects.select_related('generacion').all()
        # Aquí puedes aplicar filtros adicionales si es necesario
        nombre = self.request.GET.get('nombre')
        if nombre:  
            queryset = queryset.filter(nombre=nombre)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['generaciones'] = Generacion.objects.all()
        context['total_holomems'] = self.get_queryset().count()
        context['activos'] = self.get_queryset().filter(activo=True)
        return context


class HolomemDetailView(DetailView):
    model = Holomem
    template_name = 'detalle_miembro.html'
    context_object_name = 'holo'


class HolomemCreateView(LoginRequiredMixin, CreateView):
    model = Holomem
    form_class = HolomemForm
    template_name = 'agregar_miembro.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        return super().form_valid(form)

class HolomemUpdateView(LoginRequiredMixin, UpdateView):
    model = Holomem
    form_class = HolomemForm
    template_name = 'editar_miembro.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        return super().form_valid(form)


class HolomemDeleteView(LoginRequiredMixin, DeleteView):
    model = Holomem
    template_name = 'eliminar_miembro.html'
    context_object_name = 'holo'
    success_url = reverse_lazy('home')


def base(request):
    return render(request, 'base.html')