# blapi-port
 移植`bilibili-api-python` `v16.3.0` 中存在但在`v17.0.0`后被**移除**的api

## 目前已移植内容
 - `login`：登录模块
    - `login_with_qrcode`：扫描二维码登录（linux需要安装`python3-tkinter`）
    - `login_with_qrcode_term`： 终端扫码登录

可提issue补充（当然自行移植后PR更好）