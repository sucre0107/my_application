from django import forms
from django.core.validators import RegexValidator

from ai_apps.utils.encrypt import md5


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        label_suffix="",  # 去掉label后面的冒号
        required=True,  # 校验不能为空
        # 添加正则表达式，要求含有英文字母和数字，且长度为6-12位
        widget=forms.TextInput(attrs={
            "class": "w-full px-3 py-2 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline",
            "placeholder": "用户名"}),
    )
    password = forms.CharField(
        label="Password",
        label_suffix="",  # 去掉label后面的冒号
        required=True,  # 校验不能为空
        # 添加正则表达式，要求含有英文字母,英文标点符号或者下划线和数字，且长度为6-12位
        widget=forms.PasswordInput(attrs={
            "class": "w-full px-3 py-2 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline",
            "placeholder": "密码"}, render_value=True),
    )  # render_value=True,即使我们输错密码，先前输入的密码仍然会显示在输入框中

    def clean_username(self):
        return self.cleaned_data.get('username')
    def clean_password(self):
        # 预先对密码进行加密，视图函数中的加密就可以省略了，这样就可以保证密码的一致性
        # 直接返回加密后的密码
        print(md5(self.cleaned_data.get('password')))
        return md5(self.cleaned_data.get('password'))



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
                                  widget=forms.Textarea(attrs={'class': 'cus-textarea'}))



class EmailWriterForm(forms.Form):
    # 用来接收用户输入的文本
    received_email = forms.CharField(label='我收到的邮件',
                           widget=forms.Textarea(attrs={'class': 'cus-textarea'}))

    #language = forms.ChoiceField(label='翻译成',
                                 # required=True,
                                 # choices=[('zh', '中文'), ('en', '英文'), ('ru', '俄文'), ('ko', '韩文')],
                                 # widget=forms.Select(attrs={'class': 'select select-bordered w-32'}))
    # 我对于ai助手帮我写的邮件的额外要求
    my_extra_requirement = forms.CharField(label='我对于ai助手帮我写的邮件的额外要求',
                                    initial="be polite",
                                    widget=forms.TextInput(attrs={'class': 'p-2.5 w-full text-xl text-gray-900 bg-gray-100 rounded-lg border border-gray-300 focus:ring-blue-500'}))
    include_info = forms.CharField(label='我想在回复中包含的信息',
                                    initial="",
                                    widget=forms.Textarea(attrs={'class': 'p-2.5 w-full h-20 text-xl text-gray-900 bg-gray-100 rounded-lg border border-gray-300 focus:ring-blue-500'}))
    # 用来接收翻译好的文本
    my_response_email = forms.CharField(label='我的回复',
                                  widget=forms.Textarea(attrs={'class': 'cus-textarea'}))


class CustomerServiceAssistantForm(forms.Form):
    # 用来接收用户输入的文本
    customer_message = forms.CharField(label='顾客的信息',
                           widget=forms.Textarea(attrs={'class': 'cus-textarea'}))

    #language = forms.ChoiceField(label='翻译成',
                                 # required=True,
                                 # choices=[('zh', '中文'), ('en', '英文'), ('ru', '俄文'), ('ko', '韩文')],
                                 # widget=forms.Select(attrs={'class': 'select select-bordered w-32'}))
    # 我对于ai助手帮我写的邮件的额外要求
    my_extra_requirement = forms.CharField(label='我回复时要注意的事项',
                                    initial="be polite",
                                    widget=forms.TextInput(attrs={'class': 'p-2.5 w-full text-xl text-gray-900 bg-gray-100 rounded-lg border border-gray-300 focus:ring-blue-500'}))
    include_info = forms.CharField(label='我想在回复中包含的信息',
                                    initial="",
                                    widget=forms.Textarea(attrs={'class': 'p-2.5 w-full h-20 text-xl text-gray-900 bg-gray-100 rounded-lg border border-gray-300 focus:ring-blue-500'}))
    # 用来接收翻译好的文本
    my_reply = forms.CharField(label='我的回复',
                                  widget=forms.Textarea(attrs={'class': 'cus-textarea'}))


