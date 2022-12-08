import pandas as pd
import dask

def preprocess(filename):
    df = pd.read_csv(filename, header=None, error_bad_lines=False, encoding='utf-8')
    df = df.drop([2, 3], axis=1)
    df.columns = ['Date', 'Chat']
    message = df['Chat'].str.split("-", n=1, expand=True)
    df['Time'] = message[0]
    df['Text'] = message[1]
    message1 = df['Text'].str.split(":", n=1, expand=True)
    df['Text'] = message1[1]
    df['Name'] = message1[0]
    df = df.drop(columns=['Chat'])
    df['Text'] = df['Text'].str.lower()
    df['Text'] = df['Text'].str.replace('<media omitted>', 'MediaShared')
    df['Text'] = df['Text'].str.replace('this message was deleted', 'DeletedMsg')
    return df
