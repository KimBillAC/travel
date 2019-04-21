from rest_framework import serializers


class UserRegSerializer(serializers.ModelSerializer):

    class Meta:

        fields = '__all__'


class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:

        fiedls = '__all__'


