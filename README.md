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
