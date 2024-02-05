# annotator/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_pdf, name='upload_pdf'),
    path('annotate/<int:pdf_id>/', views.annotate_pdf, name='annotate_pdf'),
    path('export/<int:pdf_id>/', views.export_pdf, name='export_pdf'),
]
