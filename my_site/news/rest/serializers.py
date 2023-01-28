from rest_framework import serializers

from news.models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

        read_only = (
            'pk', 'created_at', 'update_at',
            # views
        )


