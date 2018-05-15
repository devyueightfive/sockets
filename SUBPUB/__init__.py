class StopException(Exception):
    def __str__(self):
        super().__str__()
        return "Stop exception"
