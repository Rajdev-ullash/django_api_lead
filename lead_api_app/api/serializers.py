from os import name
from rest_framework import serializers
from lead_api_app.models import Lead



class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Lead
        fields= "__all__"
    
    # def validate(self,data):
    #     if data['name'] == data['designation']:
    #         raise serializers.ValidationError.("Name & Designation should be unique")
    #     else:
    #         return data

    # def validate_name(self,value):
    #     if len(value)<2:
    #         raise serializers.ValidationError("Name must be at least 3 characters")

    #     else:
    #         return value


# class LeadSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     email = serializers.CharField()
#     phone = serializers.CharField()
#     designation = serializers.CharField()

#     def create(self, validated_data):
#         return Lead.objects.create(**validated_data)

#     def update(self,instance, validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.email = validated_data.get('email',instance.email)
#         instance.phone = validated_data.get('phone',instance.phone)
#         instance.designation = validated_data.get('designation',instance.designation)

#         instance.save()
#         return instance