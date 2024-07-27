from django.views.generic import TemplateView
from .models import *

class IndexView(TemplateView):
	template_name = "index.html"
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
		context["purchase_objects"] = Purchase
		return context