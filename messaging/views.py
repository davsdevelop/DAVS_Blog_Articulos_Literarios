from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Mensaje
from .forms import MensajeForm

# Bandeja de entrada (mensajes recibidos)
@login_required
def bandeja_entrada(request):
    mensajes = Mensaje.objects.filter(destinatario=request.user).order_by('-fecha_envio')
    return render(request, 'messaging/bandeja_entrada.html', {'mensajes': mensajes})

# Enviar un nuevo mensaje
@login_required
def enviar_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST, usuario_actual=request.user)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.remitente = request.user 
            mensaje.save()
            return redirect('bandeja_entrada')
    else:
        form = MensajeForm(usuario_actual=request.user)
        
    return render(request, 'messaging/enviar_mensaje.html', {'form': form})

# Leer un mensaje en detalle
@login_required
def leer_mensaje(request, pk):
    mensaje = get_object_or_404(Mensaje, pk=pk, destinatario=request.user)
    return render(request, 'messaging/leer_mensaje.html', {'mensaje': mensaje})