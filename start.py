import wx
from gui import frame_alpr
    
myALPR = wx.App()
guiFrame = frame_alpr(None)
guiFrame.Show()
myALPR.MainLoop()