from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('count/', views.count, name = 'count'),
    path('about/', views.about, name = 'about'),
    path('secret/', views.secret, name = 'secret')
]




#dead code
#from django.contrib import admin
'''urlpatterns = [
    path('', views.home),
    path('eggs/', views.eggs),
    path('new/', views.new)
]'''

'''urlpatterns = [
    path('thefartlord/', admin.site.urls),
]'''
