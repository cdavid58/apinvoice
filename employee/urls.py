from django.conf.urls import url
from .views import *

urlpatterns=[
		url(r'^Register_Employee/$',Register_Employee,name="Register_Employee"),
		url(r'^Validate_Login/$',Validate_Login,name="Validate_Login"),
		url(r'^GET_LIST_EMPLOYEE/$',GET_LIST_EMPLOYEE,name="GET_LIST_EMPLOYEE"),
		url(r'^GET_EMPLOYEE/$',GET_EMPLOYEE,name="GET_EMPLOYEE"),
		url(r'^CHANGE_PHOTO_PROFILE/$',CHANGE_PHOTO_PROFILE,name="CHANGE_PHOTO_PROFILE"),
	]