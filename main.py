import nltk
from nltk.corpus import inaugural
from nltk.corpus import stopwords

# Download the Inaugural Address Corpus if you haven't already
nltk.download('inaugural')

# Get the list of presidential inaugural addresses
addresses = inaugural.fileids()

# Initialize a frequency distribution for words
word_freq = nltk.FreqDist()

# Calculate word frequencies across all addresses
for address in addresses:
    words = inaugural.words(address)
    words = [word.lower() for word in words if word.isalpha()]  # Convert to lowercase and remove punctuation
    word_freq.update(words)

# Get the list of English stop words
stop_words = set(stopwords.words('english'))

# Filter out stop words
filtered_word_freq = [(word, freq) for word, freq in word_freq.items() if word not in stop_words]

# Sort the filtered word frequencies in descending order
sorted_word_freq = sorted(filtered_word_freq, key=lambda x: x[1], reverse=True)

# Print the sorted word frequencies
for word, freq in sorted_word_freq[:20]:
    print(f'{word}: {freq}')







