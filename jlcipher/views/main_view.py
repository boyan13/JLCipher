import wx
from . import cipher_view
from ..controllers.cipher_controller import CipherController


class MainApp(wx.App):
    #  The mode variable accounts for dimensions and other configurations.

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
        """
        Gets the text from the input TextCtrl,
         translates (ciphers or deciphers) it
         and writes it to the output TextCtrl.
        """

        # Step 1: Extract all data and pass it to
        # the controller so it can instantiate
        # the appropriate cipher class
        # (using the load() method)

        to_cipher = self.frame.cipher_panel.get_operation()  # boolean; True=cipher; False=decipher # noqa:E501
        cipher_which = self.frame.cipher_panel.get_cipher()
        key = self.frame.cipher_panel.get_key()
        text = self.frame.cipher_panel.input_text.GetValue()
        if text is None:  # Do nothing if there's no text inputted
            return
        try:
            self.cipher_controller.load(cipher_which, text, key)
        except(RuntimeError) as exc:
            if str(exc) == "Bad key":
                wx.MessageBox(
                    'This key is invalid.',
                    'Bad key',
                    wx.OK | wx.ICON_INFORMATION
                    )
            else:
                raise

        try:
            output = self.cipher_controller.translate(to_cipher)
            self.frame.cipher_panel.output_text.SetValue(output)
        except(RuntimeError) as exc:
            if str(exc) == "Bad key output":
                wx.MessageBox(
                    'Values produced by this key go outside of \
                    recognized Unicode bounds. This key is invalid.',
                    'Bad key.',
                    wx.OK | wx.ICON_INFORMATION
                    )
            else:
                raise


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
