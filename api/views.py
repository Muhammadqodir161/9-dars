from rest_framework.views import APIView
from rest_framework.response import Response
from .versioning import CustomVersioning 
class ProductListView(APIView):
    versioning_class = CustomVersioning 

    def get(self, request):
        version = request.version 
        return Response({
            "version": version, 
            "message": "Product list"
        })

