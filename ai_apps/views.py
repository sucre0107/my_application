import os
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from . import forms
from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain


# 封装一个响应类
# 将数据封装到一个对象中，这样就可以在视图函数中直接返回对象，而不用再去构造响应体了
class BaseResponse(object):
    def __init__(self, status=False, detail=None, data=None):
        self.status = status
        self.detail = detail
        self.data = data

    @property
    def dict(self):
        return self.__dict__


# Create your views here.
def translator(request):
    # 只是为了页面展示
    form = forms.TranslationForm()
    return render(request, "translator.html", {"form": form})


def translate(request):

    res = BaseResponse()
    # print(request.POST)

    text = request.POST.get('text')
    # print(type(text))
    # template里面的变量要注意空格
    try:
        template = """
        translate English to Chinese:
        English: {original_text}
        Chinese:
        """
        prompt = PromptTemplate(template=template, input_variables=["original_text"])
        llm = OpenAI(streaming=True) # 不写参数就是默认的，默认model_name = "text-davinci-003"
        llm_chain = LLMChain(prompt=prompt, llm=llm)
        original_text = text
        result = llm_chain.run(original_text)
        res.status = True
        # res.date的值是一个字典，添加一个键值对，key是translation，value是result
        res.data = {}
        res.data["translation"] = result
    except Exception as e:
        print(e)

    return JsonResponse(res.dict, json_dumps_params={'ensure_ascii': False})
