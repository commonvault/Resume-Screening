''' 'Step 5: calculate matching scores '''
# Create a data frame with the scores summary
import pandas as pd
summary = pd.DataFrame(scores,index=terms.keys(),columns=['score']).sort_values(by='score',ascending=False)
summary
