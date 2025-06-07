# Project_1 - v2
# Description: Script to read a file and print the number of occurences in the word.
f = "words.txt"
word_dict = {}

def read_words():
    words = []
    with open(f, "r") as file:
        for line in file:
            line = line.replace("\n", "")
            words.append(line)
    return words

# Function to write the words to the console in a sorted list
def write_file(words):
    for i, word in enumerate(sorted(words)):
        print(f"{i}.{word}")
    print()

# Function to count the occurrences of each word in the file and write them to a word.count file.
def count_words(words):
    word_dict = {}
    words = sorted(words)
    for word in words:
        word = word.lower().strip()
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    with open("word.count", "w") as file:
        for word, count in word_dict.items():
            file.write(f"{word}:{count}\n")
    print("Word count file created: word.count")

def main():
    words = read_words()
    write_file(words)
    count_words(words)

if __name__ == "__main__":
    main()

