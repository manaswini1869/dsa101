class Logger:

    def __init__(self):
        self.logger_timemap = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.logger_timemap.keys():
            time = self.logger_timemap[message]
            if timestamp >= time + 10:
                self.logger_timemap[message] = timestamp
                return True
            else:
                return False
        else:
            self.logger_timemap[message] = timestamp
            return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)