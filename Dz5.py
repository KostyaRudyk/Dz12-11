
from colorama import init, Fore, Back, Style

init(autoreset=True)

attributes_and_methods = [attr for attr in dir(Fore) if not callable(getattr(Fore, attr))]
print("Атрибути та методи модуля Fore (колір тексту):")
for attr in attributes_and_methods:
    print(attr)

attributes_and_methods = [attr for attr in dir(Back) if not callable(getattr(Back, attr))]
print("\nАтрибути та методи модуля Back (колір фону):")
for attr in attributes_and_methods:
    print(attr)

attributes_and_methods = [attr for attr in dir(Style) if not callable(getattr(Style, attr))]
print("\nАтрибути та методи модуля Style (стиль тексту):")
for attr in attributes_and_methods:
    print(attr)
