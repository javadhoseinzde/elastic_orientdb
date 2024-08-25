from rest_framework import serializers

class OrientSerializer(serializers.Serializer):
    host = serializers.CharField(max_length=100, required=True)
    port = serializers.CharField(max_length=100, required=True)
    user = serializers.CharField(max_length=100, required=False)
    password = serializers.CharField(max_length=100, required=False)


class CreateDbSerializer(serializers.Serializer):
    host_id = serializers.CharField(max_length=100, required=True)
    db_name = serializers.CharField(max_length=100, required=True)


class CreateTableSerializer(serializers.Serializer):
    host_id = serializers.CharField(max_length=100, required=True)
    db_name = serializers.CharField(max_length=100, required=True)
    table_name = serializers.CharField(max_length=100, required=True)


class InsertTableSerializer(serializers.Serializer):
    host_id = serializers.CharField(max_length=100, required=True)
    db_name = serializers.CharField(max_length=100, required=True)
    table_name = serializers.CharField(max_length=100, required=True)
    name = serializers.CharField(max_length=100, required=True)
    price = serializers.CharField(max_length=100, required=True)

class UpdateTableSerializer(serializers.Serializer):
    host_id = serializers.CharField(max_length=100, required=True)
    db_name = serializers.CharField(max_length=100, required=True)
    table_name = serializers.CharField(max_length=100, required=True)
    name = serializers.CharField(max_length=100, required=True)
    new_name = serializers.CharField(max_length=100, required=True)
