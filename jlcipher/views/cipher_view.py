import wx
import wx.richtext
from ..controllers.cipher_controller import CipherController


class CipherPanel(wx.Panel):
    """
    Panel that handles ciphers.
    """
    ciphers = ["Caesar", "Vigenère"]
    languages= ["English", "Bulgarian"]

    def __init__(self, parent, size, text=""):
        super().__init__(parent=parent, size=size)

        # Link controller
        self.cipher_controller = CipherController()

        # Customization
        # TODO make configurable
        self.SetBackgroundColour((20, 20, 25))

        #  Resources
        font1 = wx.Font(14, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')  # noqa: E501
        font2 = wx.Font(12, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')  # noqa: E501
        bmp_goforward = wx.ArtProvider.GetBitmap(id=wx.ART_GO_FORWARD, client=wx.ART_OTHER, size=(25, 20))  # noqa: E501
        icon_operation = wx.StaticBitmap(parent=self, id=wx.ID_ANY, bitmap=bmp_goforward)  # noqa: E501
        icon_cipher = wx.StaticBitmap(parent=self, id=wx.ID_ANY, bitmap=bmp_goforward)  # noqa: E501
        icon_key = wx.StaticBitmap(parent=self, id=wx.ID_ANY, bitmap=bmp_goforward)  # noqa: E501
        icon_language = wx.StaticBitmap(parent=self, id=wx.ID_ANY, bitmap=bmp_goforward)  # noqa: E501

        #  Panel elements
        self.input_text = wx.TextCtrl(parent=self, value=text, style=wx.TE_MULTILINE | wx.TE_RICH | wx.BORDER_SUNKEN)  # noqa: E501
        self.output_text = wx.TextCtrl(parent=self, value=text, style=wx.TE_MULTILINE | wx.TE_RICH | wx.BORDER_SUNKEN | wx.TE_READONLY)  # noqa: E501
    
        self.input_operation = wx.Choice(parent=self, choices=["Cipher", "Decipher"])  # noqa: E501
        input_operation_label = wx.StaticText(parent=self, id=wx.ID_ANY, label="Operation:")  # noqa: E501

        self.input_cipher_choice = wx.Choice(parent=self, choices=self.ciphers)  # noqa: E501
        input_cipher_choice_label = wx.StaticText(parent=self, id=wx.ID_ANY, label="Cipher:")  # noqa: E501

        self.input_key_caesar = wx.SpinCtrl(parent=self, id=wx.ID_ANY, value='3', min=1, max=917631, style=wx.SP_ARROW_KEYS | wx.SP_WRAP)  # noqa: E501
        self.input_key_word = wx.TextCtrl(parent=self, id=wx.ID_ANY, value=text, style=wx.TE_RICH | wx.BORDER_NONE)  # noqa: E501
        input_key_label = wx.StaticText(parent=self, id=wx.ID_ANY, label="Key:")  # noqa: E501

        self.input_language_choice = wx.Choice(parent=self, choices=self.languages)  # noqa: E501
        input_language_choice_label = wx.StaticText(parent=self, id=wx.ID_ANY, label="Language:")  # noqa: E501

        self.cipher_button = wx.Button(parent=self, id=wx.ID_ANY, size=(150, -1), label="Translate")  # noqa: E501

        # Panel Elements Configs
        self.input_text.SetFont(font2)
        self.input_text.SetBackgroundColour(wx.Colour(12, 12, 17))
        self.input_text.SetForegroundColour(wx.Colour(255, 255, 255))
        self.output_text.SetFont(font2)
        self.output_text.SetBackgroundColour(wx.Colour(12, 12, 17))
        self.output_text.SetForegroundColour(wx.Colour(255, 255, 255))
        self.output_text.SetValue("Currently only working with English.")

        self.input_operation.SetSelection(0)
        self.input_operation.SetFont(font2)
        input_operation_label.SetFont(font1)
        input_operation_label.SetForegroundColour((255, 255, 255))  # noqa: E501

        self.input_cipher_choice.SetSelection(0)
        self.input_cipher_choice.SetFont(font2)
        input_cipher_choice_label.SetFont(font1)
        input_cipher_choice_label.SetForegroundColour((255, 255, 255))

        self.input_key_caesar.SetFont(font1)
        self.input_key_word.SetValue("lemon")
        self.input_key_word.SetFont(font1)
        self.input_key_word.SetBackgroundColour(wx.Colour(12, 12, 17))
        self.input_key_word.SetForegroundColour(wx.Colour(255, 255, 255))
        self.input_key_word.Hide()
        input_key_label.SetFont(font1)
        input_key_label.SetForegroundColour((255, 255, 255))

        self.input_language_choice.SetSelection(0)
        self.input_language_choice.SetFont(font2)
        input_language_choice_label.SetFont(font1)
        input_language_choice_label.SetForegroundColour((255, 255, 255))

        self.cipher_button.SetFont(font2)

        #  Binds
        self.input_cipher_choice.Bind(wx.EVT_CHOICE, self.setup_key_field)
        self.cipher_button.Bind(wx.EVT_BUTTON, self.translate)

        #  Panel Sizers
        input_operation_sizer = wx.BoxSizer(wx.HORIZONTAL)
        input_cipher_choice_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.input_key_sizer = wx.BoxSizer(wx.HORIZONTAL)
        input_language_sizer = wx.BoxSizer(wx.HORIZONTAL)

        options_sizer = wx.BoxSizer(wx.VERTICAL)
        horizontal_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.main_vertical_sizer = wx.BoxSizer(wx.VERTICAL)

        #  Sizer Configs
        input_operation_sizer.Add(window=icon_operation, proportion=0)
        input_operation_sizer.AddSpacer(size=10)
        input_operation_sizer.Add(window=input_operation_label, proportion=0)
        input_operation_sizer.AddSpacer(size=10)
        input_operation_sizer.Add(window=self.input_operation, proportion=1, flag=wx.RIGHT, border=20)  # noqa: E501

        input_cipher_choice_sizer.Add(window=icon_cipher, proportion=0)
        input_cipher_choice_sizer.AddSpacer(size=10)
        input_cipher_choice_sizer.Add(window=input_cipher_choice_label, proportion=0)  # noqa: E501
        input_cipher_choice_sizer.AddSpacer(size=10)
        input_cipher_choice_sizer.Add(window=self.input_cipher_choice, proportion=1, flag=wx.RIGHT, border=20)  # noqa: E501

        self.input_key_sizer.Add(window=icon_key, proportion=0)
        self.input_key_sizer.AddSpacer(size=10)
        self.input_key_sizer.Add(window=input_key_label, proportion=0)
        self.input_key_sizer.AddSpacer(size=10)
        self.input_key_sizer.Add(window=self.input_key_caesar, proportion=1, flag=wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, border=20)  # noqa: E501
        
        input_language_sizer.Add(window=icon_language, proportion=0)
        input_language_sizer.AddSpacer(size=10)
        input_language_sizer.Add(window=input_language_choice_label, proportion=0)  # noqa: E501
        input_language_sizer.AddSpacer(size=10)
        input_language_sizer.Add(window=self.input_language_choice, proportion=1, flag=wx.RIGHT, border=20)
        
        options_sizer.Add(sizer=input_operation_sizer, proportion=0, flag=wx.UP | wx.BOTTOM | wx.EXPAND, border=10)  # noqa: E501
        options_sizer.Add(sizer=input_cipher_choice_sizer, proportion=0, flag=wx.UP | wx.BOTTOM | wx.EXPAND, border=10)  # noqa: E501
        options_sizer.Add(sizer=self.input_key_sizer, proportion=0, flag=wx.UP | wx.BOTTOM | wx.EXPAND, border=10)  # noqa: E501
        options_sizer.Add(sizer=input_language_sizer, proportion=0, flag=wx.UP | wx.BOTTOM | wx.EXPAND, border=10)  # noqa: E501
        options_sizer.AddStretchSpacer()
        options_sizer.Add(self.cipher_button, proportion=0, flag=wx.UP | wx.BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, border=10)  # noqa: E501
        
        horizontal_sizer.Add(window=self.input_text, proportion=1, flag=wx.LEFT | wx.RIGHT | wx.EXPAND, border=10)  # noqa: E501
        horizontal_sizer.Add(window=self.output_text, proportion=1, flag=wx.LEFT | wx.RIGHT | wx.EXPAND, border=10)  # noqa: E501
        horizontal_sizer.Add(sizer=options_sizer, proportion=1, flag=wx.LEFT | wx.EXPAND, border=20)  # noqa: E501
        
        self.main_vertical_sizer.Add(sizer=horizontal_sizer, proportion=1, flag=wx.EXPAND)  # noqa: E501

        self.SetSizer(self.main_vertical_sizer)
        self.main_vertical_sizer.Fit(self)
        self.Layout()

    def get_operation(self):
        o = self.input_operation.GetSelection()
        if o == 0:  # choice 1: Cipher
            return True
        elif o == 1:  # choice 2: Deipher
            return False

    def get_cipher(self):
        return self.input_cipher_choice.GetStringSelection()

    def get_key(self):
        choice = self.input_cipher_choice.GetSelection()
        if choice == 0:
            return self.input_key_caesar.GetValue()
        elif choice == 1:
            return self.input_key_word.GetValue()

    def get_language(self):
        return self.input_language_choice.GetStringSelection()

    def get_message(self):
        return self.input_text.GetValue()

    def setup_key_field(self, event):
        '''
        Change the key field to match the
        selected cipher's requirements.
        '''

        choice = self.input_cipher_choice.GetSelection()

        if choice == 0:  # Caesar Cipher Key (int)
            self.input_key_sizer.Hide(4)
            self.input_key_sizer.Detach(4)
            self.input_key_sizer.Insert(4, window=self.input_key_caesar, proportion=1, flag=wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, border=20)  # noqa: E501
            self.input_key_sizer.Show(4)
        elif choice == 1:  # Vigenere Cipher Key (string)
            self.input_key_sizer.Hide(4)
            self.input_key_sizer.Detach(4)
            self.input_key_sizer.Insert(4, window=self.input_key_word, proportion=1, flag=wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, border=20)  # noqa: E501
            self.input_key_sizer.Show(4)

        self.Layout()

    def translate(self, event):
        """
        Gets the text from the input TextCtrl,
        translates (ciphers or deciphers) it
        and writes it to the output TextCtrl.
        """

        # Harvest form
        text = self.get_message()
        if text is None:  # Do nothing if there's no text inputted
            return

        to_cipher = self.get_operation()  # boolean; True=cipher; False=decipher # noqa:E501
        cipher_which = self.get_cipher()
        key = self.get_key()
        language = self.get_language()

        # Instantiate the cipher
        try:
            self.cipher_controller.load(cipher_which, text, key, language)
        except(RuntimeError) as exc:
            if str(exc) == "Bad key":
                wx.MessageBox(
                    'This key is invalid.',
                    'Bad key',
                    wx.OK | wx.ICON_INFORMATION
                    )
            else:
                raise

        # Attempt translation (and write output if ok)
        try:
            output = self.cipher_controller.translate(to_cipher)
            self.output_text.SetValue(output)
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


class BarPanel(wx.Panel):
    """
    Serves as a configurable separator
     between panels (to be used with sizers).
    TODO make configurable (rgb?)
    """

    def __init__(self, parent):
        super().__init__(parent=parent, size=(-1, 25))
        self.SetMaxSize(wx.Size(-1, 25))
        self.SetBackgroundColour((15, 15, 20))
