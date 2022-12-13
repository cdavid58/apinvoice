from django.conf.urls import url
from .views import *

urlpatterns=[
		url(r'^Register_Employee/$',Register_Employee,name="Register_Employee"),
		url(r'^Validate_Login/$',Validate_Login,name="Validate_Login"),
	]