from .models import Quest, QComment
from rest_framework import serializers


class QCommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.email')

    class Meta:
        model = QComment
        fields = '__all__'
        read_only_fields = ['quest', 'user']


class QuestSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.email')
    qcomment = QCommentSerializer(many=True, read_only = True)

    class Meta:
        model = Quest
        fields = '__all__'
        read_only_fields = ['user', 'qcreated_at', 'qupdated_at','qcomment']