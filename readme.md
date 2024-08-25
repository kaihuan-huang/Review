# V2-python

# 在项目目录中创建虚拟环境
`python -m venv env`

# 激活虚拟环境 (Windows)
`env\Scripts\activate`

# 激活虚拟环境 (macOS/Linux)
`source env/bin/activate`
安装所需包
`pip install streamlit prophet`

在虚拟环境中运行 streamlit 应用：

`streamlit run app.py`

 For better performance, install the Watchdog module:

  $ xcode-select --install
  $ pip install watchdog

open Docker app
构建 Docker 镜像：
`docker build -t finvision .`
运行 Docker 容器：
`docker run -p 8501:8501 finvision`