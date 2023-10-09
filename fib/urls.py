from django.urls import path
from .views import FibView

handler404 = 'fib.views.custom_404'
urlpatterns =[
    path("fib/",FibView.as_view(),name="fib"),
]

