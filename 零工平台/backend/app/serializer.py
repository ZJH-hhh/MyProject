from rest_framework import serializers
from app.models.jobs import Jobs
from app.models.UserInfo import Users


class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        filds = '__all__'
