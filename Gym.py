import kivy
import kivymd
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.recycleview import RecycleView
from kivymd.uix.label import MDLabel
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.card import MDCard
from kivymd.uix.list import OneLineAvatarIconListItem

kivy.require('1.9.0')

#Classes for screens
class GymLayout(PageLayout):
    pass

class FirstScreen(Screen):
    pass

class SecondScreen(Screen):
    pass

class ThirdScreen(Screen):
    pass

class LoginScreen(Screen):
    pass

class QuestionScreen(Screen):
    pass

class QuestionScreen2(Screen):
    pass

class SignupScreen(Screen):
    pass

class MainMenu(Screen):
    pass

class Live_TrainingScreen(Screen):
    pass

class EMSScreen(Screen):
    pass

class TrainerScreen(Screen):
    pass

class NutritionScreen(Screen):
    pass

class MuscleTarget(Screen):
    pass

#Class for news feeds
class MainWidget(RecycleView, Screen):
    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.data = [{'text': str(x)} for x in range(2)]

#Class for news feeds
class SecondaryWidget(RecycleView, Screen):
    def __init__(self, **kwargs):
        super(SecondaryWidget, self).__init__(**kwargs)
        self.data = [{'text': str(x)} for x in range(2)]

class ProfileScreen(Screen):
    pass

class ChatScreen(Screen):
    pass

#Screen Manager for screens
class GymLayoutApp(MDApp):
    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        #sm.add_widget(Builder.load_file("profile.kv"))
        sm.add_widget(FirstScreen(name='screen1'))
        sm.add_widget(SecondScreen(name='screen2'))
        sm.add_widget(ThirdScreen(name='screen3'))
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(QuestionScreen(name='QuestionScreen'))
        sm.add_widget(QuestionScreen2(name='QuestionScreen2'))
        sm.add_widget(SignupScreen(name='SignupScreen'))
        sm.add_widget(MainWidget(name='MainWidget'))
        sm.add_widget(SecondaryWidget(name='SecondaryWidget'))
        sm.add_widget(MuscleTarget(name='MuscleTarget'))
        sm.add_widget(MainMenu(name='MainMenu'))
        sm.add_widget(ChatScreen(name='ChatScreen'))
        sm.add_widget(Live_TrainingScreen(name='Live_TrainingScreen'))
        sm.add_widget(EMSScreen(name='EMSScreen'))
        sm.add_widget(TrainerScreen(name='TrainerScreen'))
        sm.add_widget(NutritionScreen(name='NutritionScreen'))
        
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"

        return sm

if __name__ == '__main__':

    GymLayoutApp().run()