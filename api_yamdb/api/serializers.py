from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from reviews.models import Comment, Review, Title, User


class ReviewSerializer(serializers.ModelSerializer):
    title = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True,
    )
    author = serializers.SlugRelatedField(
        default=serializers.CurrentUserDefault(),
        slug_field='username',
        read_only=True
    )

    def validate(self, data):
        request = self.context['request']
        author = request.user
        title_id = self.context['view'].kwargs.get('title_id')
        title = get_object_or_404(Title, pk=title_id)
        if request.method == 'POST':
            if Review.objects.filter(title=title, author=author).exists():
                raise ValidationError(
                    'Вы не можете добавить более'
                    'одного отзыва на произведение'
                )
        return data

    class Meta:
        model = Review
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    review = serializers.SlugRelatedField(
        slug_field='text',
        read_only=True
    )
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Comment
        fields = '__all__'


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role'
        )
        model = User

    def validate(self, data):
        if 'role' in data and self.context['request'].user.role == 'user':
            data['role'] = 'user'
        return data


class UserSingUpSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('email', 'username')
        model = User

    def validate(self, data):
        if data['username'] == 'me':
            raise serializers.ValidationError(
                'Нельзя создавать пользователя с username = "me".'
            )
        return data


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('username', 'confirmation_code')
        extra_kwargs = {
            'username': {
                'validators': []
            }
        }
        model = User
