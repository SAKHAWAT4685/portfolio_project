from django.urls import path
from .views import *

urlpatterns = [
    path('<name>/home', home, name='home'),
    path('<name>/about', about, name= 'about'),
    path('<name>/resume', resume, name='resume'),
    path('<name>/service', service, name='service'),
    path('<name>/portfolio', portfolio, name='portfolio'),
    path('<name>/contact', contact, name='contact'),
    path('<name>/contact', contact, name='contact'),
    path('project_details/<int:id>', project_details, name='project_details'),

]