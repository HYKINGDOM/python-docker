
# 使用官方提供的Python开发镜像作为基础镜像
FROM ubuntu:latest

# 将工作目录切换为/app
WORKDIR /app

# 将当前目录下的所有内容复制到/app下
ADD . /app

RUN apt-get update -y \
    && apt-get install -y python3-pip python-dev build-essential \
    && /usr/local/bin/python -m pip3 install --upgrade pip  \
    && pip3 install --trusted-host pypi.python.org -r requirements.txt

# 允许外界访问容器的80端口
EXPOSE 80

# 设置环境变量
ENV NAME World

# 设置容器进程为：python app.py，即：这个Python应用的启动命令
CMD ["python", "app.py"]