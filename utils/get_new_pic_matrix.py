import pandas as pd

def build_new_pic_matrix(image_url, model, all_tags):
    m = pd.DataFrame(0, index=all_tags, columns=list('n'))
    response = model.predict_by_url(image_url)
    concepts = response['outputs'][0]['data']['concepts']
    for concept in concepts:
        tag_name = concept['name']
        if(tag_name not in all_tags):
            continue
        else:
            val = concept['value']
            m.loc[tag_name, 'n'] = val
    return m