from flask import Flask
from flask import request
from flask import render_template  # 渲染
from fastHan import FastHan

app = Flask(__name__)
model=FastHan()


@app.route('/', methods = ['GET', 'POST'])  # 主页地址,“装饰器”
def content_words():
    #获取html方法为post的表单内容
    if request.method=="POST":
        #request.values.get("")获取html页面name为xx的内容
        item_content=request.values.get('item_text')
        answer=model(item_content,target="CWS")
    return render_template('index.html',answer=answer[0],item_content=item_content)  # 把index.html文件读进来，再交给浏览器
#额外声明xx=xx


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)  # 127.0.0.1 回路 自己返回自己

