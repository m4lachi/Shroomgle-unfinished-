from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.properties import StringProperty

kv_str = """
<BackgroundColor@Widget>
    background_color: 201,226,138
    canvas.before:
        Color:
            rgba: root.background_color
        Rectangle:
            size: self.size
            pos: self.pos
<BackgroundLabel@Label+BackgroundColor>
    background_color: 0, 0, 0, 0
MyScreenManager:
    BRANCH:
        name: 'Intro'
    S1:
        name: 'Mushroom'
    CRed:
        name: 'Red'
    CYellow:
        name: 'Yellow'
    CGreen:
        name: 'Green'
    CBlue:
        name: 'Blue'
    CPurple:
        name: 'Purple'
    CBlack:
        name: 'Black'
    CWhite:
        name: 'White'
    Danger:
        name: 'Danger'
    Safe:
        name:
    FINAL_SCREEN:
        id: final
        name: 'Restart'

<BRANCH>
    FloatLayout:
    Label:
        pos_hint: {'x': 0.00, 'y': 0.30}
        font_size: 45
        text: 'Welcome To Shroomgle'
        color: 1,1,1
    Button:
        text: 'Start'
        color: 1,1,1
        background_color: 0,1,0
        font_size: 30
        size_hint_x: 0.40
        size_hint_y: 0.20
        pos_hint: {'x': 0.0, 'y': 0.45}
        on_release:
            root.manager.transition.direction = 'left'
            root.manager.current = 'Mushroom'

<S1>:
    FloatLayout:
        Label:
            pos_hint: {'x': 0.02, 'y': 0.20}
            font_size: 35
            text: 'What Color Is The Mushroom?'
            color: 1,1,1
        Button:
            text: 'Red'
            color: 1,1,1
            font_size: 20
            size_hint_x: 0.15
            size_hint_y: 0.15
            pos_hint: {'x': 0.30, 'y': 0.45}
            on_release:
                root.manager.transition.direction = 'left'
                root.manager.current = 'Red'
                root.manager.ids.final.previous = root.name
        Button:
            text: 'Yellow'
            color: 1,1,1
            font_size: 20
            size_hint_x: 0.15
            size_hint_y: 0.15
            pos_hint: {'x': 0.45, 'y': 0.45}
            on_release:
                root.manager.transition.direction = 'left'
                root.manager.current = 'Yellow'
                root.manager.ids.final.previous = root.name
        Button:
            text: 'Green'
            color: 1,1,1
            font_size: 20
            size_hint_x: 0.15
            size_hint_y: 0.15
            pos_hint: {'x': 0.60, 'y': 0.45}
            on_release:
                root.manager.transition.direction = 'left'
                root.manager.current = 'Green'
                root.manager.ids.final.previous = root.name
        Button:
            text: 'Blue'
            color: 1,1,1
            font_size: 20
            size_hint_x: 0.15
            size_hint_y: 0.15
            pos_hint: {'x': 0.30, 'y': 0.30}
            on_release:
                root.manager.transition.direction = 'left'
                root.manager.current = 'Blue'
                root.manager.ids.final.previous = root.name
        Button:
            text: 'Purple'
            color: 1,1,1
            font_size: 20
            size_hint_x: 0.15
            size_hint_y: 0.15
            pos_hint: {'x': 0.45, 'y': 0.3}
            on_release:
                root.manager.transition.direction = 'left'
                root.manager.current = 'Purple'
                root.manager.ids.final.previous = root.name
        Button:
            text: 'Black'
            color: 1,1,1
            font_size: 20
            size_hint_x: 0.15
            size_hint_y: 0.15
            pos_hint: {'x': 0.6, 'y': 0.30}
            on_release:
                root.manager.transition.direction = 'left'
                root.manager.current = 'Black'
                root.manager.ids.final.previous = root.name
        Button:
            text: 'White'
            color: 1,1,1
            font_size: 20
            size_hint_x: 0.15
            size_hint_y: 0.15
            pos_hint: {'x': 0.45, 'y': 0.15}
            on_release:
                root.manager.transition.direction = 'left'
                root.manager.current = 'White'
                root.manager.ids.final.previous = root.name
        
        Button:
            text: 'Back'
            color: 1,1,1
            font_size: 20
            size_hint_x: 0.15
            size_hint_y: 0.15
            pos_hint: {'x': 0, 'y': 0}
            on_release:
                root.manager.transition.direction = 'right'
                root.manager.current = 'Intro'
                
        
<S2>:
    FloatLayout:
        Label:
            pos_hint: {'x': 0.00, 'y': 0.20}
            font_size: 35
            text: 'me este SCREEN-2'
            color: 1, 1, 1, 1
        Button:
            text: 'Onward'
            color: 1.0, 0.6, 0.0, 1
            font_size: 20
            size_hint_x: 0.20
            size_hint_y: 0.20
            pos_hint: {'x': 0.40, 'y': 0.15}
            on_release:
                root.manager.transition.direction = 'left'
                root.manager.current = 'Restart'
                root.manager.ids.final.previous = root.name
        Button:
            text: 'Back'
            color: 1.0, 0.6, 0.0, 1
            font_size: 20
            size_hint_x: 0.20
            size_hint_y: 0.20
            pos_hint: {'x': 0.60, 'y': 0.15}
            on_release:
                root.manager.transition.direction = 'right'
                root.manager.current = 'Intro'
<S3>:
    FloatLayout:
        Label:
            pos_hint: {'x': 0.00, 'y': 0.20}
            font_size: 35
            text: 'something SCREEN-3'
            color: 1, 1, 1, 1
        Button:
            text: 'Lets Go'
            color: 1.0, 0.6, 0.0, 1
            font_size: 20
            size_hint_x: 0.20
            size_hint_y: 0.20
            pos_hint: {'x': 0.40, 'y': 0.15}
            on_release:
                root.manager.transition.direction = 'left'
                root.manager.current = 'Restart'
                root.manager.ids.final.previous = root.name
        Button:
            text: 'Back'
            color: 1.0, 0.6, 0.0, 1
            font_size: 20
            size_hint_x: 0.20
            size_hint_y: 0.20
            pos_hint: {'x': 0.60, 'y': 0.15}
            on_release:
                root.manager.transition.direction = 'right'
                root.manager.current = 'Intro'
<S4>
    FloatLayout:
        Label:
            pos_hint: {'x': 0.00, 'y': 0.20}
            font_size: 35
            text: 'something SCREEN-3'
            color: 1, 1, 1, 1
        Button:
            text: 'Lets Go'
            color: 1.0, 0.6, 0.0, 1
            font_size: 20
            size_hint_x: 0.20
            size_hint_y: 0.20
            pos_hint: {'x': 0.40, 'y': 0.15}
            on_release:
                root.manager.transition.direction = 'left'
                root.manager.current = 'Restart'
                root.manager.ids.final.previous = root.name
        Button:
            text: 'Back'
            color: 1.0, 0.6, 0.0, 1
            font_size: 20
            size_hint_x: 0.20
            size_hint_y: 0.20
            pos_hint: {'x': 0.60, 'y': 0.15}
            on_release:
                root.manager.transition.direction = 'right'
                root.manager.current = 'Intro'
<FINAL_SCREEN>:
    FloatLayout:
        Label:
            pos_hint: {'x': 0.00, 'y': 0.20}
            font_size: 35
            text: 'Final Screen'
            color: 1, 1, 1, 1
        Button:
            text: 'Restart'
            color: 1.0, 0.6, 0.0, 1
            font_size: 20
            size_hint_x: 0.20
            size_hint_y: 0.20
            pos_hint: {'x': 0.40, 'y': 0.15}
            on_release:
                root.manager.transition.direction = 'right'
                root.manager.current = 'Intro'

"""

class MyScreenManager(ScreenManager):
    pass

class BRANCH(Screen):
    pass

class S1(Screen):
    pass

class S2(Screen):
    pass

class S3(Screen):
    pass

class S4(Screen):
    pass

class CRed(Screen):
    pass  
class CYellow(Screen):
    pass    
class CGreen(Screen):
    pass
class CBlue(Screen):
    pass    
class CPurple(Screen):
    pass
class CBlack(Screen):
    pass
class CWhite(Screen):
    pass
class FINAL_SCREEN(Screen):
    previous = StringProperty()

class MAINApp(App):
    def build(self):
        return Builder.load_string(kv_str)
    

if __name__ == '__main__':
    MAINApp().run()
