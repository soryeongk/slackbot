from rtmbot import RtmBot
from rtmbot.core import Plugin

import chat_logic
import secret


class HelloPlugin(Plugin):
    def process_message(self, data):
        text = data["text"]
        if not text.startswith('소령 '):
            return

        # print(data)
        reply = chat_logic.answer(text[3:])
        if reply is not None:
            self.outputs.append([data["channel"], ':dait_happy: : ' + reply])

config = {
    "SLACK_TOKEN": secret.SLACK_TOKEN,
    "ACTIVE_PLUGINS": ["main.HelloPlugin"]
}
bot = RtmBot(config)
bot.start()
