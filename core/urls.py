from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.conf import settings

#Realmente nose porque hace esto.    !!INVESTIGAR MAS!!
urlpatterns = [
    #Definimos la ruta de donde va a leer apps(carpeta) blog->urls
    path('api/blog/', include('apps.blog.urls')),
    path('api/category/', include('apps.category.urls')),


    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]