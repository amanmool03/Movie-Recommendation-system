from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

texts=['London Paris London','Paris Paris London']
cv = CountVectorizer()
cv_fit=cv.fit_transform(texts)

print(f'The feature names are {cv.get_feature_names()}')
print(cv_fit.toarray())

similarity_scores=cosine_similarity(cv_fit)
print(similarity_scores)

