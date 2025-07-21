# IELTS Score Backend

本项目为雅思作文自动评分后端，基于 FastAPI。

## 依赖安装

```bash
pip install -r requirements.txt
```

## 启动命令

```bash
uvicorn main:app --reload
```

## API 说明

- `POST /score`
    - 请求体：`{"text": "作文内容"}`
    - 返回：评分结果 JSON

## CORS 支持

已内置 CORS 支持，前端可直接跨域请求。 