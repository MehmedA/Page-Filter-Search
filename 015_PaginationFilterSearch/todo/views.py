from rest_framework.viewsets import ModelViewSet

from .serializers import Todo, TodoSerializer

from .paginations import CustomPageNumberPagination

#from rest_framework.pagination import PageNumberPagination



class TodoView(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = CustomPageNumberPagination #locale settings

#Alternatif gecici yontem:
#PageNumberPagination.page_size = 25

#page_query_param =
#PageNumberPagination.page_query_param = 'sayfa'
#PageNumberPagination.page_size_query_param = 'adet'