from django.views.generic import TemplateView,CreateView,ListView
from django.contrib.auth.views import LoginView as BaseLoginView,LogoutView as BaseLogoutView
from .forms import SignupForm,LoginForm,MediaUploadForm
from django.urls import reverse_lazy
from .models import MediaUploadModel

# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"
      
class HomeView(ListView):
    template_name = "home.html"
    model = MediaUploadModel
    context_object_name = "images"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        tag = self.request.GET.get('tag')
        if tag:
            queryset = queryset.filter(tag=tag)
        return queryset
    
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
    
class MediaUploadView(CreateView):
    template_name = "mediaupload.html"
    form_class = MediaUploadForm
    success_url = reverse_lazy("teethapp:home")
    
 