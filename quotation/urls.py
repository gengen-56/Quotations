from django.conf.urls import url
from . import views

app_name = 'quotations'

urlpatterns = [
    url('', views.QuotationView.as_view(), name='index')
]
