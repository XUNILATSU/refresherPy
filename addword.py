def calculate_alphabet_sum(word):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    word = word.lower()  # Convert the word to lowercase for case-insensitivity
    alphabet_sum = sum(alphabet.index(char) + 1 for char in word if char.isalpha())
    return alphabet_sum

def main():
    while True:
        user_input = input("Enter a word or phrase: ")
        result = calculate_alphabet_sum(user_input)
        print(f"The sum of alphabet ranks for the input '{user_input}' is: {result} \n")

if __name__ == "__main__":
    main()