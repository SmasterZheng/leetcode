from flask import Flask
from flask import render_template # jinja2
from flask import redirect,url_for #访问首页自动跳转到url界面
from flask import request # 当中包含了所有请求的数据和头信息
import qrc




app=Flask(__name__) # 实例了对象
# 路由器分配网络
# 路由分配请求


@app.route('/') # 页面路径
def hello_world():
    return redirect(url_for('url'))



@app.route('/url',methods=['GET','POST'])
def url(): # 默认请求方式为GET
    # print(request.method)
    if request.method=='GET':
        return render_template('url.html')

    url = request.form['url']
    print(url)  # 获取前端form里的输入
    imgurl = qrc.url(url)
    return open(imgurl,'rb').read() # 图片的二进制信息

if __name__ == '__main__':
    app.run(debug=True) # flask 的debug默认关闭，但别的框架是启用的，测试环境使用，生产环境不行，因为会暴露代码
