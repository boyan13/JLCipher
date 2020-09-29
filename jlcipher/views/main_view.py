import wx
from . import cipher_view


class MainApp(wx.App):
    #  The mode variable accounts for dimensions and other configurations.

    def __init__(self, mode):
        self.mode = mode

        super().__init__()

    def OnInit(self):
        self.frame = MainFrame(parent=None, title="JLCipher: The Quick Cipher App", pos=(20, 20), mode=self.mode)  # noqa: E501
        self.frame.Show()

        return True


class MainFrame(wx.Frame):
    """
    This is the only window that the app uses.
    """

    def __init__(self, parent, title, pos, mode):
        super().__init__(parent=parent, title=title, size=mode["WINDOW_SIZE"], pos=pos)  # noqa: E501

        self.SetMinSize(wx.Size(mode["MIN_WINDOW_SIZE"]))

        self.cipher_panel = cipher_view.CipherPanel(parent=self, size=mode["WINDOW_SIZE"])  # noqa: E501
        self.topbar_panel = cipher_view.BarPanel(parent=self)  # this is only decorative  # noqa: E501
        self.botbar_panel = cipher_view.BarPanel(parent=self)  # this is only decorative  # noqa: E501

        sz = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sz)

        sz.Add(window=self.topbar_panel, proportion=0, flag=wx.EXPAND)
        sz.Add(window=self.cipher_panel, proportion=1, flag=wx.EXPAND)
        sz.Add(window=self.botbar_panel, proportion=0, flag=wx.EXPAND)

        sz.Fit(self)
        self.Layout()
