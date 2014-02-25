from django.db import models


class Lessons(models.Model):
	playlist = models.ForeignKey('Playlists', related_name="lessons")
	added_date = models.DateTimeField(auto_now_add=True)


class Sounds(models.Model):
	xenocanto_url = models.URLField(max_length=200)
	species_name = models.CharField(max_length=100)
	waveform_path = models.FilePathField(path=None)
	spectrogram_path = models.FilePathField(path=None)
	species = models.ForeignKey('Species', related_name="sp")
	lessons = models.ManyToManyField('Lessons', related_name="sounds")
	added_date = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return u'%s' % self.xenocanto_url

	class Meta:
		ordering = ('added_date',)


class Species(models.Model):
	eng_name = models.CharField(max_length=30, null=False)

	def __unicode__(self):
		return u'%s' % self.eng_name


class Playlists(models.Model):
	playlist_name = models.CharField(max_length=50)
	playlist_type = models.CharField(max_length=20)
	added_date = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return u'%s - %s' % (self.playlist_name, self.playlist_type)


class Annotations(models.Model):
	sound = models.ForeignKey('Sounds', related_name="annotations")
	user = models.ForeignKey('auth.User', related_name="annotations")
	wave_onset = models.FloatField()
	wave_offset = models.FloatField()
	spec_onset = models.FloatField()
	spec_offset= models.FloatField()
	species = models.CharField(max_length=100)
	added_date = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('added_date',)


class GroundTruth(models.Model):
	sound = models.ForeignKey('Sounds', related_name="anno")
	user = models.ForeignKey('auth.User', related_name="anno")
	wave_onset = models.FloatField()
	wave_offset = models.FloatField()
	spec_onset = models.FloatField()
	spec_offset= models.FloatField()
	species = models.ForeignKey('Species', related_name="species")
	added_date = models.DateTimeField(auto_now_add=True)
