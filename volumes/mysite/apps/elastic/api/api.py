from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import ElasticSerializer
from .elastic_connector import Elastic

    

class ElasticApi(APIView):
    def post(self, request):
        serializer = ElasticSerializer(data=request.data)
        if serializer.is_valid():
            host = serializer.validated_data.get("host")
            port = serializer.validated_data.get("port")
            user = serializer.validated_data.get("user")
            password = serializer.validated_data.get("password")
            aggs = serializer.validated_data.get("aggs")
            index = serializer.validated_data.get("index")

            ins = Elastic(host=host, port=port, user=user, password=password, aggs=aggs, index=index)

            res = ins.aggregation()
            
            return Response({
                f"index {index} aggregation field {aggs}": res
            })
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
