from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.uix.videoplayer import VideoPlayer
from kivymd.toast import toast
from kivymd.uix.gridlayout import MDGridLayout
from pytube import YouTube, streams
from kivy.properties import StringProperty, ListProperty, NumericProperty
import math
import os
import random
class Homer(Screen):
    pass
class StartupPage(Screen):
    pass
class HomeFrame(ScreenManager):
    pass
class VideoApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Amber"
        self.wid = Builder.load_file('appsto.kv')
        return self.wid
    def menu_call(self):
        pass
    def download_call(self):
         if True:
             self.url = self.root.get_screen('first').ids.box.text
             yt = YouTube(self.url)
             youtubeObject = yt.streams.get_highest_resolution()  
         else:
             toast("not valid URL!")
         try:
             toast('starting download.......!')
             sis = youtubeObject.download()
             toast('download finished')
             name = yt.title
             new = str(random.randrange(100000)) + ".mp4"
             namef = str(name)+'.mp4'
             os.rename(namef, new)
             os.replace(new, 'DCIM/'+new)
             toast('success')
         except:
             toast('some error')             
  
    def play_call(self, **kwargs):
        self.ml = StringProperty()
        if True:
            self.url = self.root.get_screen('first').ids.box.text
            yt = YouTube(self.url)
            self.img = yt.thumbnail_url
            self.root.get_screen('first').ids.imga.source= self.img
            self.ml = yt.streams.get_highest_resolution().filesize_mb
            self.lm = "SIZE : " + str(math.ceil(self.ml)) + "MB"
            self.root.get_screen('first').ids.size.text=self.lm 
        else:
            toast('invalid link!')
            
    def cancel_call(self, *args):
        self.root.get_screen('first').ids.box.text = ''
        self.root.get_screen('first').ids.imga.source =  'imgt/yt.png'
        self.root.get_screen('first').ids.size.text = ''
        
    def ttjk(self):
        toast("sorry!  not set futures")
           
        
if __name__ == "__main__":
    VideoApp().run()
    
    

