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


class ChatBotForm(forms.Form):
    # 用户输入的文本
    user_input = forms.CharField(label='我说',
                                 initial="",
                                 widget=forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded focus:outline-none', 'placeholder':"来说点什么把...（Shift + Enter = 换行 ）"}))