''' Step 4: check membership of words in dictionary '''
class themeIndustrialEngineering:
    def __init__(self):
        # Initializie score counters for each area
        self.quality = 0
        self.operations = 0
        self.supplychain = 0
        self.project = 0
        self.data = 0
        self.healthcare = 0

    def countScore(self, terms, text):
        # Create an empty list where the scores will be stored
        self.scores = []
        self.terms_included = []
        
        # Obtain the scores for each area
        for area in terms.keys():
        
            if area == 'Quality/Six Sigma':
                for word in terms[area]:
                    if word in text:
                        self.quality +=1
                        self.terms_included.append(word)
                self.scores.append(self.quality)
        
            elif area == 'Operations management':
                for word in terms[area]:
                    if word in text:
                        self.operations +=1
                        self.terms_included.append(word)
                self.scores.append(self.operations)
        
            elif area == 'Supply chain':
                for word in terms[area]:
                    if word in text:
                        self.supplychain +=1
                        self.terms_included.append(word)
                self.scores.append(self.supplychain)
        
            elif area == 'Project management':
                for word in terms[area]:
                    if word in text:
                        self.project +=1
                        self.terms_included.append(word)
                self.scores.append(self.project)
        
            elif area == 'Data analytics':
                for word in terms[area]:
                    if word in text:
                        self.data +=1
                        self.terms_included.append(word)
                self.scores.append(self.data)
        
            else:
                for word in terms[area]:
                    if word in text:
                        self.healthcare +=1
                        self.terms_included.append(word)
                self.scores.append(self.healthcare)
        return (self.scores, self.terms_included)
