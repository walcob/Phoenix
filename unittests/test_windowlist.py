import sys
import imp_unittest, unittest
import wx
##import os; print 'PID:', os.getpid(); raw_input('Ready to start, press enter...')

#---------------------------------------------------------------------------

class WindowList(unittest.TestCase):
    def setUp(self):
        self.app = wx.App()
        self.frames = list()
        for i in range(5):
            frm = wx.Frame(None, title='frm%d' % i)
            self.frames.append( frm )
        for i in range(5):
            w = wx.Window(self.frames[4])

    def tearDown(self):
        def _closeAll():
            for frm in self.frames:
                frm.Close()
        wx.CallAfter(_closeAll)
        self.app.MainLoop()
        del self.app
            
        
    def test_WindowList_GetTLW1(self):    
        TLWs = wx.GetTopLevelWindows()
        self.assertTrue(len(TLWs) == 5)
        
    def test_WindowList_GetTLW2(self):    
        TLWs = wx.GetTopLevelWindows()        
        for tlw in TLWs:
            self.assertTrue(type(tlw) == wx.Frame)
            self.assertTrue(tlw.Title.startswith('frm'))
        
    def test_WindowList_GetChildren(self):
        children = self.frames[0].GetChildren()
        self.assertTrue(len(children) == 0)
        children = self.frames[4].GetChildren()
        self.assertTrue(len(children) == 5)
       
#---------------------------------------------------------------------------


if __name__ == '__main__':
    unittest.main()