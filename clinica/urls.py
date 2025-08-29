from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.views.generic import RedirectView 
from consultas.views import home
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', RedirectView.as_view(url='/login/', permanent=False)), 
    path('', login_required(home), name='home'),  # ← Protege a view diretamente
    path('pacientes/', include('pacientes.urls')),
    path('consultas/', include('consultas.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('home/', home, name='home'),  
]