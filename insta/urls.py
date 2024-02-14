"""insta URL Configuration"""

from django.contrib import admin

from django.urls import include, path

from gram import views

from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

'''Here we have imported (include)-: this allows us to add the gram url pattern
as done below this is to avoid filling up all our urls in this page'''

''' End Of Import'''
#-------------------------------#


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('gram.urls')),

    #url for registration
    # path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('login/',views.login,name ='login'),
    path('accounts/', include('registration.backends.simple.urls')),

]