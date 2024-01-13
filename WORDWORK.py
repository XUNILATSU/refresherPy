# PYTHON WORDWORK

def variable_word(word):
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	word = word.lower(); #Convers to lowercase 
	v_sum = sum(alphabet.index(char) + 1 for char in word if char.isalpha())
	return v_sum
	
def main():
	while True:
		user_input = input("Enter a word to add:" )
		result = variable_word(user_input)  #STRUGGLED WITH IDENTIFYING THE WORKING ORDER OF VARIABLE
		print(f"The sum of alphabet ranks for the input '{user_input}' is : {result} \n")
	
if __name__== "__main__":
	main()
    


def count_words(text):
    words = text.split()
    return len(words)

def main():
    while True:
        print("Word Counting Application")
        print("Enter your essay below. Press Enter twice to finish input.")

        essay_lines = []
        while True:
            line = input()
            if not line:
                break
            essay_lines.append(line)

        essay_text = ' '.join(essay_lines)
        word_count = count_words(essay_text)

        print("\nWord count: {}".format(word_count))

        another_round = input("Do you want to count words in another essay TYPE(yes/no)? ").lower()
        if another_round != 'yes':
            break
