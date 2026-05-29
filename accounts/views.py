from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .forms import RegistroUsuarioForm, EditarUsuarioForm, EditarPerfilForm
from .models import Perfil


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

# Vista de Registro
def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    
    return render(request, 'accounts/registro.html', {'form': form})

# Vista de Perfil 
@login_required
def perfil(request):
    return render(request, 'accounts/perfil.html')

# Vista para Editar el Perfil
@login_required
def editar_perfil(request):

    perfil = request.user.perfil 
    
    if request.method == 'POST':
        user_form = EditarUsuarioForm(request.POST, instance=request.user)
        perfil_form = EditarPerfilForm(request.POST, request.FILES, instance=perfil)
        
        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()
            return redirect('perfil')
    else:
        user_form = EditarUsuarioForm(instance=request.user)
        perfil_form = EditarPerfilForm(instance=perfil)
        
    return render(request, 'accounts/editar_perfil.html', {
        'user_form': user_form,
        'perfil_form': perfil_form
    })