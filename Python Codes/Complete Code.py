# Import required libraries
# import PyPDF2
import textract
import re
import string
import pandas as pd
import matplotlib.pyplot as plt
from DictionarySetup import termsIndustrialEngineering
from ScoresCalculation import themeIndustrialEngineering

text = textract.process('../Files/ornwipa_resume.pdf', encoding='ascii')
text = str(text.lower())
text = text.replace('\n', ' ')
text = text.replace('\\n', ' ')
text = text.translate(str.maketrans('','',string.punctuation))

termsDict = termsIndustrialEngineering()
terms = termsDict.getTerms()

scoresList = themeIndustrialEngineering()
scores = scoresList.countScore(terms, text)
        
# Create a data frame with the scores summary
summary = pd.DataFrame(scores,index=terms.keys(),columns=['score']).sort_values(by='score',ascending=False)
print(summary)

# Create pie chart visualization
pie = plt.figure(figsize=(10,10))
plt.pie(summary['score'], labels=summary.index, explode = (0.1,0,0,0,0,0), autopct='%1.0f%%',shadow=True,startangle=90)
plt.title('Industrial Engineering Candidate - Resume Decomposition by Areas')
plt.axis('equal')
plt.show()

# Save pie chart as a .png file
# pie.savefig('resume_screening_results.png')
