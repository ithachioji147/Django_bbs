from django import forms
from django.forms import ModelForm
from .models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        # fields = ['title', 'author', 'theme', 'text', 'attached_file','status', 'passcode']  # パスワード機能作成後こちら
        fields = ['title', 'author', 'theme', 'text', 'attached_file','status']

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)

        if 'instance' not in kwargs or kwargs['instance'] is None:
            self.fields['status'].disabled = True


        # if 'user' in kwargs and kwargs['user'].is_staff:  # models側で指定しているので不要では？
        #     self.fields['status'].widget = forms.Select()
        #     self.fields['status'].queryset = Article.STATUS_CHOICES

    # def cleand_data(self):  #  バリデーションチェック（調べ中）
    #     passcode = self.cleand_data['passcode']
    #     if not passcode:
    #         return passcode
        
    #     if not passcode.isdigit() or len(passcode) != 4:
    #         raise forms.ValidationError('4桁の半角数字を入力してください。')
        
    #     return passcode
