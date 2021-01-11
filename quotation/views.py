from django.views.generic import TemplateView
from .models import Quotation
# Create your views here.


class QuotationView(TemplateView):
    model = Quotation
    context_object_name = '名前'
    template_name = 'quotation/index.html'
