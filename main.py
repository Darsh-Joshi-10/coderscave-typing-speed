#Typing Speed Checker

import time
import random

class TypingSpeedChecker:
    def __init__(self):
        self.word = self.get_sentence()
        self.input_text = ''
        self.start_time = 0

    def get_sentence(self):
        # Replace this with your sentences or a file containing sentences
        sentences = ["The quick brown fox jumps over the lazy dog",
                     "Python is an amazing programming language",
                     "Practice makes perfect"]
        sentence = random.choice(sentences)
        return sentence

    def calculate_speed(self):
        end_time = time.time()
        elapsed_time = end_time - self.start_time

        # Calculate speed in words per minute (WPM)
        words_typed = len(self.input_text.split())
        wpm = (words_typed / elapsed_time) * 60

        return wpm

    def start_test(self):
        print("Type the following sentence:")
        print(self.word)
        input("Press Enter when you're ready to start...")

        self.start_time = time.time()
        self.input_text = input("Start typing... ")

        # Calculate typing speed
        typing_speed = self.calculate_speed()
        print(f"\nYour typing speed: {typing_speed:.2f} words per minute")

if __name__ == "__main__":
    typing_test = TypingSpeedChecker()
    typing_test.start_test()
