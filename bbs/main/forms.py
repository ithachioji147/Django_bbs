from django import forms
from django.forms import ModelForm
# from .models import Article
from .models import Article, Theme


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'author', 'theme', 'text', 'attached_file','status']

    theme = forms.ModelChoiceField(queryset=Theme.objects.all(), empty_label='テーマを選択して下さい')

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)

        if 'instance' not in kwargs or kwargs['instance'] is None:
            self.fields['status'].disabled = True


    # def cleand_data(self):  #  バリデーションチェック（調べ中）
    #     passcode = self.cleand_data['passcode']
    #     if not passcode:
    #         return passcode
        
    #     if not passcode.isdigit() or len(passcode) != 4:
    #         raise forms.ValidationError('4桁の半角数字を入力してください。')
        
    #     return passcode
