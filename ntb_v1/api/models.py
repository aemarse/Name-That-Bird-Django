from django.db import models


class Sounds(models.Model):
	xenocanto_url = models.URLField(max_length=200)
	species_name = models.CharField(max_length=100)
	waveform_path = models.FilePathField(path=None)
	spectrogram_path = models.FilePathField(path=None)
	added_date = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('added_date',)


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
