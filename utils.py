import colorama
from colorama import Fore

colorama.just_fix_windows_console()
colorama.init()


def write(text, color=0):
	if color == 0:
		print(f"{Fore.GREEN}[+]{Fore.WHITE} {text}")
	elif color == 1:
		print(f"{Fore.YELLOW}[~]{Fore.WHITE} {text}")
	elif color == 2:
		print(f"{Fore.RED}[-]{Fore.WHITE} {text}")
	else:
		print(f"{Fore.WHITE}[#]{Fore.WHITE} {text}")