from rest_framework import serializers

class ElasticSerializer(serializers.Serializer):
    host = serializers.CharField(max_length=100, required=True)
    port = serializers.CharField(max_length=100, required=True)
    user = serializers.CharField(max_length=100, required=False)
    password = serializers.CharField(max_length=100, required=False)
    index = serializers.CharField(max_length=100, required=False)
    aggs = serializers.CharField(max_length=100, required=False)
    
