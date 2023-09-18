import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    ordered = scores["score"].sort_values(ascending = False).to_list()
    try:
        max_score = ordered[0]
        lst =[]
        count = 1
        
        for score in ordered:
            if score == max_score:
                lst.append(count)
            else:
                max_score = score
                count += 1
                lst.append(count)
        data = {"score": ordered, "rank": lst}
        return pd.DataFrame(data=data)

    except:
        data = {"score": [], "rank": []}
        return pd.DataFrame(data=data)