from django.urls import path
from . import views # para poder acceder a vistas
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    #cuando usuario aceda a app que se redireccione a:
    #  path('',views.inicio,name='inicio'), 
    path('',views.index,name='inicio'),
    path('nosotros',views.nosotros,name='nosotros'),

    path('personaje',views.personaje,name='personaje'),

    path('personaje/crear',views.crear,name='crear'),
    path('personaje/editar',views.editar,name='editar'),
    path('eliminar/<int:id>',views.eliminar,name='eliminar'),
     path('personaje/editar/<int:id>',views.editar,name='editar')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
