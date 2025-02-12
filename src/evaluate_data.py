# model stuff
import torch

# custom metrics for evaluation
from sklearn.metrics import accuracy_score, f1_score

# create metrics to evaluate performance
def compute_metrics(pred):
    logits, labels = pred
    preds = torch.sigmoid(torch.tensor(logits)).numpy() > 0.5  # Apply sigmoid and threshold
    accuracy = accuracy_score(labels, preds)
    f1 = f1_score(labels, preds, average="micro")
    return {"accuracy": accuracy, "f1": f1}


# inference function to classify predictions based on a pre-trained classifier
def classify_batch(batch, classifier, threshold, suffix='_bert'):
    outputs = classifier(batch['response'])
    
    labels = classifier.model.config.id2label.values()
    labels_llm = [x+suffix for x in labels] # to differentiate from the actual labels 
    batch_results = {label: [] for label in labels_llm}

    # loop through the batch 
    # each out will be of form [{'label': 'first_label', 'score': score}, {'label': 'second_label', ...}]
    for out in outputs:
        label_scores = {label: 0 for label in labels_llm}

        # update if above threshold
        label_scores.update({
            result['label'] + suffix: int(result['score'] > threshold)
            for result in out if result['score'] > threshold
        })
        
        # update other if NO label exceeds threshold 
        if sum(label_scores.values())==0:
            label_scores['other'+suffix]=1
        
        # Append results
        for label in labels_llm:
            batch_results[label].append(label_scores[label])
        

    return batch_results


# inference function to classify predictions based on a non-trained LLM
def classify_batch_llm(batch, classifier, labels, threshold, suffix='_llm'):
    outputs = classifier(batch['response'], labels, multi_label=True, truncation=True)
    
    # note that the labels fed into the classifier are the words - need to get the lower cased version here for matching 
    labels_llm = [x.lower().replace(' ','_')+suffix for x in labels] # to differentiate from the actual labels 
    batch_results = {label: [] for label in labels_llm}

    # loop through the batch 
    # each out will be of form {'sequence': 'response', 'labels': [list,of,labels], 'scores':[list,of,scores]}
    for out in outputs:
        label_scores = {label: 0 for label in labels_llm}

        # update if above threshold
        for label, score in zip(out["labels"], out["scores"]):
            label_fixed = label.lower().replace(' ','_')
            if score > threshold:
                label_scores[label_fixed+suffix] = 1
        
        # update other if NO label exceeds threshold 
        if sum(label_scores.values())==0:
            label_scores['other'+suffix]=1
        
        # Append results
        for label in labels_llm:
            batch_results[label].append(label_scores[label])

    return batch_results


# make comparisons
# perfect match
def all_right(x, categories_original, new_cats):
    for ii, cat in enumerate(categories_original):
        new_cat = new_cats[ii]
        if x[cat] != x[new_cat]:
            return False
    return True

# correct plus an extra
def right_plus_extra(x, categories_original, new_cats):
    for new_cat, cat in zip(new_cats, categories_original):
        original_match = True
        extra = False
        if x[new_cat] > x[cat]:
            extra = True
        if x[cat] > x[new_cat]:
            original_match = False
            
    if original_match and extra:
        return True
    else:
        return False
    
# added one or more (but may have missed one) 
def added_one(x, categories_original, new_cats):
    for ii, cat in enumerate(categories_original):
        new_cat = new_cats[ii]
        if x[cat]==0:
            if x[new_cat]==1:
                return True
            
    return False

# missed one or more
def missed_one(x, categories_original, new_cats):
    for ii, cat in enumerate(categories_original):
        new_cat = new_cats[ii]
        if x[new_cat]==0:
            if x[cat]==1:
                return True
            
    return False
        