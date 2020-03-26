from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index,name='index'),
    # path('result',views.result,name='result'),
    # path('path_and_rename',views.path_and_rename, name="path_and_rename"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)