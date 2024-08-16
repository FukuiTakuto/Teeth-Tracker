from django.urls import path
from .views import HomeView,SignupView,IndexView,LoginView,LogoutView,MediaUploadView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'teethapp'

urlpatterns = [
    path('index/',IndexView.as_view(),name = "index"),
    path('home/',HomeView.as_view(),name = "home"),
    path('signup/',SignupView.as_view(),name = "signup"),
    path('login/',LoginView.as_view(),name = "login"),
    path("logout/",LogoutView.as_view(),name='logout'),
    path("mediaupload",MediaUploadView.as_view(),name="mediaupload")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)