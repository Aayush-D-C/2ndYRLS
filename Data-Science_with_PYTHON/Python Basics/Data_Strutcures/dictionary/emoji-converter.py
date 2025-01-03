emoji = {
    ":)": "😊",
    ":(": "☹️",
    ":D": "😄",
    ":P": "😛",
    ";)": "😉",
    ":o": "😮",
    ":O": "😮",
    ":|": "😐",
    ":'(": "😢",
    "XD": "😆",
    ":-*": "😘",
    ":<": "😠",
    ">:": "😠",
    ":/": "😕",
    ":3": "😺",
    ">:D": "😈",
    "<3": "❤️",
    "o/": "🙋‍♂️",
    "\\o": "🙋‍♀️",
    ":-|>": "🧙",
    "\\m/": "🤘",
    ":x": "🤐",
    ":z": "😴",
    "B-)": "😎",
    "o_O": "😳",
    "^_^": "😊",
    "-_-": "😑",
    ":v": "🐦",
    ":^)": "🤡",
    "*<|:-)": "🎅",
    "<(\")": "🐧",
    ":@"")": "🐷",
}

def beginning():
    print("Welcome to the Emoji Converter!")
    print("Feel free to use emoji symbols, and we will convert them for you! ^_^")
    print("Type 'exit' to quit.\n")

def emoji_converter():
    while True:
        text = input("> ")
        if text.lower() == "exit":
            print("Goodbye! 😊")
            break
        
        # Split the input text into words
        words = text.split(" ")
        output = ""
        
        # Convert each word to its emoji if found
        for word in words:
            output += emoji.get(word, word) + " "
        
        # Print the converted message
        print(output.strip())

# Start the program
beginning()
emoji_converter()
