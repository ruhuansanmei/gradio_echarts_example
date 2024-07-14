
import gradio as gr
from gradio_mycomponent import MyComponent
import json

def transform_data(data, ratio):
    'transform data with ratio'
    '转换原始数据'
    obj =  json.loads(data)
    for serie in obj.get('series'):
        data = serie.get('data')
        if data != None:
            new_data = list(map(lambda x: x * ratio, data))
            serie['data'] = new_data
    return json.dumps(obj)


demo = gr.Interface(
    transform_data,
    inputs=[gr.Text(value=r'{"title":{"text":"ECharts示例,可按倍率调整数据(draw with ratio changed data)"},"tooltip":{},"xAxis":{"data":["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]},"yAxis":{},"series":[{"name":"销量","type":"bar","data":[5,20,36,10,10,20]}]}', label='原始数据(raw data)'),
             gr.Slider(value=2, minimum=1, maximum=10, step=1, label= "倍数(ratio)")],
    #   outputs =["text"],   # interactive version of your component
    outputs= MyComponent(),  # static version of your component
    # examples=[[example]],  # uncomment this line to view the "example version" of your component
    submit_btn= "绘图(draw)",
    clear_btn= "清除数据(clear)"
)


if __name__ == "__main__":
    demo.launch(server_name= '0.0.0.0')
