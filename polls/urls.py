from django.urls import path
from .import views
    
urlpatterns = [
    path('', views.polls_list, name='polls_list'),
    path('<int:polls_id>', views.polls_detail, name="polls_detail"), 
    path('type/<int:polls_type_id>', views.polls_with_type, name="polls_with_type" ),
    path('type/<int:polls_type_id>', views.polls_with_type, name="polls_with_type"),
    path('date/<int:year>/<int:month>', views.polls_with_date, name="polls_with_date"),
  
]