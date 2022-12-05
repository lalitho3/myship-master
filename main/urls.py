from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('upload_post/', UploadPost.as_view(), name='upload_post')
]