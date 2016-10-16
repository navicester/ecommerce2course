from django.shortcuts import render

from django.views.generic.edit import FormView
from .forms import AddressForm

# Create your views here.
class AddressSelectFormView(FormView):
	form_class = AddressForm
	template_name = "orders/address_select.html"