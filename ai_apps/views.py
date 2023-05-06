import os
from time import sleep
import asyncio
import openai
from django.http import JsonResponse, StreamingHttpResponse
from django.shortcuts import render, HttpResponse
from . import forms
from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain
from langchain.callbacks.base import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


# 封装一个响应类
# 将数据封装到一个对象中，这样就可以在视图函数中直接返回对象，而不用再去构造响应体了
class BaseResponse(object):
    def __init__(self, status=False, detail=None, data=None):
        self.status = status
        self.detail = detail or {}
        self.data = data or {}

    @property
    def dict(self):
        return self.__dict__


from django.http import StreamingHttpResponse



def generate_stream_data(text):
    template = """
                            translate English to Chinese:
                            English: {original_text}
                            Chinese:
                            """

    prompt = template.format(original_text=text)
    chunks = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "you are a translator"},
                      {"role": "user", "content": prompt}
                      ],
            temperature=0,
            stream=True)

    for chunk in chunks:

        result = chunk.choices[0].get("delta", {}).get("content")
        finish_reason = chunk.choices[0].get("finish_reason")
        if result is not None:
            print(result)
            yield f"data: {result}\n\n"
        if finish_reason == "stop":
            break
    yield 'data: \n\n'


def pack_event_stream(request):
    # 当请求头stop为true时，停止推送数据
    stop = request.GET.get('stop')
    if stop == 'false':
        text = request.GET.get('text')
        stream_data = generate_stream_data(text)
        response = StreamingHttpResponse(stream_data, status=200, content_type='text/event-stream')
        response['Cache-Control'] = 'no-cache'
        # 服务器端不缓存数据，nginx就不会缓存数据，这样就可以实时看到数据了
        response['X-Accel-Buffering'] = 'no'
        return response
    return HttpResponse('后台已经停止推送数据')



def test_index(request):
    form = forms.TranslationForm()
    return render(request, 'test.html', {'form': form})


def index(request):
    return render(request, "index.html")


# Create your views here.
def translator(request):
    # 只是为了页面展示
    form = forms.TranslationForm()
    return render(request, "translator.html", {"form": form})


# def translate(request):
#
#     res = BaseResponse()
#     # print(request.POST)
#
#     text = request.POST.get('text')
#     # print(type(text))
#     # template里面的变量要注意空格
#     try:
#         template = """
#         translate English to Chinese:
#         English: {original_text}
#         Chinese:
#         """
#         prompt = PromptTemplate(template=template, input_variables=["original_text"])
#         llm = OpenAI(streaming=True,verbose=True, temperature=0)# 不写参数就是默认的，默认model_name = "text-davinci-003"
#         llm_chain = LLMChain(prompt=prompt, llm=llm,callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]))
#         original_text = text
#         result = llm_chain.run(original_text)
#         res.status = True
#         # res.date的值是一个字典，添加一个键值对，key是translation，value是result
#         res.data = {}
#         res.data["translation"] = result
#         print(result)
#     except Exception as e:
#         print(e)
#
#     return JsonResponse(res.dict, json_dumps_params={'ensure_ascii': False})

# 原生openai,使用completion，贵，不推荐

# def translate(request):
#
#     res = BaseResponse()
#     # print(request.POST)
#
#     text = request.POST.get('text')
#     # print(type(text))
#     # template里面的变量要注意空格
#     try:
#         template = """
#         translate English to Chinese:
#         English: {original_text}
#         Chinese:
#         """
#         prompt=template.format(original_text=text)
#         completion = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0)
#         result = completion.choices[0].text
#         res.status = True
#         # res.date的值是一个字典，添加一个键值对，key是translation，value是result
#         res.data = {}
#         res.data["translation"] = result
#         #print(completion)
#         #print(result)
#     except Exception as e:
#         print(e)
#
#     return JsonResponse(res.dict, json_dumps_params={'ensure_ascii': False})

# 原生openai,使用chatcompletion，便宜，推荐
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
        prompt = template.format(original_text=text)
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "you are a translator"},
                      {"role": "user", "content": prompt}
                      ],
            temperature=0,
            # stream=True,
        )
        result = chat_completion.choices[0].message.content
        ######这样可以取得token的使用情况
        # usage_completion = chat_completion.usage.completion_tokens
        # usage_prompt = chat_completion.usage.prompt_tokens
        # total_tokens = chat_completion.usage.total_tokens
        # print(usage_completion,usage_prompt,total_tokens)
        ######
        res.status = True
        # res.date的值是一个字典，添加一个键值对，key是translation，value是result
        res.data = {}
        res.data["translation"] = result
        # print(chat_completion)
        # print(result)
    except Exception as e:
        print(e)

    return JsonResponse(res.dict, json_dumps_params={'ensure_ascii': False})


def email_writer(request):
    # 只是为了页面展示
    emailWriterForm = forms.EmailWriterForm()

    return render(request, "email_writer.html", {"emailWriterForm": emailWriterForm})


def generate_email(request):
    res = BaseResponse()
    received_email = request.POST.get('received_email')
    include_info = request.POST.get('include_info')
    my_extra_requirement = request.POST.get('my_extra_requirement')
    try:
        template = """
            We received an email from a customer：{received_email},
            help me write a an email reply in English that includes this information: {include_info}? 
            Additionally, follow these conditions when writing the email: {my_extra_requirement}.
            """
        prompt = template.format(
            received_email=received_email,
            include_info=include_info,
            my_extra_requirement=my_extra_requirement
        )
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system",
                       "content": "You are a reliable AI email writing assistant who can help me write satisfying English emails based on my prompts."},
                      {"role": "user", "content": prompt}
                      ],
            temperature=0,
            # stream=True,
        )
        result = chat_completion.choices[0].message.content

        res.status = True
        res.data = {}
        res.data["my_response_email"] = result
    except Exception as e:
        print(e)

    return JsonResponse(res.dict, json_dumps_params={'ensure_ascii': False})
