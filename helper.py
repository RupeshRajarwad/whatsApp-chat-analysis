def fetch_stats(selected_user,df):
    if selected_user=="Overall":
        # 1 : fetch number of messages
        num_messages=df.shape[0]
        #2: number of words
        words=[]
        for messages in df['Text']:
            words.extend(messages.split())
        return num_messages,len(words)
    else:
        new_df=df[df['Name']==selected_user]
        num_messages=new_df.shape[0]
        words=[]
        for messages in new_df['Text']:
            words.extend(messages.split())
        return num_messages,len(words)

