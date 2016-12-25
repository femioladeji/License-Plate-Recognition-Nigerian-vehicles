"""
This is the GUI module, it is responsible for the frame display,
button actions and all GUI related functionalities
"""

import wx
import wx.xrc
import full


class frame_alpr (wx.Frame):

    def __init__(self, parent=None):
        """
        initializes the frame display
        """
        wx.Frame.__init__(self, parent, id = wx.ID_ANY, title=u"ALPR",
            pos=wx.DefaultPosition, size=wx.Size(800, 800),
            style=wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL)
        
        self.SetSizeHintsSz(wx.Size(800,800), wx.Size(800, 800))
        
        self.menubar = wx.MenuBar(0)
        self.menu_file = wx.Menu()
        self.menuitem_openfile = wx.MenuItem(self.menu_file, wx.ID_ANY,
            u"Open File", wx.EmptyString, wx.ITEM_NORMAL)
        self.menu_file.AppendItem(self.menuitem_openfile)

        self.menubar.Append(self.menu_file, u"File") 
        
        self.menu_about = wx.Menu()
        self.menubar.Append(self.menu_about, u"About") 
        
        self.SetMenuBar(self.menubar)
        
        fgSizer1 = wx.FlexGridSizer(2, 1, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        
        self.panel_main = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition,
            wx.Size(800, 450), wx.TAB_TRAVERSAL)
        self.panel_main.SetBackgroundColour(wx.Colour(255, 255, 255))
        
        gbSizer1 = wx.GridBagSizer(0, 0)
        gbSizer1.SetFlexibleDirection(wx.BOTH)
        gbSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        
        gbSizer1.SetMinSize(wx.Size(800, 450)) 
        self.text_filepathlabel = wx.StaticText(self.panel_main, wx.ID_ANY,
            u"File Path:", wx.DefaultPosition, wx.DefaultSize, 0)
        #self.text_filepathlabel.Wrap( -1 )
        self.text_filepathlabel.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(),
            70, 90, 92, False, wx.EmptyString))
        
        gbSizer1.Add(self.text_filepathlabel, wx.GBPosition(0, 0),
            wx.GBSpan(1, 1), wx.ALL, 5)
        
        self.text_filepath = wx.StaticText(self.panel_main, wx.ID_ANY,
            u"No image file choosen", wx.DefaultPosition, wx.DefaultSize, 0)
        self.text_filepath.Wrap(-1)
        gbSizer1.Add( self.text_filepath, wx.GBPosition(0, 1),
            wx.GBSpan(1, 1), wx.ALL, 5)
        
        self.panel_imagearea = wx.Panel(self.panel_main, wx.ID_ANY,
          wx.DefaultPosition, wx.Size(800, 330), wx.TAB_TRAVERSAL)
        self.bSizer3 = wx.BoxSizer(wx.VERTICAL)
        
        self.bSizer3.SetMinSize(wx.Size(800, 330))
        self.text_placeholder = wx.StaticText(self.panel_imagearea, wx.ID_ANY,
            u"No image to display", wx.DefaultPosition, wx.DefaultSize, 0)
        self.text_placeholder.Wrap(-1)
        self.text_placeholder.SetFont(wx.Font(16, 70, 90, 92, False,
            wx.EmptyString))

        self.bSizer3.Add(self.text_placeholder, 0, wx.ALIGN_CENTER|wx.ALL, 5)

        self.panel_imagearea.SetSizer(self.bSizer3)
        self.panel_imagearea.Layout()
        gbSizer1.Add(self.panel_imagearea, wx.GBPosition(1, 0),
            wx.GBSpan(1, 2), wx.EXPAND |wx.ALL, 5)

        fgSizer2 = wx.FlexGridSizer(0, 3, 0, 0)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED )

        self.btn_remove = wx.Button(self.panel_main, wx.ID_ANY,
            u"Remove Image", wx.DefaultPosition, wx.Size(-1,40), 0)

        fgSizer2.Add(self.btn_remove, 0, wx.ALL, 5)

        self.btn_execute = wx.Button(self.panel_main, wx.ID_ANY, u"Run ALPR",
            wx.DefaultPosition, wx.Size(-1, 40), 0)

        fgSizer2.Add(self.btn_execute, 0, wx.ALL, 5)

        self.btn_save = wx.Button(self.panel_main, wx.ID_ANY, u"Save",
            wx.DefaultPosition, wx.Size(-1, 40), 0)

        self.enable_or_disable_buttons([self.btn_save, self.btn_execute,
            self.btn_remove], False)

        fgSizer2.Add(self.btn_save, 0, wx.ALL, 5)

        gbSizer1.Add(fgSizer2, wx.GBPosition(2, 0), wx.GBSpan(1, 2),
            wx.ALIGN_CENTER, 5)

        self.panel_main.SetSizer(gbSizer1)
        self.panel_main.Layout()
        fgSizer1.Add(self.panel_main, 1, wx.EXPAND |wx.ALL, 5)

        self.panel_result = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition,
            wx.Size( 800,350 ), wx.TAB_TRAVERSAL)
        self.panel_result.SetBackgroundColour( wx.Colour(255, 255, 255))
        
        bSizer5 = wx.BoxSizer(wx.VERTICAL)
        
        bSizer5.SetMinSize(wx.Size(800, -1 )) 
        self.m_staticText7 = wx.StaticText(self.panel_result, wx.ID_ANY,
            u"PLATES IDENTIFIED", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)
        self.m_staticText7.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(),
            70, 90, 92, True, wx.EmptyString))
        
        bSizer5.Add(self.m_staticText7, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        
        self.listResult = wx.ListCtrl(self.panel_result, wx.ID_ANY,
            size=wx.Size(750, -1), style=wx.LC_REPORT|wx.BORDER_SUNKEN)
        self.listResult.InsertColumn(0, 'PLATE TEXT', width=100)
        self.listResult.InsertColumn(1, 'OWNER', width=200)
        self.listResult.InsertColumn(2, 'ISSUE DATE', width=100)
        self.listResult.InsertColumn(3, 'EXPIRY DATE', width=100)
        self.listResult.InsertColumn(4, 'CHASIS', width=100)
        self.listResult.InsertColumn(5, 'TYPE', width=100)
        bSizer5.Add(self.listResult, 1, wx.ALIGN_CENTER|wx.ALL, 5)
        
        self.panel_result.SetSizer( bSizer5 )
        self.panel_result.Layout()

        fgSizer1.Add(self.panel_result, 1, wx.EXPAND |wx.ALL, 5)
        
        
        self.SetSizer(fgSizer1)
        self.Layout()
        
        self.Centre(wx.BOTH)
        self.scrollwindow_action = wx.ScrolledWindow(self.panel_imagearea,
            wx.ID_ANY)
        self.scrollwindow_action.SetScrollbars(1, 1, 1, 1)
        self.scrollwindow_action.SetScrollRate(5, 5)
        self.scrollwindow_action.SetMinSize(wx.Size(800, 330))
        self.scrollwindow_action.SetMaxSize(wx.Size(800, 330))
        self.scrollwindow_action.Hide()
        self.bSizer3.Add(self.scrollwindow_action, 0, wx.ALL, 5)
        # Connect Events
        self.Bind(wx.EVT_MENU, self.open_image_menu,
            id = self.menuitem_openfile.GetId())
        self.btn_remove.Bind(wx.EVT_BUTTON, self.remove_image)
        self.btn_execute.Bind(wx.EVT_BUTTON, full.execute_ALPR)
        #the currentState is a property to check if the placeholder
        #text is showing or an image is showing
        #1 is the first state that indicates that the placeholder is showing
        self.currentState = 1
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def open_image_menu(self, event):
        """
        method to handle filedialog and ensure that only image files are
        selected and displays the filepath
        """
        wcard = "Image Files(*.jpg, *.jpeg, *.png, *.bmp)|*.jpg; *.jpeg; *.png; *.bmp"
        imgFileDialog = wx.FileDialog(None, 'Select An Image', wildcard=wcard)
        if imgFileDialog.ShowModal() == wx.ID_OK:
            self.imagepath = imgFileDialog.GetPath()
            full.imagepath = self.imagepath
            full.listResult = self.listResult
            self.text_filepath.SetLabel(self.imagepath)
            if self.currentState == 1:
                self.text_placeholder.Hide()
                self.showPreviewImage()
                self.currentState=2
                self.enable_or_disable_buttons([self.btn_remove,
                    self.btn_execute], True)
            else:
                self.previewImage.Destroy()
                self.showPreviewImage()

            
        event.Skip()
    
    def showPreviewImage(self):
        """
        previews the image selected by the user
        """
        bSizer_action = wx.BoxSizer(wx.VERTICAL)
        self.previewImage = wx.StaticBitmap(self.scrollwindow_action,
            wx.ID_ANY, wx.Bitmap(self.imagepath, wx.BITMAP_TYPE_ANY ),
            wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer_action.Add(self.previewImage, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        self.scrollwindow_action.SetSizer(bSizer_action)
        self.scrollwindow_action.Layout()
        bSizer_action.Fit(self.scrollwindow_action)
        self.scrollwindow_action.Show()

    def remove_image(self, event):
        """
        removes the selected image and resets the filepath textlabel
        """
        self.previewImage.Destroy()
        self.scrollwindow_action.Hide()
        self.text_placeholder.Show()
        self.text_filepath.SetLabel('No image file choosen')
        self.currentState = 1;
        self.enable_or_disable_buttons([self.btn_remove, self.btn_execute], False)

    def enable_or_disable_buttons(self, button_list, status):
        """
        enables or disables a button

        Parameters
        -----------
        button_list: List of the button identifiers
        status: Boolean; True for enable, False for disable
        """
        for eachBtn in button_list:
            eachBtn.Enable(status)
    