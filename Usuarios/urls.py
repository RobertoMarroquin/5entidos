from django.urls import path,include

from .models import Usuario
from .views import signup_view,login_view,logout_func

urlpatterns = [
    path('registro/',signup_view,name="signup"),
    path('login/',login_view,name="login"),
    path('logout/',logout_func, name='logout'),

]
