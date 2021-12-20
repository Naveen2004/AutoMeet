import datetime as d
from os import system
import webbrowser
import sys


class AutoMeet(object):
    def __init__(self):

        self.sub = ("EN", "MA", "PH", "PY", "CH", "TT", "AP", "SS")

        self.timing = (
            ((8, 00), (8, 45)),
            ((8, 45), (9, 30)),
            ((9, 45), (10, 30)),
            ((10, 30), (11, 15)),
            ((11, 45), (12, 30)),
            ((12,30),(13,15))
        )

        self.time_table = (
            ("CH", "PH", "PY", "MA", "TT", "TT"),
            ("EN", "PY", "CH", "PH", "MA", "PH"),
            ("MA", "PH", "EN", "PY", "AP", "MA"),
            ("PY", "CH", "MA", "EN", "PH", "PY"),
            ("PH", "PY", "CH", "MA", "CH", "SS", "MA"),
        )
        self.codes = (
            "cxg-qntr-qqe",
            "bqz-bzpt-ncy",
            "xcs-obfq-rqo",
            "qee-aumx-vbh",
            "bfr-ammi-skf",
            "gzy-agha-emm",
            "gzy-agha-emm",
            "gzy-agha-emm",
        )

    def get_current_slot(self):
        self.slot = None

        current_time = d.datetime.now().hour, d.datetime.now().minute
        date = d.date(1, 1, 1)

        current_time = d.datetime.combine(
            date, d.time(hour=current_time[0], minute=current_time[1])
        )

        for duration in self.timing:
            s_time = d.time(hour=duration[0][0], minute=duration[0][1])
            e_time = d.time(hour=duration[1][0], minute=duration[1][1])

            s_time = d.datetime.combine(date, s_time)
            e_time = d.datetime.combine(date, e_time)

            if (
                current_time <= e_time
                and current_time >= s_time
            ):
                self.slot = self.timing.index(duration)
                break

        else:
            if not self.slot:
                self.slot = -1

    def get_current_class(self):
        self.get_current_slot()
        day = d.datetime.weekday(d.datetime.today())
        if day == 5 or day == 6:
            return "XX"
        if self.slot == -1:
            return "XX"
        else:
            return self.time_table[day][self.slot]

    def attend_class(self):
        if self.cls == "XX":
            print(
                "\n"
                + Fore.MAGENTA
                + "[*_*] "
                + Fore.YELLOW
                + "No Classes Now, Enjoy Yourself.."
            )
            return

        else:
            if self.cls in self.sub:
                webbrowser.open(
                    "https://meet.google.com/%s" % self.codes[self.sub.index(self.cls)]
                )

    def execute(self):
        self.cls = self.get_current_class()
        class_fullname = (
            "English",
            "Matrices And Calculus",
            "Engineering Physics",
            "Problem Solving And Python Programming",
            "Engineering Chemistry",
            "Technical Training",
            "Aptitude",
            "Soft Skills",
        )
        current_class_fullname = str()
        if self.cls in self.sub and self.cls != "XX":
            current_class_fullname = class_fullname[self.sub.index(self.cls)]

        if not current_class_fullname:
            print(
                "\n"
                + Fore.MAGENTA
                + "[*_*] "
                + Fore.YELLOW
                + "No Classes Now, Enjoy Yourself.."
            )
            return
        print(
            "\n"
            + Fore.BLUE
            + "[+] The current class is :  "
            + Fore.LIGHTCYAN_EX
            + Style.BRIGHT
            + current_class_fullname
            + Style.NORMAL
            + Fore.WHITE
        )
        inp = input(
            "\n"
            + Fore.MAGENTA
            + "[!] Do you want to proceed with current selection? (y/n/default=y) :  "
            + Fore.CYAN
        )
        if inp in ["y", "Y", ""]:
            self.attend_class()
            return
        elif inp in ["n", "N"]:
            for n in class_fullname:
                print(Fore.LIGHTGREEN_EX + f"[{class_fullname.index(n)+1}]  " + n)
            try:
                ch = int(
                    input(
                        "\n"
                        + Fore.MAGENTA
                        + "[+] Enter the number from the list to proceed: "
                        + Fore.CYAN
                    )
                )
                if ch in range(1, 9):
                    self.cls = self.sub[ch - 1]
                    self.attend_class()
            except ValueError:
                system(cls_cmd)
                self.execute()


if __name__ == "__main__":

    cls_cmd = (
        "cls"
        if sys.platform == "win32"
        else ("clear" if sys.platform == "linux" else "")
    )
    system(cls_cmd)
    try:
        from colorama import Fore, Style
    except ImportError:
        import subprocess

        subprocess.run("pip install colorama")
        system(cls_cmd)
        from colorama import Fore, Style

    title = r"""
    _         _        __  __           _
   / \  _   _| |_ ___ |  \/  | ___  ___| |_
  / _ \| | | | __/ _ \| |\/| |/ _ \/ _ \ __|
 / ___ \ |_| | || (_) | |  | |  __/  __/ |_
/_/   \_\__,_|\__\___/|_|  |_|\___|\___|\__|
"""
    
    print(Fore.LIGHTGREEN_EX+title+Fore.RESET)
    AutoMeet().execute()

    print(Fore.RESET)
