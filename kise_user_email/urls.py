from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import SendEmailView

urlpatterns = [
    path('send_email/', SendEmailView.as_view(), name="send_email"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
