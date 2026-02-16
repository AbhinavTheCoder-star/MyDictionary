from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["My_Dictionary"]
collection = db["Dictionary_Collection"]

def getWord():
    return(input("Enter the word: ")).strip()

def getMeaning():
    return(input("Enter the meaning: ")).strip()

def getExample():
    return(input("Enter the Example Sentence: ")).strip()

def storeWord(word, meaning, example):
    document = {"word": word, "meaning": meaning, "example": example}
    collection.insert_one(document)

while True:
    choice = input("Would you like to add a word or search for a word? (1 or 2): ")
    if choice == "1":
        word = getWord()
        meaning = getMeaning()
        example = getExample()
        storeWord(word, meaning, example)
    elif choice == "2":
        word = getWord()
        result = collection.find_one({"word": word})
        if result:
            print(f"{result['word']} - {result['meaning']}")
            print(f"Example - {result['example']}")
        else:
            print("Word not found!")
