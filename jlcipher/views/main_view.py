import wx
from . import cipher_view
from ..controllers import cipher_controller


class MainApp(wx.App):
    def __init__(self, mode):
        self.mode = mode
        self.cipher_controller = cipher_controller.CipherController(cipher_or_decipher=True, cipher_which='Caesar', key=3)

        super().__init__()

    def OnInit(self):
        self.frame = MainFrame(parent=None, title="JLCipher: The Quick Cipher App", pos=(20, 20), mode=self.mode)
        self.frame.Show()

        self.Bind(wx.EVT_BUTTON, self.translate, id=1)

        return True

    def translate(self, event):
        operation = self.frame.cipher_panel.get_operation()
        cipher_which = self.frame.cipher_panel.get_cipher()
        key = self.frame.cipher_panel.get_key()

        text = self.frame.cipher_panel.input_text.GetValue()

        print("KEY: ", key)

        self.cipher_controller.set_operation(operation)
        self.cipher_controller.set_cipher(cipher_which)
        self.cipher_controller.set_key(key)

        self.cipher_controller.translate(text)


class MainFrame(wx.Frame):
    def __init__(self, parent, title, pos, mode):
        super().__init__(parent=parent, title=title, size=mode["WINDOW_SIZE"], pos=pos)

        self.SetMinSize(wx.Size(mode["MIN_WINDOW_SIZE"]))

        self.cipher_panel = cipher_view.CipherPanel(parent=self, size=mode["WINDOW_SIZE"])
        self.topbar_panel = cipher_view.BarPanel(parent=self)
        self.botbar_panel = cipher_view.BarPanel(parent=self)

        sz = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sz)

        sz.Add(window=self.topbar_panel, proportion=0, flag=wx.EXPAND)
        sz.Add(window=self.cipher_panel, proportion=1, flag=wx.EXPAND)
        sz.Add(window=self.botbar_panel, proportion=0, flag=wx.EXPAND)

        sz.Fit(self)
        self.Layout()
