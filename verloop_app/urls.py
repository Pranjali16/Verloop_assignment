from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^add/', StoryView.as_view(), name='add-story'),
]