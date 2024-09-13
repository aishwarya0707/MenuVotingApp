from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import CreateEmployeeAPIView, LoginView, LogoutView, RegisterView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("create-employee/", CreateEmployeeAPIView.as_view(), name="employee_create"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
