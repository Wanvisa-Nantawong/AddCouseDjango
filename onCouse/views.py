from rest_framework import  viewsets

from .forms import AddCouseForm
from .models import AddCouse
from .serializers import AddCouseSerializer


class AddCouseViewSet(viewsets.ModelViewSet) :
    queryset = AddCouse.objects.all()
    serializer_class = AddCouseSerializer

