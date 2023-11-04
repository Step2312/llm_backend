<h3 align="center">大模型后台</h3>


## 📝 目录

- [本项目](#about)
- [安装](#installation)
- [使用](#usage)

## 🧐 本项目 <a name = "about"></a>

这是一个大模型后台，用于生成中医健康养生建议数据。

## 🚀 安装库<a name = "installation"></a>

```
pip install flask
pip install flask-jwt-extended
pip install gunicorn
```

## 🎈 使用 <a name = "usage"></a>

1. 本地运行

   ```bash
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

2. 获取数据示例(test.ipynb)

   1. 用户认证(**第一步，必须先认证**)

      ```python
      import requests
      url = 'http://10.120.53.47:5000/login'
      data = {'username': 'njucm', 'password': 'njucm'}
      response = requests.post(url, json=data)
      access_token = response.json()['access_token']
      ```

    2. 获取数据示例代码

        ````python
         url = 'http://10.120.53.47:5000/wd'
         headers = {'Authorization': 'Bearer {}'.format(access_token)}
         json = {'question': '我压力很大，怎么办？'}
         response = requests.post(url, headers=headers, json=json)
         response.json()
        ````
        ```python
         url = 'http://10.120.53.47:5000/zx'
         headers = {'Authorization': 'Bearer {}'.format(access_token)}
         json = {
            'name':'张三',
            'gender':'男',
            'age':'20',
            'disease':'高血压 糖尿病',
            'question':'我压力很大，怎么办？'
         }
         response = requests.post(url, headers=headers)
         response.json()
        ```


