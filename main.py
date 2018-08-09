from rtmbot import RtmBot
from rtmbot.core import Plugin
import chat_logic
import secret


class HelloPlugin(Plugin):
    def process_message(self, data):
        print(data)
        reply = chat_logic.answer(data["text"])
        if reply is not None:
            self.outputs.append([data["channel"], reply])

config = {
    "SLACK_TOKEN": secret.SLACK_TOKEN,
    "ACTIVE_PLUGINS": ["main.HelloPlugin"]
}
bot = RtmBot(config)
bot.start()
