import rumps
import webbrowser
import subprocess
import getpass
import pyperclip
import datetime


class Cobanov(rumps.App):
    def __init__(self):
        super(Cobanov, self).__init__("Cobanov", title="🦊")
        self.menu = [
            rumps.MenuItem(title="Clipboard", icon="assets/clipboard.png"),
            rumps.MenuItem(title="Desktop", icon="assets/desktop.png"),
            rumps.MenuItem(title="Youtube", icon="./assets/youtube.png"),
            rumps.MenuItem(title="Gmail", icon="assets/gmail.png"),
            rumps.MenuItem(title="Cobanov", icon="assets/fox.png"),
            rumps.MenuItem(title="Screenshot", icon="assets/gmail.png"),
        ]
        self.path = f"/Users/{getpass.getuser()}/Documents/clipboards"

    @ rumps.clicked("Clipboard")
    def clipboard(self, _):

        NOW = datetime.datetime.now()

        with open(f"{self.path}/clipboards.txt", "a") as file:
            clip = pyperclip.paste()
            file.write(f"\n[{NOW}]\n{clip}\n")
        rumps.notification(
            title="Kopyalandı", subtitle="Documents altından ulaşabilirsin!", message=clip[:100])
        self.title = "Copied!"

    @ rumps.clicked("Desktop")
    def prefs(self, _):
        subprocess.call(["open", f"/Users/{getpass.getuser()}/Desktop"])
        self.title = "Desktop!"

    @ rumps.clicked("Youtube")
    def youtube(self, _):
        webbrowser.open('https://youtube.com/', new=2)

    @ rumps.clicked("Gmail")
    def gmail(self, _):
        webbrowser.open('https://mail.google.com/', new=2)

    @ rumps.clicked("Cobanov")
    def love(self, _):
        rumps.alert(title="Cobanov", message="Cobanov seni seviyor!",
                    icon_path="./assets/fox.png")

    @ rumps.clicked("Screenshot")
    def screenshot(self, _):
        subprocess.call(["screencapture", f"{self.path}/screenshot.jpg"])

    def refresh_status(self):
        self.title = "🦊"

    @ rumps.timer(5)
    def deneme(self, sender):
        self.refresh_status()


if __name__ == "__main__":
    Cobanov().run()
