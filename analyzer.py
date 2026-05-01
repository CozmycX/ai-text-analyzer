def analyze_text(text):
    words = text.split()
    word_count = len(words)

    positive_words = ["good", "great", "excellent", "happy"]
    negative_words = ["bad", "sad", "angry", "terrible"]

    score = 0

    for word in words:
        if word.lower() in positive_words:
            score += 1
        elif word.lower() in negative_words:
            score -= 1

    print(f"Word Count: {word_count}")

    if score > 0:
        print("Sentiment: Positive 😊")
    elif score < 0:
        print("Sentiment: Negative 😡")
    else:
        print("Sentiment: Neutral 😐")

text = input("Enter text to analyze: ")
analyze_text(text)
