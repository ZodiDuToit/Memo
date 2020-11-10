from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock

import database

# screen manager
class WindowManager(ScreenManager):
    pass


# screens
class MainWindow(Screen):

    container = ObjectProperty(None)
    

    def on_enter(self):
        Clock.schedule_once(self.addTitleButtons)
    
    def changeCurrentScreen(self, screen, direction):
        self.manager.current = screen
        self.manager.transition.direction = direction

    def onTitleButtonRelease(self, instance):
        global currectMemosTitle

        currectMemosTitle = instance.text
        self.changeCurrentScreen("display", "right")

    def addbutton(self, text, on_release):
        self.container.add_widget(Button(text=text, on_release=on_release))

    def addTitleButtons(self, instance):
        self.container.clear_widgets()
        
        for title in database.retreiveAllTitles():
            self.addbutton(title, self.onTitleButtonRelease)  

    def getRandomTitle(self):
        return database.retreiveRandomTitle()

    def getRandomContent(self):
        return database.retreiveRandomContent()

class AddWindow(Screen): 

    help = ObjectProperty(None)
    title = ObjectProperty(None)
    content = ObjectProperty(None)

    def makeTitleContentGlobal(self):
        global editingTitle, editingContent

        editingTitle, editingContent = self.title, self.content

    def isFalidTitle(self):
        return len(self.title.text) >= 1

    def addHelpMessage(self, message):
        self.help.text = message


class EditingWindow(Screen):
    
    title = ObjectProperty(None)
    content = ObjectProperty(None)

    def on_enter(self):
        Clock.schedule_once(self.addTitleAndContent)

    def addTitleAndContent(self, instance):
        global editingTitle, editingContent

        editingTitle, editingContent = self.title, self.content
 
        self.content.text = str(database.retreive(currectMemosTitle))
        self.title.text = str(currectMemosTitle)    

        
class DisplayWindow(Screen):

    title = ObjectProperty(None)
    content = ObjectProperty(None)

    def on_enter(self):
        Clock.schedule_once(self.addTitleAndContent)

    def addTitleAndContent(self, instance):
        self.content.text = database.retreive(currectMemosTitle)
        self.title.text = currectMemosTitle

    def deleteMemo(self):
        database.delete(self.title.text)

  
# buttons
class ScrollViewButton(Button):
    pass

class OpenSaveMemoPopupButton(Button):
    def show_popup(self):

        popupWindow = SaveMemoPopup()
        popupWindow.open()


# popups
class SaveMemoPopup(Popup):

    def close(self):
        self.dismiss()

    def saveChanges(self):
        database.insert(editingTitle.text, editingContent.text)


class ColorLabel(Label):
    pass


kv = Builder.load_file("widgets.kv")

# app
class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()
