from nltk.corpus import stopwords

example_sent = "This is a sample sentence, showing off! the stop words, filtration."

stop_words = set(stopwords.words('english'))
print(stop_words)

word_tokens = example_sent.split()
filtered_sentence = [w for w in word_tokens if not w in stop_words]

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print(word_tokens)
print(filtered_sentence)
print()
file = open("file.txt")
line = file.read()
data = line.split()
file_filtered_sentence = []
for w in data:
    if w not in stop_words:
        file_filtered_sentence.append(w)

print(data)
print(file_filtered_sentence)