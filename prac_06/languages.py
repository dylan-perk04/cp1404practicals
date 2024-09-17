"""
CP1404 Practical - Client code to use the ProgrammingLanguage class.
Estimated time: 50 minutes
Actual time: 55 minutes
"""

from prac_06.programming_language import ProgrammingLanguage


def main():
    """Program to display a programming language's values using a Class."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)

    languages = [python, ruby, visual_basic]
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.language_name)


main()
