from django.conf.urls import url
from .views import *

urlpatterns=[
		url(r'^CREATE_CLIENT/$',CREATE_CLIENT,name="CREATE_CLIENT"),
		url(r'^GET_LIST_CLIENT/$',GET_LIST_CLIENT,name="GET_LIST_CLIENT"),
		url(r'^GET_CLIENT/$',GET_CLIENT,name="GET_CLIENT"),
		url(r'^DELETE_CLIENT/$',DELETE_CLIENT,name="DELETE_CLIENT"),
		url(r'^EDIT_CLIENT/$',EDIT_CLIENT,name="EDIT_CLIENT"),
	]