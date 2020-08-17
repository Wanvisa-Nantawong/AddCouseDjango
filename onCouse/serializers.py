from .models import AddCouse, AddCouseTimeline, Student
from rest_framework import serializers


class AddCouseTimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddCouseTimeline
        fields = ['id',
                  'addCouse_name',
                  'teacher_name',
                  'teacher_Period']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'code', 'name']


class AddCouseSerializer(serializers.ModelSerializer):
    participant = StudentSerializer(many=True,required=False)
    addCousetimeline_set = AddCouseTimelineSerializer(many=True,required=False)

    class Meta:
        model = AddCouse
        fields = ['id',
                  'addCouse_name',
                  'teacher_name','teacher_Period',
                  'addCouse_ID','participant','addCousetimeline_set']
