import openai
def mytest():

    for chunk in openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user",
            "content": "给我写一首10行的情书"
        }],
        stream=True,
    ):
        content = chunk["choices"][0].get("delta", {}).get("content")
        if content is not None:
            print(content, end='') # end='' is important，否则会换行，导致输出不连续，影响体验，这里的print是为了方便调试，实际应用中不需要
            # 如何在前段页面显示这个打字机的效果
            # 1. 用ajax轮询，每隔一段时间请求一次后端，后端返回一个字符串，前端拼接到页面上
            # 2. 用websocket，后端主动推送数据到前端
            # 3. 用sse，后端主动推送数据到前端



