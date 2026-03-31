import nltk
from nltk.tokenize import word_tokenize



try: #because you don't want to download it again and again :)
    nltk.data.find('tokenizers/punkt')  
except LookupError:
    nltk.download('punkt')
    
try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')


def preprocess_text(text):

    print("\n Original Text:")
    print(text)


    text = text.lower()
    print("\n Lowercased:")
    print(text)

    
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    
    cleaned_text = ""
    for char in text:
        if char not in punctuation:
            cleaned_text += char

    print("\n Without Punctuation:")
    print(cleaned_text)

    
    tokens = word_tokenize(cleaned_text)
    print("\n Tokens:")
    print(tokens)

    
    stopwords = [
        "is", "the", "in", "and", "a", "to", "of", "for", "on",
        "with", "as", "by", "at", "an", "be", "this", "that", "are",
        "was", "were", "it", "from", "or", "but", "not"
    ]

    filtered_tokens = []

    for word in tokens:
        if word not in stopwords:
            filtered_tokens.append(word)

    print("\n After Stopword Removal:")
    print(filtered_tokens)

    return filtered_tokens


text = input("Enter text: ")
preprocess_text(text)