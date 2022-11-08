
from django.contrib import admin
from django.http import StreamingHttpResponse
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from camera import VideoCamera, gen


urlpatterns = [
    path('monitor/', lambda r: StreamingHttpResponse(gen(VideoCamera()),
                                                         content_type='multipart/x-mixed-replace; boundary=frame')),
    path('admin/', admin.site.urls),
    path('video/', include('video.urls')),
    path('', include('landing.urls')),
    path('SK/', include('SK.urls')),
    path('Town/', include('Town.urls')),
    path('Edu/', include('Edu.urls')),
    path('Result/', include('Result.urls')),
    path('About/', include('About.urls')),
    path('Record/', include('Record.urls')),
    


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)