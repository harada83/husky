from django.db import models



class Doctor(models.Model):
	name = models.CharField(max_length=64, blank=True, null=True, default=None)
	is_active = models.BooleanField(default=True)

	def __unicode__(self):
		return "%s" % self.name

	class Meta:
		verbose_name = "ФИО врача"
		verbose_name_plural = "ФИО врачей"



class Patient(models.Model):
    doctor = models.ForeignKey(Doctor, blank=True, null=True, default=None)
    name = models.CharField(max_length=128, blank=True, null=True, default=None)

    def __str__(self):
        return "Пациент %s %s" % (self.name, self.doctor,)

    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'