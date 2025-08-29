from django.shortcuts import render, redirect
from .models import Consulta
from django import forms
from django.shortcuts import get_object_or_404
from django.db.models import Sum
from django.utils.dateparse import parse_date
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# =========================
# Formulário de Consulta
# =========================
class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'  
        widgets = {
            'data_consulta': forms.DateInput(attrs={'type': 'date'}),
            'horario_inicio': forms.TimeInput(attrs={'type': 'time'}),
            'horario_fim': forms.TimeInput(attrs={'type': 'time'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'usuario' in self.fields:
            del self.fields['usuario']

# =========================
# Página inicial com calendário
# =========================
@login_required 
def home(request):
    consultas = Consulta.objects.filter(usuario=request.user)
    return render(request, 'home.html', {'consultas': consultas})

# =========================
# Cadastro de nova consulta
# =========================
@login_required 
def consulta_nova(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST, user = request.user)
        if form.is_valid():
            consulta = form.save(commit=False)  
            consulta.usuario = request.user    
            consulta.save()                    
            return redirect('home')
    else:
        form = ConsultaForm(user=request.user)
    return render(request, 'consultas/consulta_form.html', {'form': form})

# =========================
# Lista de consultas / Relatórios
# =========================
@login_required 
def consulta_lista(request):
    consultas = Consulta.objects.filter(usuario=request.user)
    total_valor = 0

    # Filtros
    data_inicio = request.GET.get('data_inicio')
    data_fim = request.GET.get('data_fim')
    situacao = request.GET.get('situacao')

    if data_inicio:
        consultas = consultas.filter(data_consulta__gte=parse_date(data_inicio))
    if data_fim:
        consultas = consultas.filter(data_consulta__lte=parse_date(data_fim))
    if situacao and situacao != 'Todos':
        consultas = consultas.filter(situacao=situacao)

    # Totalizar valores
    total_valor = consultas.aggregate(Sum('valor_consulta'))['valor_consulta__sum'] or 0

    return render(request, 'consultas/consulta_list.html', {
        'consultas': consultas,
        'total_valor': total_valor,
        'data_inicio': data_inicio or '',
        'data_fim': data_fim or '',
        'situacao': situacao or 'Todos',
    })

# =========================
# Página de calendário (opcional, se precisar)
# =========================
@login_required 
def calendario(request):
    consultas = Consulta.objects.filter(usuario=request.user)
    return render(request, 'consultas/calendario.html', {'consultas': consultas})

@login_required 
def consulta_editar(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = ConsultaForm(request.POST, instance=consulta, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Consulta atualizada com sucesso!")
            return redirect('home')  # volta para o calendário
        else:
            messages.error(request, "Erro ao atualizar a consulta. Verifique os campos.")
    else:
        form = ConsultaForm(instance=consulta, user=request.user)

    return render(request, 'consultas/consulta_form.html', {'form': form})
