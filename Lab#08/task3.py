import re
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from nltk.corpus import words
import nltk
from difflib import get_close_matches

# Download the NLTK words corpus
nltk.download("words")

class SpellingChecker:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x500")
        self.root.title("Spelling Checker")

        # Scrolled Text for input
        self.text = ScrolledText(self.root, font=("Arial", 14))
        self.text.bind("<KeyRelease>", self.check)
        self.text.pack()

        # Label for suggestions
        self.suggestion_label = tk.Label(self.root, text="", font=("Arial", 12), fg="blue", wraplength=580, justify="left")
        self.suggestion_label.pack()

        self.old_spaces = 0
        self.root.mainloop()

    def check(self, event):
        content = self.text.get("1.0", tk.END)
        space_count = content.count(" ")

        if space_count != self.old_spaces:
            self.old_spaces = space_count

            # Remove existing tags
            for tag in self.text.tag_names():
                self.text.tag_delete(tag)

            # Clear suggestions
            self.suggestion_label.config(text="")

            misspelled_words = []

            # Check each word in the content
            for word in content.split():
                # Ignore numeric data
                if re.sub(r"[^\w]", "", word.lower()).isnumeric():
                    continue

                cleaned_word = re.sub(r"[^\w]", "", word.lower())

                if cleaned_word and cleaned_word not in words.words():
                    position = content.find(word)
                    self.text.tag_add(word, f"1.{position}", f"1.{position + len(word)}")
                    self.text.tag_config(word, foreground="red")

                    # Collect misspelled words for suggestions
                    misspelled_words.append(cleaned_word)

            # Generate suggestions for misspelled words
            suggestions_text = ""
            for misspelled_word in misspelled_words:
                suggestions = get_close_matches(misspelled_word, words.words(), n=3)
                if suggestions:
                    suggestions_text += f"Suggestions for '{misspelled_word}': {', '.join(suggestions)}\n"

            # Update suggestions label
            if suggestions_text:
                self.suggestion_label.config(text=suggestions_text)

# Initialize the spelling checker
SpellingChecker()
