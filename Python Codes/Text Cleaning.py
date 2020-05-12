''' Step 2: clean text, remove non-alphabets and punctuations '''
import string
import re

# Convert all strings to lowercase
text = str(text.lower())

# Remove tags and non-alphabets
text = text.replace('\n', ' ')
text = text.replace('\\n', ' ')

# Remove punctuation
text = text.translate(str.maketrans('','',string.punctuation))

# Remove extra spaces
text = re.sub(' +', ' ', text)
