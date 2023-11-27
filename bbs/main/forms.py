from django import forms
from django.forms import ModelForm
from .models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'author', 'theme', 'text', 'attached_file','status', 'passcode']

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)

        if 'instance' not in kwargs or kwargs['instance'] is None:
            self.fields['status'].widget = forms.HiddenInput()

        if 'user' in kwargs and kwargs['user'].is_staff:
            self.fields['status'].widget = forms.Select()
            self.fields['status'].queryset = Article.STATUS_CHOICES

    def validate_passcode(self):
        passcode = self.cleand_data['passcode']
        if not passcode:
            return passcode
        
        if not passcode.isdigit() or len(passcode) != 4:
            raise forms.ValidationError('4桁の半角数字を入力してください。')
        
        return passcode
