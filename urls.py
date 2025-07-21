from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('',views.index,name='index'),
     path('math/',views.math,name='math'),
     path('technology/',views.technology,name='technology'),
     path('bacci/',views.bacci,name='bacci'),
     path('leanai/',views.lean_ai,name='lean_ai'),
     path('test/',views.test,name='test'),
     path('login/',views.login,name='login'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

