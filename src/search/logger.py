class Logger:

    enabled: bool = False

    @staticmethod
    def log(msg: str):
        if (Logger.enabled):
            print(msg)