from rest_framework import serializers
from api.models import Sounds, Annotations
from django.contrib.auth.models import User


class SoundSerializer(serializers.ModelSerializer):
	annotations = serializers.PrimaryKeyRelatedField(many=True)
	
	class Meta:
		model = Sounds
		fields = ('id', 'xenocanto_url', 'species_name', 
			'waveform_path', 'spectrogram_path', 'added_date', 
			'annotations')


class AnnotationSerializer(serializers.ModelSerializer):
	owner = serializers.Field(source='owner.username')

	class Meta:
		model = Annotations
		fields = ('id', 'user', 'sound', 'wave_onset', 'wave_offset', 
			'spec_onset', 'spec_offset', 'species', 
			'added_date')


class UserSerializer(serializers.ModelSerializer):
	annotations = serializers.PrimaryKeyRelatedField(many=True)

	class Meta:
		model = User
		fields = ('id', 'username', 'annotations')
