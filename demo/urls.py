from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    path('', views.home, name='home'),        #首页 ^^^^^^
    path('admin/', admin.site.urls),
    path('ckeditor', include( 'ckeditor_uploader.urls')),
    path('polls/', include('polls.urls')),         #链接 子url 
    path('comment/', include('comment.urls')),  
    path('likes/', include('likes.urls')),  
    path('user/', include('user.urls')),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)