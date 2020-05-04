from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
app_name="myuser"

urlpatterns=[
    # path('',views.index,name='index'),
    path('',views.LoginView.as_view(),name='login'),
    path('register/',views.UserFormView.as_view(),name='register'),
    # path('forgotpassword/',views.forgotpassword,name='forgotpasssword')
]
