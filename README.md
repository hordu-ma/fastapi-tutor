# FastAPI 教程项目

标准 `uv` 管理的 FastAPI 学习项目。

## 项目结构

```
.
├── src/fastapi_tutor/          # 源代码目录
│   ├── __init__.py
│   ├── main.py
│   ├── depend_inject.py        # 依赖注入示例
│   ├── enum_1.py               # 枚举示例
│   ├── query.py                # 查询参数示例
│   ├── shebang.py
│   └── walrus.py               # 海象运算符示例
├── tests/                      # 测试目录
├── pyproject.toml              # 项目配置（uv）
├── uv.lock                     # 依赖锁文件
└── README.md
```

## 快速开始

### 环境设置

```bash
# 安装 uv（如未安装）
curl -LsSf https://astral.sh/uv/install.sh | sh

# 创建虚拟环境并安装依赖
uv sync

# 激活虚拟环境
source .venv/bin/activate
```

### 运行应用

```bash
# 启动 FastAPI 服务器
uv run uvicorn fastapi_tutor.main:app --reload

# 或者直接运行
python -m uvicorn fastapi_tutor.main:app --reload
```

### 开发工作流

```bash
# 运行测试
uv run pytest

# 代码检查
uv run ruff check src/ tests/

# 类型检查
uv run mypy src/

# 自动格式化
uv run ruff format src/ tests/
```

## 依赖管理

### 添加新依赖

```bash
uv add package_name
uv add --group dev package_name  # 开发依赖
```

### 移除依赖

```bash
uv remove package_name
```

### 同步依赖

```bash
uv sync  # 安装所有依赖
uv sync --group dev  # 仅安装指定组
```

## 学习资源

- [FastAPI 官方文档](https://fastapi.tiangolo.com/)
- [Pydantic 文档](https://docs.pydantic.dev/)
- [uv 包管理器](https://docs.astral.sh/uv/)
