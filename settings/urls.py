from django.conf.urls import url
from .views import *

urlpatterns=[
		url(r'^Type_DocumentI/$',Type_DocumentI,name="Type_DocumentI"),
		url(r'^Type_Organizations/$',Type_Organizations,name="Type_Organizations"),
		url(r'^Type_Regimen/$',Type_Regimen,name="Type_Regimen"),
		url(r'^Municipalitys/$',Municipalitys,name="Municipalitys"),
		url(r'^Type_Documents/$',Type_Documents,name="Type_Documents"),
	]