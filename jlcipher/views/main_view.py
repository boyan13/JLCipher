import wx
from . import cipher_view
from ..controllers.cipher_controller import CipherController


class MainApp(wx.App):
    def __init__(self, mode):
        self.mode = mode
        self.cipher_controller = CipherController()

        super().__init__()

    def OnInit(self):
        self.frame = MainFrame(parent=None, title="JLCipher: The Quick Cipher App", pos=(20, 20), mode=self.mode)  # noqa: E501
        self.frame.Show()

        self.Bind(wx.EVT_BUTTON, self.translate, id=1)

        return True

    def translate(self, event):
        decipher = self.frame.cipher_panel.get_operation()  # boolean
        cipher_which = self.frame.cipher_panel.get_cipher()
        key = self.frame.cipher_panel.get_key()
        text = self.frame.cipher_panel.input_text.GetValue()

        self.cipher_controller.load(cipher_which, text, key)
        output = self.cipher_controller.translate(decipher)
        self.frame.cipher_panel.output_text.SetValue(output)


class MainFrame(wx.Frame):
    def __init__(self, parent, title, pos, mode):
        super().__init__(parent=parent, title=title, size=mode["WINDOW_SIZE"], pos=pos)  # noqa: E501

        self.SetMinSize(wx.Size(mode["MIN_WINDOW_SIZE"]))

        self.cipher_panel = cipher_view.CipherPanel(parent=self, size=mode["WINDOW_SIZE"])  # noqa: E501
        self.topbar_panel = cipher_view.BarPanel(parent=self)
        self.botbar_panel = cipher_view.BarPanel(parent=self)

        sz = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sz)

        sz.Add(window=self.topbar_panel, proportion=0, flag=wx.EXPAND)
        sz.Add(window=self.cipher_panel, proportion=1, flag=wx.EXPAND)
        sz.Add(window=self.botbar_panel, proportion=0, flag=wx.EXPAND)

        sz.Fit(self)
        self.Layout()
