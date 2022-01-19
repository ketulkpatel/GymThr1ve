from rest_framework import serializers
from .models import Brand


# class Assets_Server_Channels_serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Assets_Server_Channels
#         fields = ('asset_server_channel_name',)	

class Brand_Serializer(serializers.ModelSerializer):
	# asset_server_channel_id = serializers.RelatedField(source="Assets_Server_Channels",read_only=True)
	# asset_server_channel_id = serializers.PrimaryKeyRelatedField(queryset=Assets_Server_Channels.objects.all(), source='asset_server_channel_channel', write_only=True)

	class Meta:
		model = Brand
		fields = ['brand_id','brand_name']
		depth = 1
