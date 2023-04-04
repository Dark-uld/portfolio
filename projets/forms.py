from django.forms import ModelForm
from .models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        exclude = ('is_read',)

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        # self.fields['title'].widget.attrs.update({'class':'input', 'placeholder': 'Add title'})

        for name, field in self.fields.items() :
            field.widget.attrs.update({'class':'input'})