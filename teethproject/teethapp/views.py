from django.views.generic import TemplateView,CreateView,ListView
from django.contrib.auth.views import LoginView as BaseLoginView,LogoutView as BaseLogoutView
from .forms import SignupForm,LoginForm,MediaUploadForm,EventForm
from django.urls import reverse_lazy
from .models import MediaUploadModel,CalendarModel
from django.http import Http404,HttpResponse
import json
from django.middleware.csrf import get_token
from django.template import loader


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
    
def CalendarView(request):
    get_token(request)
    template = loader.get_template("calendar.html")
    return HttpResponse(template.render())
 
def Eventadd(request):
    if request.method == "GET":
        raise Http404()
    
    datas = json.loads(request.body)
    eventform = EventForm(datas)
    if eventform.is_valid()  == False:
        raise Http404()
    
    start_date = datas["start_date"]
    end_date = datas["end_date"]
    event_name = datas["event_name"]
    
    event = CalendarModel(
        event_name = str(event_name),
        start_date = start_date,
        end_date = end_date,
    )
    event.save()
    
    return HttpResponse("")