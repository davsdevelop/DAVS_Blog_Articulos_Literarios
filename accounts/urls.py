from django.urls import path
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView
from . import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('password/', PasswordChangeView.as_view(template_name='accounts/cambiar_password.html', success_url='/cuentas/password/exito/'), name='cambiar_password'),
    path('password/exito/', PasswordChangeDoneView.as_view(template_name='accounts/password_exito.html'), name='password_exito'),
]