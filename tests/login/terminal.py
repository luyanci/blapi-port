import sys
import time
from bilibili_api import Credential,login_v2,sync
from bilibili_api.login_v2 import QrCodeLoginEvents

def login_with_qrcode_term() -> Credential:
    """
    终端扫描二维码登录

    Args:

    Returns:
        Credential: 凭据
    """
    
    qrcode =login_v2.QrCodeLogin()
    sync(qrcode.generate_qrcode())
    print(qrcode.get_qrcode_terminal() + "\n")
    while True:
        result = sync(qrcode.check_state())
        if result == QrCodeLoginEvents.SCAN:
            sys.stdout.write("\r 请扫描二维码↑")
            sys.stdout.flush()
        elif result == QrCodeLoginEvents.CONF:
            sys.stdout.write("\r 点下确认啊！")
            sys.stdout.flush()
        elif result == QrCodeLoginEvents.TIMEOUT:
            print("二维码过期，请扫新二维码！")
            sync(qrcode.generate_qrcode())
            print(qrcode.get_qrcode_terminal() + "\n")
        elif result == QrCodeLoginEvents.DONE:
            sys.stdout.write("\r 成功！")
            sys.stdout.flush()
            return qrcode.get_credential()
        time.sleep(1)
    
