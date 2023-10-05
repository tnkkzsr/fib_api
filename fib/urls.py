from django.urls import path
from .views import TestView,FibView



    
urlpatterns =[
    path("test/",TestView.as_view(),name="test"),
    path("fib/",FibView.as_view(),name="fib"),
]