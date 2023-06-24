import base64
from ai_apps import forms
from utils.base import BaseResponse
from django.shortcuts import render
import openai
from django.http import JsonResponse, StreamingHttpResponse, HttpResponse


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

def generate_stream_data(text):
    template = text

    # prompt = template.format(original_text=text)
    prompt = template
    chunks = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system",
                   "content": "you are my translate assistant and need to determine whether to translate my text into Chinese or English based on its content I give you.you need give me only the translation result and no more other words"},
                  {"role": "user", "content":
                      '''
                        Translate 
                        ##
                        {prompt}
                        ##
                        into English or Chinese
                      '''.format(prompt=prompt)},
                  ],
        temperature=0,
        stream=True)

    for chunk in chunks:
        # 得到delta的content，存在字典里面
        result = chunk.choices[0].get("delta", {}).get("content")
        finish_reason = chunk.choices[0].get("finish_reason")
        # 如果有需要，可以打印出来看看
        print(chunk)
        # print(type(chunk))  # openai的一个对象

        if result is not None:

            # 这里必须要encode，否则会报错，因为result是unicode编码，而sse只支持utf-8编码
            byte_str = result.encode('utf-8')
            # b64_str = base64.b64encode(byte_str).decode('utf-8')

            #print(type(result))  # 这里是bytes类型

            #print("result", result)
            #print(f"data: {byte_str}\n\n", type(f"data: {result}\n\n"))
            yield f"data: {byte_str}\n\n"
        if finish_reason == "stop":
            break
    yield 'data: \n\n'


def pack_trans_stream(request):
    # 当请求头stop为true时，停止推送数据
    stop = request.GET.get('stop')
    if stop == 'false':
        text = request.GET.get('text')
        stream_data = generate_stream_data(text)
        response = StreamingHttpResponse(stream_data, status=200, content_type='text/event-stream', charset='utf-8',
                                         )
        response['Cache-Control'] = 'no-cache'
        # 服务器端不缓存数据，nginx就不会缓存数据，这样就可以实时看到数据了
        response['X-Accel-Buffering'] = 'no'
        # print(response) # StreamingHttpResponse对象
        return response
    return HttpResponse('后台已经停止推送数据')
