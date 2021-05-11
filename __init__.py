import re
import sys
import json
from os.path import dirname, join
from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler, intent_file_handler
from mycroft.messagebus.message import Message
from mycroft.skills.core import resting_screen_handler

class VaccineInfo(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('info.vaccine.intent')
    def handle_info_vaccine(self, message):
        self.speak_dialog('info.vaccine')


    @intent_file_handler('info.harvey.intent')
    def handle_info_harvey(self, message):
        self.speak_dialog('info.harvey')

    @intent_file_handler('info.bus.intent')
    def handle_info_harvey(self, message):
        self.gui.clear()
        self.enclosure.display_manager.remove_active()
        self.gui.show_image("qr.png", "Scan here to find bus schedules", "Scan here to find bus schedules")
        
        
def create_skill():
    return VaccineInfo()

