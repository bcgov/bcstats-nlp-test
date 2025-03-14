# model stuff
from datasets import Dataset

# convert to a multi labeled dataset for use with huggingface
def get_labels_list(row):
    out = list(row.values[1:])
    # make sure everything is a float
    out = [float(x) for x in out]
    return out


# chunk data into train, test splits
def create_train_test_dataframes(df, n_train=1_000):
    df_train = df.iloc[:n_train, :]
    df_test = df.iloc[n_train:, :]
    return df_train, df_test


# use distillbert to tokenize the data (a smaller version of vert)
def tokenize_data(example, tokenizer):
    return tokenizer(example['response'], truncation=True, padding='max_length')

# create a huggingface style Dataset to best utilize their tools
def create_hf_dataset(df, tokenizer):
    dataset = Dataset.from_pandas(df[['response', 'label']])
    dataset = dataset.map(
        tokenize_data, 
        batched=True, 
        fn_kwargs={'tokenizer': tokenizer}
        )
    
    return dataset


