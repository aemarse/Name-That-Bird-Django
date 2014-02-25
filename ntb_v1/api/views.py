from api.models import Sounds, Annotations, Lessons, Playlists, Species, GroundTruth
from api.serializers import SoundSerializer, AnnotationSerializer, SpeciesSerializer
from api.serializers import UserSerializer, PlaylistSerializer, LessonSerializer, GroundTruthSerializer
from api.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions, renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User


@api_view(('GET',))
def api_root(request, format=None):
	return Response({
		'users': reverse('user-list', request=request, format=format),
		'sounds': reverse('sound-list', request=request, format=format),
		'annotations': reverse('annotation-list', request=request, format=format),
		'playlists': reverse('playlist-list', request=request, format=format),
		'lessons': reverse('lesson-list', request=request, format=format),
		'truth': reverse('groundtruth-list', request=request, format=format),
	})

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


class PlaylistList(generics.ListCreateAPIView):
	"""
	List all sounds
	"""
	queryset = Playlists.objects.all()
	serializer_class = PlaylistSerializer


class PlaylistDetail(generics.RetrieveUpdateDestroyAPIView):
	"""
	Retrieve, update, or delete a sound instance
	"""
	queryset = Playlists.objects.all()
	serializer_class = PlaylistSerializer


class LessonList(generics.ListCreateAPIView):
	"""
	List all sounds
	"""
	queryset = Lessons.objects.all()
	serializer_class = LessonSerializer


class LessonDetail(generics.RetrieveUpdateDestroyAPIView):
	"""
	Retrieve, update, or delete a sound instance
	"""
	queryset = Lessons.objects.all()
	serializer_class = LessonSerializer


class GroundTruthList(generics.ListCreateAPIView):
	"""
	List all sounds
	"""
	queryset = GroundTruth.objects.all()
	serializer_class = GroundTruthSerializer


class GroundTruthDetail(generics.RetrieveUpdateDestroyAPIView):
	"""
	Retrieve, update, or delete a sound instance
	"""
	queryset = GroundTruth.objects.all()
	serializer_class = GroundTruthSerializer
