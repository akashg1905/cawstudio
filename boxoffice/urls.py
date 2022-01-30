from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include

from boxoffice import views

urlpatterns=[
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('register',views.register,name='register'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)