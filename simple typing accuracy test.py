import time

# Sentence to type
sentence = "The quick brown fox jumps over the lazy dog"

print("Typing Accuracy Test")
print("Type the sentence below exactly as shown:")
print(sentence)
print()

input("Press Enter when you are ready...")

start_time = time.time()
typed_text = input("Start typing: ")
end_time = time.time()

# Calculate time taken
time_taken = end_time - start_time

# Calculate accuracy
correct_chars = 0
for i in range(min(len(sentence), len(typed_text))):
    if sentence[i] == typed_text[i]:
        correct_chars += 1

accuracy = (correct_chars / len(sentence)) * 100

# Words per minute (WPM)
words = len(typed_text.split())
wpm = (words / time_taken) * 60

print("\nResults:")
print(f"Time taken: {round(time_taken, 2)} seconds")
print(f"Accuracy: {round(accuracy, 2)}%")
print(f"Typing speed: {round(wpm, 2)} WPM")