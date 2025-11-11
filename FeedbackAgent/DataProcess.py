from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
import pandas as pd
nltk.download('stopwords')
nltk.download('punkt') # For word_tokeni
nltk.download('punkt_tab')

class DataProcess:
    
    df:pd.DataFrame

    def load_data_file(self, file_path):
        self.df = pd.read_csv(file_path)
        return self.df

    def remove_stopwords_from_text(text):
        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(text)
        filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
        return " ".join(filtered_sentence)

    def extract_metadata(self, df):
        metadata = {}
        # Column names
        metadata['Schema'] = df.columns.tolist()
        
        metadata['Text'] = "The user feedback comments are stored in the 'Text' column."
        
        metadata["Level"] = ("The 'Level' column indicates the sentiment level of the feedback, "
                            "with values ranging from 1 (bad experience) to 5 (good experience). "
                            "This column can be used to analyze the overall sentiment distribution of the feedback.")
        return metadata

    def preprocess_data(self, df: pd.DataFrame) -> pd.DataFrame:
        df.dropna(subset=['Text'], inplace=True)
        df['Text'] = df['Text'].str.replace(r'[\r\n]+', ' ', regex=True)
        
        df_relevant = df[['Text', 'Level']] #Keep only relevant columns
        
        return df_relevant