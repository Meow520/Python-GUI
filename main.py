from robottools import RobotTools
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window

from kivy.properties import StringProperty

from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

# Window sizeを決める
Window.size = (600, 250)
# 日本語扱えるように設定
resource_add_path('font')
LabelBase.register(DEFAULT_FONT, 'mplus-2c-regular.ttf')

rt = RobotTools(ip="", port=22222)

class TextWidget(Widget):
    text = StringProperty()
    
    def _init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)
        self.text = ''
        
    def start_idle(self):
    # アイドルモーションを開始する
        rt.play_idle_motion()

    def stop_idle(self):
        # アイドルモーションを終了する
        rt.stop_idle_motion()
    
    def reset_pose(self):
        # ポーズをリセットする
        servo_map = dict(HEAD_R=0, HEAD_P=-5, HEAD_Y=0, BODY_Y=0, 
                        L_SHOU=-90, L_ELBO=0, R_SHOU=90, R_ELBO=0)
        pose = dict(Msec=1000, ServoMap=servo_map)
        rt.play_pose(pose)

    def say_text(self, text:str):
        # 引数で与えた文字列を発話
        rt.say_text(text)
        
    def free_speak(self):
        # 引数で与えた文字列を発話
        self.text = self.ids["text_box"].text
        rt.say_text(self.text)

class RobotGUIApp(App):
    pass

if __name__ == "__main__":
    RobotGUIApp().run()