# Word Pyramid Decoder

The "Pyramid Decoder" is a Python script designed to decode messages represented as pyramids of words. Given a file containing numeric pairs and corresponding words, the script extracts relevant words and constructs a pyramid structure. The decoding process involves arranging words into rows based on the numeric sequence and then joining them to form the final decoded message. This versatile tool can be applied to various word-based encoding schemes, providing a flexible solution for decoding messages organized in a pyramid format.

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
message_file = '.../coding_qual_input.txt'
result = decode(message_file)
print(result)

land sun too huge dont such noun student brown complete play cook yard clock would plain excite fire wish cool child past colony oil dog back money kind open finger touch are dad am modern meant ocean pitch suit town east over group good kind down band especially organ of fire out area touch happen sat electric wrote buy lot stop corn where check live best hold cause grand present indicate slave we like visit state morning true are ball history seat rain less glass tone song fair element speed produce quotient sand begin moment offer probable all necessary post cent happen speech object silver third crease wait triangle idea clothe young discuss field company capital compare chart possible written remember mile cold lady felt against skin prepare he card organ object our major discuss system hole above they produce straight level though modern dry bought milk make show middle center blood speak prove select power come brown experiment strong hurry touch reach case beat over dry hill company opposite work field felt prepare now his stay toward observe time stop possible card prepare current compare neighbor thus include copy bit stead does general solve glad duck offer happen ball bread like machine come any band it section close heavy produce got possible insect way before men bird ease trade winter am repeat first to each guide column single remember wild major coast class done jump sister feel check fire nine indicate parent whole her the temperature design big skill friend hit wait instant blow about chick answer man material current think print nor better example people drink gun together cost require or people planet ease ready enough sugar deal with us share office protect low thus farm oxygen fire force select paragraph always poem chick planet fact moment term
