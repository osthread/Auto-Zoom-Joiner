from plyer import notification
import webbrowser, schedule, time

class AutoZoomJoin:
    def __init__(self):
        self.zoom_class_1 = "Zoom-Link Here" 
        self.zoom_class_2 = "Zoom-Link Here" 
        self.zoom_class_3 = "Zoom-Link Here" 
  
    def open_zoom(self, zoom_url):
        webbrowser.open(zoom_url)
        notification.notify(title='Auto Zoom Join', message=f'Opened Zoom at {time.strftime("%Y-%m-%d %H:%M:%S")}')

    def join_class(self, zoom_url):
        self.open_zoom(zoom_url)

    def schedule_classes(self):
        schedule.every().tuesday.at("13:02:00").do(self.join_class, self.zoom_class_1)
        schedule.every().thursday.at("13:05:00").do(self.join_class, self.zoom_class_2)
        schedule.every().monday.at("17:20:00").do(self.join_class, self.zoom_class_3)

    def run(self):
        self.schedule_classes()

        notification.notify(title='Auto Zoom Join', message='Zoom classes will be auto joined.')

        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    autojoin = AutoZoomJoin()
    autojoin.run()
