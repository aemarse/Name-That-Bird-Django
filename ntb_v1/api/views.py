from api.models import Sounds, Annotations
from api.serializers import SoundSerializer, AnnotationSerializer
from api.serializers import UserSerializer
from rest_framework import generics, permissions
from api.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User


class SoundList(generics.ListCreateAPIView):
	"""
	List all sounds
	"""
	queryset = Sounds.objects.all()
	serializer_class = SoundSerializer


class SoundDetail(generics.RetrieveUpdateDestroyAPIView):
	"""
	Retrieve, update, or delete a sound instance
	"""
	queryset = Sounds.objects.all()
	serializer_class = SoundSerializer


class AnnotationList(generics.ListCreateAPIView):
	"""
	List all annotations
	"""
	queryset = Annotations.objects.all()
	serializer_class = AnnotationSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	# def pre_save(self, obj):
	# 	obj.owner = self.request.user


class AnnotationDetail(generics.RetrieveUpdateDestroyAPIView):
	"""
	Retrieve, update, or delete an annotation instance
	"""
	queryset = Annotations.objects.all()
	serializer_class = AnnotationSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, 
							IsOwnerOrReadOnly,)

	# def pre_save(self, obj):
	# 	obj.owner = self.request.user


class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
