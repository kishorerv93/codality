def solution(message, K):
	# lets make sure to run the algorithm only if message length exceeds K value
	if len(message) <= K:
		return message

	# For reference, we will keep a list of words from the original message
	initial_message_list = message.split(' ')

	# first we take the original message, and split by char count based on K value
	message = message[:K]

	# Break into words
	words = message.split(' ')

	# using the initial_message_list, we will check if the last word in processed list, is a complete word.
	# if it is a complete word, we return without changes, else we remove the last incomplete word.
	words = words[:-1] if words[-1] != initial_message_list[(len(words)-1)] else words

	# join all the words with space
	output = ' '.join(words)

	# return the processed message
	return(output)


if __name__ == '__main__':
	message = "codility we test coders and also the love"
	K = 27
	print(solution(message, K))
