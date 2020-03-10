from colorama import Fore
import re


color_regex = re.compile("(\x9B|\x1B\\[)[0-?]*[ -\/]*[@-~]")


def strip_color(str):
    """Strip color from string."""
    return color_regex.sub("", str)


def len_color(str):
    """Compute how long the color escape sequences in the string are."""
    return len(str) - len(strip_color(str))


def ljust_with_color(str, n):
    """ljust string that might contain color."""
    return str.ljust(n + len_color(str))


class Colorizer(object):
    def __init__(self, use_color):
        self.use_color = use_color

    def set_use_color(self, use_color):
        self.use_color = use_color

    def get_use_color(self):
        return self.use_color

    def red(self,str):
        if self.use_color:
            return Fore.RED + str + Fore.RESET
        else:
            return str

    def green(self,str):
        if self.use_color:
            return Fore.GREEN + str + Fore.RESET
        else:
            return str

    def yellow(self,str):
        if self.use_color:
            return Fore.YELLOW + str + Fore.RESET
        else:
            return str

    def blue(self,str):
        if self.use_color:
            return Fore.BLUE + str + Fore.RESET
        else:
            return str
