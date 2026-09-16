# Try to append to a tuple. It won't work. 
# Name: Rin Isoe
# Date: Sept. 16, 2026

survey_respondents = (1012, 1035, 1021, 1053)
# Tuples are immutable, so create a new tuple instead of using append().
survey_respondents = survey_respondents + (1054,)
print("Updated survey respondents:", survey_respondents)