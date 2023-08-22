class ChorusApiException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr("Erreur Chorus API: {}".format(str(self.msg)))
