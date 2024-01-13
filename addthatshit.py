#python code study
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