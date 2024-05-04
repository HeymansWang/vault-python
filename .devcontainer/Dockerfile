FROM python:3.9.19-bullseye

RUN sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list

# 安装依赖
RUN apt-get update
RUN apt-get install -y vim git zip unzip python3-pip
RUN pip3 install --upgrade pip

RUN apt-get clean 

# 创建 pip 镜像 
RUN pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple  

# 配置 datetime
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# 安装 sudo 
RUN apt-get install -y sudo

# 配置 sudo
RUN echo "vscode ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# 指定 user
RUN useradd -ms /bin/bash vscode
USER vscode

# 配置用户的 PATH 环境变量
RUN touch /home/vscode/.bash_aliases
RUN echo 'export PATH="$HOME/.local/bin:$PATH"' > /home/vscode/.bash_aliases

WORKDIR /workspaces 
