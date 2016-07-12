"""time needed for sleep, datetime needed to get current datetime"""
import random
import datetime

import dateutil.parser as parser
from questions import questions
from errbot import BotPlugin, botcmd

class CitizenshipTest(BotPlugin):  # pylint: disable=too-many-ancestors

    def idle_check(self):
        """Instance check for idle 24 hours"""
        start_min = datetime.date.today().isoformat() + "T14:00:00"
        start_max = datetime.date.today().isoformat() + "T22:00:00"
        # If time is between 4 and 4:01, run the function.
        if parser.parse(start_min) < datetime.datetime.now() < parser.parse(start_max) and datetime.date.weekday() < 5:
            self.quiz("<#C1MFBRH3L>")

    def quiz(self, channel):
        room = self.build_identifier(channel)

        num = random.random()
        if num <= .5:
            self.send(room, random.choice(questions))

    def activate(self):
        super().activate()
        self.start_poller(900, self.idle_check)

    @botcmd()
    def quizzer(self, msg, args):
        self.quiz("<#C1MFBRH3L>")