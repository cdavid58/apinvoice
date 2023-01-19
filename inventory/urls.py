from django.conf.urls import url
from .views import *

urlpatterns=[
		url(r'^Save_Category/$',Create_Category,name="Save_Category"),
		url(r'^Save_SubCategory/$',CreateSubCategories,name="Save_SubCategory"),
		url(r'^CREATE_INVENTORY/$',CREATE_INVENTORY,name="CREATE_INVENTORY"),
		url(r'^GET_PRODUCT/$',GET_PRODUCT,name="GET_PRODUCT"),
		url(r'^GET_LIST_INVENTORY/$',GET_LIST_INVENTORY,name="GET_LIST_INVENTORY"),
		url(r'^UPDATE_PRODUCT/$',UPDATE_PRODUCT,name="UPDATE_PRODUCT"),
		url(r'^DELETE_PRODUCT/$',DELETE_PRODUCT,name="DELETE_PRODUCT"),
	]