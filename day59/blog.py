import datetime
today = datetime.datetime.now()
class Blog:

    def __init__(self, id, title, subtitle, body):
        self.id = id
        self.title = title
        self.subtitle = subtitle
        self.body = body
        self.author = 'Aakash Kumar'
        self.date = f"{today.strftime('%B')} {today.day}, {today.year}" 