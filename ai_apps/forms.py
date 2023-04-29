from django import forms


class TranslationForm(forms.Form):
    # 用来接收用户输入的文本
    text = forms.CharField(label='原文',
                           # max_length=1000,
                           widget=forms.Textarea(attrs={'class': 'cus-textarea'}))

    # 用来接收用户选择的语言
    language = forms.ChoiceField(label='翻译成',
                                 required=True,
                                choices=[('zh', '中文'), ('en', '英文'), ('ru', '俄文'), ('ko', '韩文')],
                                widget=forms.Select(attrs={'class': 'select select-bordered w-32'}))

    # 用来接收翻译好的文本
    translation = forms.CharField(label='译文',
                                  # max_length=1000,
                                  widget=forms.Textarea(attrs={'class': 'cus-textarea'}))