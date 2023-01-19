from django.conf.urls import url
from .views import *

urlpatterns=[
		url(r'^CREATE_INVOICE/$',CREATE_INVOICE,name="CREATE_INVOICE"),
		url(r'^GET_LIST_INVOICE/$',GET_LIST_INVOICE,name="GET_LIST_INVOICE"),
		url(r'^GET_INVOICE/$',GET_INVOICE,name="GET_INVOICE"),
		url(r'^Send_DIAN/$',Send_DIAN,name="Send_DIAN"),
		url(r'^GET_CONSECUTIVE/$',GET_CONSECUTIVE,name="GET_CONSECUTIVE"),
		url(r'^CLEAN_FILE/$',CLEAN_FILE,name="CLEAN_FILE"),
		url(r'^DELETE_INVOICE/$',DELETE_INVOICE,name="DELETE_INVOICE"),
	]