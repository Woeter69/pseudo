import json

with open("old_english_dictionary.json") as f:
    old_eng_dict = json.load(f)


def convert_to_pseudo(text):
    words = text.split()
    result = []

    for word in words:
        key = word.lower().strip("!?,.")

        converted = old_eng_dict.get(key,word)

        if word[0].isupper():
            converted = converted.capitalize()
        
        result.append(converted)

    return " ".join(result)
