from .serializer import OrientSerializer, CreateDbSerializer, CreateTableSerializer, \
        InsertTableSerializer, UpdateTableSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .orient_connector import OrientCrud
from apps.orient.models import OrientHost

class OrientApiView(APIView):
    def post(self, request):
        serializer = OrientSerializer(data=request.data)
        if serializer.is_valid():
            host = serializer.validated_data.get("host")
            port = serializer.validated_data.get("port")
            user = serializer.validated_data.get("user")
            password = serializer.validated_data.get("password")            

            query = OrientHost.objects.create(host=host, port=port,\
                                               user=user, password=password)
            print(query.id)
            return Response({
                "orient_id" : query.id
            })
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CreateDbApiView(APIView):
    
    def post(self, request):
        print("valid0")
        serializer = CreateDbSerializer(data=request.data)
        if serializer.is_valid():
            print("valid")
            host = serializer.validated_data.get("host_id")
            db_name = serializer.validated_data.get("db_name")
            
            ins = OrientCrud(host=host)
            db = ins.create_database(db_name)


            return Response(
                {"create_db": db}
            )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class DeleteDbApiView(APIView):
    
    def post(self, request):
        print("valid0")
        serializer = CreateDbSerializer(data=request.data)
        if serializer.is_valid():
            print("valid")
            host = serializer.validated_data.get("host_id")
            db_name = serializer.validated_data.get("db_name")
            
            ins = OrientCrud(host=host)
            db = ins.delete_database(db_name)


            return Response(
                {"delete_db": db}
            )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CreateTableApiView(APIView):
    
    def post(self, request):
        print("valid0")
        serializer = CreateTableSerializer(data=request.data)
        if serializer.is_valid():
            print("valid")
            host = serializer.validated_data.get("host_id")
            db_name = serializer.validated_data.get("db_name")
            table_name = serializer.validated_data.get("table_name")


            ins = OrientCrud(host=host)
            db = ins.create_table(db_name, table_name)


            return Response(
                {"create_table": db}
            )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class DeleteTableApiView(APIView):
    
    def post(self, request):
        print("valid0")
        serializer = CreateTableSerializer(data=request.data)
        if serializer.is_valid():
            print("valid")
            host = serializer.validated_data.get("host_id")
            db_name = serializer.validated_data.get("db_name")
            table_name = serializer.validated_data.get("table_name")

            ins = OrientCrud(host=host)
            db = ins.drop_table(db_name, table_name)


            return Response(
                {"delete_table": db}
            )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



class InsertTableApiView(APIView):
    
    def post(self, request):
        print("valid0")
        serializer = InsertTableSerializer(data=request.data)
        if serializer.is_valid():
            print("valid")
            host = serializer.validated_data.get("host_id")
            db_name = serializer.validated_data.get("db_name")
            table_name = serializer.validated_data.get("table_name")
            name = serializer.validated_data.get("name")
            price = serializer.validated_data.get("price")

            ins = OrientCrud(host=host)
            db = ins.insert_table(db_name, table_name, name, price)


            return Response(
                {"insert_table": db}
            )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ListTableApiView(APIView):
    
    def post(self, request):
        print("valid0")
        serializer = CreateDbSerializer(data=request.data)
        if serializer.is_valid():
            print("valid")
            host = serializer.validated_data.get("host_id")
            db_name = serializer.validated_data.get("db_name")
            
            ins = OrientCrud(host=host)
            db = ins.get_classes(db_name)

            return Response(
                {"table_list": db}
            )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TableRowApiView(APIView):
    
    def post(self, request):
        print("valid0")
        serializer = CreateTableSerializer(data=request.data)
        if serializer.is_valid():
            print("valid")
            host = serializer.validated_data.get("host_id")
            db_name = serializer.validated_data.get("db_name")
            table_name = serializer.validated_data.get("table_name")
            
            ins = OrientCrud(host=host)
            db = ins.get_row(db_name, table_name)

            return Response(
                {"db": db}
            )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UpdateRowApiView(APIView):
    
    def post(self, request):
        print("valid0")
        serializer = UpdateTableSerializer(data=request.data)
        if serializer.is_valid():
            print("valid")
            host = serializer.validated_data.get("host_id")
            db_name = serializer.validated_data.get("db_name")
            table_name = serializer.validated_data.get("table_name")
            name = serializer.validated_data.get("name")
            new_name = serializer.validated_data.get("new_name")

            ins = OrientCrud(host=host)
            db = ins.update(table_name, name, new_name, db_name)

            return Response(
                {"db": db}
            )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)