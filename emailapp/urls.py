from django.urls import path
from .views import SendBulkEmail

urlpatterns = [
    path("send-email/", SendBulkEmail.as_view(), name="send_email"),
]