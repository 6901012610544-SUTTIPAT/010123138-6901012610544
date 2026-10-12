import tkinter as tk

#Function to count specific character occurrence in main text
def count_character():
    text = entry_text.get()
    char = entry_char.get()
    
    #Check if search character field is empty
    if not char:
        label_result.config(text="Result: Please enter a character to count.")
        return
        
    count = text.lower().count(char.lower())
    label_result.config(text=f"Result: Character '{char}' appears {count} time(s)")

#Function to count vowels (a, e, i, o, u) in main text
def count_vowels():
    text = entry_text.get()
    vowels = "aeiouAEIOU"
    
    #Calculate total count of vowels
    vowel_count = sum(1 for char in text if char in vowels)
    label_result.config(text=f"Result: Total Vowels = {vowel_count}")

#Function to check if main text is a palindrome
def check_palindrome():
    text = entry_text.get()
    
    #Clean text by removing spaces and converting to lowercase
    cleaned_text = "".join(text.split()).lower()
    
    #Check if input text is empty
    if not cleaned_text:
        label_result.config(text="Result: Please enter text to check.")
        return

    #Compare cleaned text with its reversed version
    if cleaned_text == cleaned_text[::-1]:
        label_result.config(text=f"Result: '{text}' is a Palindrome!")
    else:
        label_result.config(text=f"Result: '{text}' is NOT a Palindrome.")

#Create the main window
root = tk.Tk()
root.title("GUI Text Analyzer")
root.geometry("400x320")

#Label and Entry widget for main text input
label_text_input = tk.Label(root, text="Enter Text:")
label_text_input.pack(pady=(10, 2))

entry_text = tk.Entry(root, width=40)
entry_text.pack(pady=2)

#Label and Entry widget for search character input
label_char_input = tk.Label(root, text="Enter Character to Count:")
label_char_input.pack(pady=(10, 2))

entry_char = tk.Entry(root, width=10)
entry_char.pack(pady=2)

#"Count Character" button
btn_count_char = tk.Button(root, text="Count Character", command=count_character, width=20)
btn_count_char.pack(pady=5)

#"Count Vowels" button
btn_count_vowels = tk.Button(root, text="Count Vowels", command=count_vowels, width=20)
btn_count_vowels.pack(pady=5)

#"Check Palindrome" button
btn_check_palindrome = tk.Button(root, text="Check Palindrome", command=check_palindrome, width=20)
btn_check_palindrome.pack(pady=5)

#Label for displaying calculation results
label_result = tk.Label(root, text="Result: -", font=("Arial", 11, "bold"), fg="blue")
label_result.pack(pady=15)

#Start application event loop
root.mainloop()