from django.urls import path
from .views import FibView



    
urlpatterns =[

    path("fib/",FibView.as_view(),name="fib"),
]