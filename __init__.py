from mycroft import MycroftSkill, intent_file_handler


class VaccineInfo(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('info.vaccine.intent')
    def handle_info_vaccine(self, message):
        self.speak_dialog('info.vaccine')


def create_skill():
    return VaccineInfo()

