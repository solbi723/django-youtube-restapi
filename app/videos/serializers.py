from rest_framework import serializers
from .models import Video
from users.serializers import UserInfoSerializer
from reactions.models import Reaction

class VideoListSerializer(serializers.ModelSerializer):
    # Video:User => Video(FK) -> User
    user = UserInfoSerializer(read_only=True) # Video(FK)

    class Meta:
        model = Video
        fields = "__all__"
        # depth = 1



from comments.serializers import CommentSerializer

class VideoDetailSerializer(serializers.ModelSerializer):
    user = UserInfoSerializer(read_only=True) # Video(FK)

    comment_set = CommentSerializer(many=True, read_only=True)

    reactions = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = "__all__"
       

    def get_reactions(self, video):
        return Reaction.get_video_reactions(video) # 비디오 줄게 -> 리액션 내놔.


# docker-compose run --rm app sh -c 'python manage.py makemigrations'
# docker-compose run --rm app sh -c 'python manage.py migrate'
    
# 여기서 질문! 어드민으로 해서 좋아요 카운트를 올려봤는데 like_count가 안들어가네요.. ;;