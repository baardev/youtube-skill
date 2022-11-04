from mycroft import MycroftSkill, intent_handler


class Youtube(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler('youtube.intent')
    def handle_youtube(self, message):
        self.speak_dialog('youtube')


def create_skill():
    return Youtube()

