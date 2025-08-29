
# from django.shortcuts import render, redirect,  get_object_or_404
# from .models import Paciente
# from django import forms

# class PacienteForm(forms.ModelForm):
#     class Meta:
#         model = Paciente
#         fields = '__all__'

# def paciente_novo(request):
#     if request.method == 'POST':
#         form = PacienteForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('paciente_lista')
#     else:
#         form = PacienteForm()
#     return render(request, 'pacientes/paciente_form.html', {'form': form})

# def paciente_lista(request):
#     pacientes = Paciente.objects.all()
#     return render(request, 'pacientes/paciente_list.html', {'pacientes': pacientes})

# def paciente_editar(request, pk):
#     paciente = get_object_or_404(Paciente, pk=pk)
#     if request.method == 'POST':
#         form = PacienteForm(request.POST, instance=paciente)
#         if form.is_valid():
#             form.save()
#             return redirect('paciente_lista')
#     else:
#         form = PacienteForm(instance=paciente)
#     return render(request, 'pacientes/paciente_form.html', {'form': form})

# def paciente_excluir(request, pk):
#     paciente = get_object_or_404(Paciente, pk=pk)
#     if request.method == 'POST':
#         paciente.delete()
#         return redirect('paciente_lista')
#     return render(request, 'pacientes/paciente_confirm_delete.html', {'paciente': paciente})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Paciente
from django import forms

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'email', 'telefone']  
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'usuario' in self.fields:
            del self.fields['usuario']

@login_required
def paciente_novo(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            paciente = form.save(commit=False)
            paciente.usuario = request.user  # 🔐 Associa ao usuário logado
            paciente.save()
            return redirect('paciente_lista')
    else:
        form = PacienteForm()
    return render(request, 'pacientes/paciente_form.html', {'form': form})

@login_required
def paciente_lista(request):
    #  Filtra apenas pacientes do usuário logado
    pacientes = Paciente.objects.filter(usuario=request.user)
    return render(request, 'pacientes/paciente_list.html', {'pacientes': pacientes})

@login_required
def paciente_editar(request, pk):
    # 🔐 Garante que só o dono pode editar
    paciente = get_object_or_404(Paciente, pk=pk, usuario=request.user)
    
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('paciente_lista')
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'pacientes/paciente_form.html', {'form': form})

@login_required
def paciente_excluir(request, pk):
    # 🔐 Garante que só o dono pode excluir
    paciente = get_object_or_404(Paciente, pk=pk, usuario=request.user)
    
    if request.method == 'POST':
        paciente.delete()
        return redirect('paciente_lista')
    return render(request, 'pacientes/paciente_confirm_delete.html', {'paciente': paciente})
