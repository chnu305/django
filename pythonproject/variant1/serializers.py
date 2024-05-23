from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Files, Accounts

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', "groups"]

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = '__all__'

class FileSerializer(serializers.ModelSerializer):
    author_file = AccountsSerializer()

    class Meta:
        model = Files
        fields = '__all__'