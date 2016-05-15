import pandas as pd
from sklearn.linear_model import LogisticRegression

train = pd.read_csv("./train.csv")
test = pd.read_csv("./test.csv")

train.loc[:, 'pixel0':] = train.loc[:, 'pixel0':] * 1.0 / 255.0
test.loc[:, 'pixel0':] = test.loc[:, 'pixel0':] * 1.0 / 255.0

alg = LogisticRegression(random_state = 1)
alg.fit(train.loc[:, 'pixel0':], train.loc[:, 'label'])

predictions = alg.predict(test)

submission = pd.DataFrame({"ImageId": range(1, test.shape[0] + 1), "label": predictions})

submission.to_csv("result.csv", index = False)


