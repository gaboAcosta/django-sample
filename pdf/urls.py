from django.urls import path
from .views import InvoiceView

urlpatterns = [
    path('invoice', InvoiceView.render_pdf)
]
