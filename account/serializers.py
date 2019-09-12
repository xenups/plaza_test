from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['name', 'bio', 'pic']
        read_only_fields = ['pic']


class ProfilePicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['pic']
