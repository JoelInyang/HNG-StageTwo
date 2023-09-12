from django.urls import path
from .views import PersonListCreateView, PersonRetrieveUpdateDeleteView

urlpatterns = [
    path('persons/', PersonListCreateView.as_view(), name='person-list-create'),
    path('person/<int:pk>/', PersonRetrieveUpdateDeleteView.as_view(), name='person-list-create'),
]