from django.urls import path
from .views import company_list, upload_csv, esg_history

urlpatterns = [
    path("", company_list),
    path("upload/", upload_csv),
    path("history/<int:company_id>/", esg_history),
]