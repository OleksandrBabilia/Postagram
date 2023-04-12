from rest_framework import serializers


class AbstractSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(sources='public_id', read_only=True, format='hex')
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
    
    class Meta:
        abstract = True