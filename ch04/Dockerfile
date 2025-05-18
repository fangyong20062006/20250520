FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 创建非 root 用户
RUN groupadd app && useradd -m -g app app

# 拷贝 requirements 并安装依赖（root 权限）
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 拷贝剩余代码并更改权限
COPY . .
RUN chown -R app:app /app

# 切换为非 root 用户
USER app

# 设置默认命令
CMD ["python3", "app.py"]
