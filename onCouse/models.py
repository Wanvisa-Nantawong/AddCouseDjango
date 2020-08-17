from django.db import models

# Create your models here.
ADDCOUSE_TYPES = [
    ('AV', 'AVAILABLE'),
    ('UV', 'UNAVAILABLE'),
]


class Student(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.code} - {self.name}'


class AddCouse(models.Model):
    class Meta:
        verbose_name_plural = "AddCouse"

    addCouse_name = models.CharField(max_length=255)
    addCouse_ID = models.CharField(max_length=2, choices=ACTIVITY_TYPES)
    teacher_name = models.TextField(max_length=255)
    teacher_Period = models.DateTimeField(max_length=255)  # วันที่สร้างกิจกรรมขึ้นมาในระบบ

    participant = models.ManyToManyField(Student,blank=True)


class AddCouseTimeline(models.Model):
    addCouse = models.ForeignKey(AddCouse, on_delete=models.CASCADE)
    addCouse_start = models.DateTimeField()
    addCouse_stop = models.DateTimeField(blank=True, null=True)
    addCouse_plantitle = models.CharField(max_length=255)
