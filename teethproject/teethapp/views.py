from django.views.generic import TemplateView,CreateView
from django.contrib.auth.views import LoginView as BaseLoginView,LogoutView as BaseLogoutView
from .forms import SignupForm,LoginForm
from django.urls import reverse_lazy

# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"
    
class HomeView(TemplateView):
    template_name = "home.html"
    
class LoginView(BaseLoginView):
    form_class = LoginForm
    template_name = "login.html"
    success_url = reverse_lazy("teethapp:home")
    
class SignupView(CreateView):
    form_class = SignupForm
    template_name = "signup.html"
    success_url = reverse_lazy("teethapp:login")
    
class LogoutView(BaseLogoutView):
    success_url = reverse_lazy("teethapp:index")
    
    
 