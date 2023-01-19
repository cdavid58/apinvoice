from django.conf.urls import url
from .views import *

urlpatterns=[
		url(r'^CREATE_SHOPPINGS/$',CREATE_SHOPPINGS,name="CREATE_SHOPPINGS"),
		url(r'^CHECK_INVOICE_NUMBER/$',CHECK_INVOICE_NUMBER,name="CHECK_INVOICE_NUMBER"),
	]