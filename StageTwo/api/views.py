from rest_framework import generics
from Stage2App.models import Person
from .serializers import PersonSerializer

class PersonListCreateView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    
    def get_queryset(self):
        queryset = Person.objects.all()
        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(name=name)
        return queryset
    
    
class PersonRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer