import wx
import wx.richtext


class CipherPanel(wx.Panel):
    '''
        Displays 2 large text boxes and cipher options.

        If text is provided, the first text box will contain it.
    '''
    def __init__(self, parent, size, text=""):
        super().__init__(parent=parent, size=size)

        self.cipher = True

        self.SetBackgroundColour((20, 20, 25))
        font1 = wx.Font(14, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')
        font2 = wx.Font(12, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')
        font3 = wx.Font(10, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')
        bmp1 = wx.ArtProvider.GetBitmap(id=wx.ART_FLOPPY, client=wx.ART_OTHER, size=(20, 20))

        #  Panel elements
        self.input_text = wx.TextCtrl(parent=self, value=text, style=wx.TE_MULTILINE | wx.TE_RICH | wx.BORDER_SUNKEN)
        self.input_text.SetFont(font2)
        self.input_text.SetBackgroundColour(wx.Colour(12, 12, 17))
        self.input_text.SetForegroundColour(wx.Colour(255, 255, 255))
        self.output_text = wx.TextCtrl(parent=self, value=text, style=wx.TE_MULTILINE | wx.TE_RICH | wx.BORDER_SUNKEN | wx.TE_READONLY)
        self.output_text.SetFont(font2)
        self.output_text.SetBackgroundColour(wx.Colour(12, 12, 17))
        self.output_text.SetForegroundColour(wx.Colour(255, 255, 255))
        icon1 = wx.StaticBitmap(parent=self, id=wx.ID_ANY, bitmap=bmp1)
        input_operation_label = wx.StaticText(parent=self, id=wx.ID_ANY, label="Operation:")
        input_operation_label.SetFont(font1)
        input_operation_label.SetForegroundColour((255, 255, 255))
        icon2 = wx.StaticBitmap(parent=self, id=wx.ID_ANY, bitmap=bmp1)
        input_cipher_choice_label = wx.StaticText(parent=self, id=wx.ID_ANY, label="Cipher:")
        input_cipher_choice_label.SetFont(font1)
        input_cipher_choice_label.SetForegroundColour((255, 255, 255))
        input_key_label = wx.StaticText(parent=self, id=wx.ID_ANY, label="Key:")
        icon3 = wx.StaticBitmap(parent=self, id=wx.ID_ANY, bitmap=bmp1)
        input_key_label.SetFont(font1)
        input_key_label.SetForegroundColour((255, 255, 255))
        self.input_operation = wx.Choice(parent=self, choices=["Cipher", "Decipher"])
        self.input_operation.SetSelection(0)
        self.input_operation.SetFont(font2)
        self.input_cipher_choice = wx.Choice(parent=self, choices=["Caesar", "Vigenère"])
        self.input_cipher_choice.SetSelection(0)
        self.input_cipher_choice.SetFont(font2)
        self.input_key_caesar = wx.SpinCtrl(parent=self, id=1, value='3', min=1, max=27, style=wx.SP_ARROW_KEYS | wx.SP_WRAP)
        self.input_key_caesar.SetFont(font1)
        self.input_key_word = wx.TextCtrl(parent=self, id=2, value=text, style= wx.TE_RICH | wx.BORDER_NONE)
        self.input_key_word.SetValue("lemon")
        self.input_key_word.SetFont(font1)
        self.input_key_word.SetBackgroundColour(wx.Colour(12, 12, 17))
        self.input_key_word.SetForegroundColour(wx.Colour(255, 255, 255))
        cipher_button = wx.Button(parent=self, id=1, size=(150, -1), label="Apply")
        cipher_button.SetFont(font2)

        self.input_key_word.Hide()

        #  Binds
        self.input_cipher_choice.Bind(wx.EVT_CHOICE, self.setup_key_field)

        #  Panel Sizers
        input_operation_sizer = wx.BoxSizer(wx.HORIZONTAL)
        input_cipher_choice_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.input_key_sizer = wx.BoxSizer(wx.HORIZONTAL)
        options_sizer = wx.BoxSizer(wx.VERTICAL)
        horizontal_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.main_vertical_sizer = wx.BoxSizer(wx.VERTICAL)

        #  Sizer layout
        input_operation_sizer.Add(window=icon1, proportion=0)
        input_operation_sizer.AddSpacer(size=10)
        input_operation_sizer.Add(window=input_operation_label, proportion=0)
        input_operation_sizer.AddSpacer(size=10)
        input_operation_sizer.Add(window=self.input_operation, proportion=1, flag=wx.RIGHT, border=20)
        input_cipher_choice_sizer.Add(window=icon2, proportion=0)
        input_cipher_choice_sizer.AddSpacer(size=10)
        input_cipher_choice_sizer.Add(window=input_cipher_choice_label, proportion=0)
        input_cipher_choice_sizer.AddSpacer(size=10)
        input_cipher_choice_sizer.Add(window=self.input_cipher_choice, proportion=1, flag=wx.RIGHT, border=20)
        self.input_key_sizer.Add(window=icon3, proportion=0)
        self.input_key_sizer.AddSpacer(size=10)
        self.input_key_sizer.Add(window=input_key_label, proportion=0)
        self.input_key_sizer.AddSpacer(size=10)
        self.input_key_sizer.Add(window=self.input_key_caesar, proportion=1, flag=wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, border=20)
        options_sizer.Add(sizer=input_operation_sizer, proportion=0, flag=wx.UP | wx.BOTTOM | wx.EXPAND, border=10)
        options_sizer.Add(sizer=input_cipher_choice_sizer, proportion=0, flag=wx.UP | wx.BOTTOM | wx.EXPAND, border=10)
        options_sizer.Add(sizer=self.input_key_sizer, proportion=0, flag=wx.UP | wx.BOTTOM | wx.EXPAND, border=10)
        options_sizer.AddStretchSpacer()
        options_sizer.Add(cipher_button, proportion=0, flag=wx.UP | wx.BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, border=10)
        horizontal_sizer.Add(window=self.input_text, proportion=1, flag=wx.LEFT | wx.RIGHT | wx.EXPAND, border=10)
        horizontal_sizer.Add(window=self.output_text, proportion=1, flag=wx.LEFT | wx.RIGHT | wx.EXPAND, border=10)
        horizontal_sizer.Add(sizer=options_sizer, proportion=1, flag=wx.LEFT | wx.EXPAND, border=20)
        self.main_vertical_sizer.Add(sizer=horizontal_sizer, proportion=1, flag=wx.EXPAND)

        self.SetSizer(self.main_vertical_sizer)
        self.main_vertical_sizer.Fit(self)
        self.Layout()

    def get_operation(self):
        o = self.input_operation.GetSelection()
        if o == 0:
            return True
        elif o == 1:
            return False

    def get_cipher(self):
        return self.input_cipher_choice.GetStringSelection()

    def get_key(self):
        choice = self.input_cipher_choice.GetSelection()
        if choice == 0:
            return self.input_key_caesar.GetValue()
        elif choice == 1:
            return self.input_key_word.GetValue()
    
    def setup_key_field(self, event):
        choice = self.input_cipher_choice.GetSelection()

        if choice == 0:
            self.input_key_sizer.Hide(4)
            self.input_key_sizer.Detach(4)
            self.input_key_sizer.Insert(4, window=self.input_key_caesar, proportion=1, flag=wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, border=20)
            self.input_key_sizer.Show(4)
        elif choice == 1:
            self.input_key_sizer.Hide(4)
            self.input_key_sizer.Detach(4)
            self.input_key_sizer.Insert(4, window=self.input_key_word, proportion=1, flag=wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, border=20)
            self.input_key_sizer.Show(4)

        self.Layout()


class BarPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent, size=(-1, 25))
        self.SetMaxSize(wx.Size(-1, 25))
        self.SetBackgroundColour((15, 15, 20))
