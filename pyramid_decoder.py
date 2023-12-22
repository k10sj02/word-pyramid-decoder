def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()

    # Extracting relevant words and their corresponding numbers
    word_number_pairs = [line.split() for line in lines]
    relevant_numbers = [int(pair[0]) for pair in word_number_pairs]
    relevant_words = [pair[1] for pair in word_number_pairs if int(pair[0]) in relevant_numbers]

    # Constructing the pyramid of words
    pyramid = []
    start_index = 0

    for i in range(1, max(relevant_numbers) + 1):
        row = relevant_words[start_index:start_index + i]
        pyramid.append(row)
        start_index += i

    # Creating the final decoded string
    decoded_string = ' '.join([' '.join(row) for row in pyramid])
    return decoded_string

# Example usage:
message_file = 'file'
result = decode(message_file)
print(result)
