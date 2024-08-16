from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/authent/login/')),  # Redirect to the login page of the authent app
    path('admin/', admin.site.urls),
    path('authent/', include('authent.urls')),
    path('compte/', include('compte.urls')),
    path('user/', include('user.urls')),
    path('client/', include('client.urls')),
    
]
