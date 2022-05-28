# Read text from a file, and count the occurrence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    with open("./story.txt", "r") as f:
        read_file = f.read()
    return read_file
result = read_file_content("./story.txt")
print(result)


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    split_text = text.split()
    
    dic = {}
    for i in split_text:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return dic           

print(count_words())

    #return {"as": 10, "would": 20}