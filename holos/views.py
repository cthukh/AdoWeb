from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Generacion, Holomem
from .forms import HolomemForm

class HolomemListView(ListView):
    model = Holomem
    template_name = 'lista_holomems.html'
    context_object_name = 'holomems'

    def get_queryset(self):
        queryset = Holomem.objects.select_related('generacion').all()
        # Aquí puedes aplicar filtros adicionales si es necesario
        name_gen = self.request.GET.get('nombre')
        if name_gen:
            queryset = queryset.filter(nombre=name_gen)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['holomiembros'] = Generacion.objects.all()
        context['total_vtubers'] = self.get_queryset().count()
        context['activos'] = [holo for holo in self.get_queryset() if holo.activo]
        return context


class HolomemDetailView(DetailView):
    model = Holomem
    template_name = 'detalle_miembro.html'
    context_object_name = 'holo'

def detalle_miembro(request, uuid):
    miembro = get_object_or_404(Holomem, uuid=uudi)
    context = {
        'miembro': miembro
    }
    return render(request, 'detalle_miembro.html', context)


class HolomemCreateView(CreateView):
    model = Holomem
    form_class = HolomemForm
    template_name = 'agregar_miembro.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        return super().form_valid(form)

def base(request):
    return render(request, 'base.html')