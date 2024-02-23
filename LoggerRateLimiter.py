class Logger(object):

    def __init__(self):
        self.seen_messages = {}

    def shouldPrintMessage(self, timestamp, message):
        if message not in self.seen_messages:

            self.seen_messages[message] = timestamp
            return True

        # if the message is already there
        last_seen_timestamp = self.seen_messages[message]

        if timestamp - last_seen_timestamp>=10:

            self.seen_messages[message] = timestamp
            return True
        return False

