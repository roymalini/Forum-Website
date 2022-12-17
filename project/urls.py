from django.contrib import admin
from django.urls import path,include
from chat import views as chatView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('chatroom/', chatView.chatroom, name = "chatroom"),
    path('chat/', include('chat.urls')),
    path('',include('forum.urls')),
    path('',include('Auth.urls')),
]+ static(settings.MEDIA_URL , document_root= settings.MEDIA_ROOT)
