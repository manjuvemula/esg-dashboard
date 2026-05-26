from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static


# ---------------- HOME PAGE ----------------
def home(request):
    return HttpResponse("ESG Backend Running 🚀")


# ---------------- URLS ----------------
urlpatterns = [
    path("", home),
    path("admin/", admin.site.urls),
    path("api/companies/", include("companies.urls")),
]

# ---------------- MEDIA FILES ----------------
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)