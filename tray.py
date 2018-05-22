import wx
import os

TRAY_TOOLTIP = 'My Torify'
TRAY_ICON = 'tor.png'

def create_menu_item(menu, label, func):
    item = wx.MenuItem(menu, -1, label)
    menu.Bind(wx.EVT_MENU, func, id=item.GetId())
    menu.AppendItem(item)
    return item

class TaskBarIcon(wx.TaskBarIcon):
    def __init__(self, frame):
        self.frame = frame
        super(TaskBarIcon, self).__init__()
        self.set_icon(TRAY_ICON)
        self.Bind(wx.EVT_TASKBAR_LEFT_DOWN, self.on_left_down)
        self.set_flag = False

    def CreatePopupMenu(self):
        menu = wx.Menu()
        create_menu_item(menu, 'Start/Stop torify', self.on_left_down)
        menu.AppendSeparator()
        create_menu_item(menu, 'About', self.on_hello)
        menu.AppendSeparator()
        create_menu_item(menu, 'Exit', self.on_exit)
        return menu

    def set_icon(self, path):
        icon = wx.IconFromBitmap(wx.Bitmap(path))
        self.SetIcon(icon, TRAY_TOOLTIP)

    def on_left_down(self, event):
        if(not self.set_flag):
            os.system("xterm -e \"sudo python toriptables2.py -l\"")
            self.set_flag = True
        else:
            os.system("xterm -e \"sudo python toriptables2.py -f\"")
            self.set_flag = False

    def on_hello(self, event):
        print "To-do"

    def on_exit(self, event):
        wx.CallAfter(self.Destroy)
        self.frame.Close()

class App(wx.App):
    def OnInit(self):
        frame=wx.Frame(None)
        self.SetTopWindow(frame)
        TaskBarIcon(frame)
        return True

def main():
    app = App(False)
    app.MainLoop()


if __name__ == '__main__':
    main()