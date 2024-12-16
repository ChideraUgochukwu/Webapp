from django import forms
from .models import Topic, ChatRoom, Message

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class ChatRoomForm(forms.ModelForm):
    class Meta:
        model = ChatRoom
        fields = ['name', 'topic', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 2,
                'placeholder': 'Type your message here...',
                'class': 'form-control'
            }),
        }
        labels = {
            'content': '',
        }
