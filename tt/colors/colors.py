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


def apply_color(ansicode_fore, str):
    return ansicode_fore + str + Fore.RESET


class Colorizer(object):
    def __init__(self, use_color):
        self.use_color = use_color

    def set_use_color(self, use_color):
        self.use_color = use_color

    def get_use_color(self):
        return self.use_color

    def red(self,str):
        if self.use_color:
            return apply_color(Fore.RED, str)
        else:
            return str

    def grey(self,str):
        if self.use_color:
            return apply_color(Fore.LIGHTBLACK_EX, str)
        else:
            return str

    def cyan(self, str):
        if self.use_color:
            return apply_color(Fore.CYAN, str)
        else:
            return str

    def green(self,str):
        if self.use_color:
            return apply_color(Fore.GREEN, str)
        else:
            return str

    def yellow(self,str):
        if self.use_color:
            return apply_color(Fore.YELLOW, str)
        else:
            return str

    def blue(self,str):
        if self.use_color:
            return apply_color(Fore.BLUE, str)
        else:
            return str

