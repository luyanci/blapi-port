import time
from bilibili_api import Credential,login_v2,sync
from bilibili_api.login_v2 import QrCodeLoginEvents
from bilibili_api.exceptions import LoginError

start = time.perf_counter()

def login_with_qrcode(root=None) -> Credential:
    """
    扫描二维码登录

    Args:
        root (tkinter.Tk | tkinter.Toplevel, optional): 根窗口，默认为 tkinter.Tk()，如果有需要可以换成 tkinter.Toplevel(). Defaults to None.

    Returns:
        Credential: 凭据
    """
    global start
    global photo
    global login_key, qrcode_image
    global credential
    global id_
    import tkinter
    import tkinter.font

    from PIL.ImageTk import PhotoImage

    if root == None:
        root = tkinter.Tk()
    root.title("扫码登录")
    qrcode = login_v2.QrCodeLogin()
    sync(qrcode.generate_qrcode())
    qrcode_image = qrcode.get_qrcode_picture().url.removeprefix("file://")
    photo = PhotoImage(file=qrcode_image)
    qrcode_label = tkinter.Label(root, image=photo, width=600, height=600)
    qrcode_label.pack()
    big_font = tkinter.font.Font(root, size=25)
    log = tkinter.Label(root, text="请扫描二维码↑", font=big_font, fg="red")
    log.pack()

    def update_events():
        global id_
        global start, credential, is_destroy, login_key
        events = sync(qrcode.check_state())
        if events == QrCodeLoginEvents.SCAN:
            log.configure(text="请扫描二维码↑", fg="red", font=big_font)
        elif events == QrCodeLoginEvents.CONF:
            log.configure(text="点下确认啊！", fg="orange", font=big_font)
        elif events == QrCodeLoginEvents.TIMEOUT:
            raise LoginError("二维码过期，请扫新二维码！")
        elif events == QrCodeLoginEvents.DONE:
            log.configure(text="成功！", fg="green", font=big_font)
            credential = qrcode.get_credential()
            root.after(1000, destroy)
            return 0
        id_ = root.after(500, update_events)
        if time.perf_counter() - start > 120:  # 刷新
            sync(qrcode.generate_qrcode())
            qrcode_image = qrcode.get_qrcode_picture().url.removeprefix("file://")
            photo = PhotoImage(file=qrcode_image)
            qrcode_label = tkinter.Label(root, image=photo, width=600, height=600)
            qrcode_label.pack()
            start = time.perf_counter()

        root.update()

    def destroy():
        global id_
        root.after_cancel(id_)  # type: ignore
        root.destroy()

    root.after(500, update_events)
    root.mainloop()
    root.after_cancel(id_)  # type: ignore
    return credential

if __name__ == '__main__':
    print(login_with_qrcode())