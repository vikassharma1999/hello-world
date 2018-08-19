from django.urls import path
app_name="CreateDb"
from .import views
urlpatterns=[
path('',views.model_form_upload,name="CreateDb")
] 