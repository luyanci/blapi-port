<div align="center">

# blapi-port

[仓库地址](https://github.com/luyanci/blapi-port)|[pypi](https://pypi.org/project/blapi-port)

 移植`bilibili-api-python` 在`17.0.0`后被**移除**的api

[![pdm-managed](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fpdm-project%2F.github%2Fbadge.json)](https://pdm-project.org)
[![PyPI](https://img.shields.io/pypi/v/blapi-port?logo=python&logoColor=%23cccccc)](https://pypi.org/project/blapi-port)

</div>

## 如何使用

```bash
> pip install blapi-port
```

然后`import`需要的模块即可

## 目前已移植内容

**所有展示的模块都要添加`_port`后缀以防import冲突**

 - `login`：登录模块
    - `login_with_qrcode`：扫描二维码登录（linux需要安装`python3-tkinter`）
    - `login_with_qrcode_term`： 终端扫码登录

可提issue补充/反馈Bug（当然自行移植/修复后PR更好）

## 引用代码

[`bilibili-api-python`](https://github.com/Nemo2011/bilibili-api)
