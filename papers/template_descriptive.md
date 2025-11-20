# Metadata

https://doi.org/10.1017/S1366728921000699





# Methods



**# Participants**



Experiment 1

19 French–English bilingual children

average age of 3.50 years (range: 3.10–4.10)

12 males and 7 females



A modified version of the Language Experience and Proficiency Questionnaire (Marian et al., 2007) was used to assess the children’s language background and proficiency.

Language dominance = the language that was rated the highest for comprehension; when ratings were equal, mother’s dominant language (A predetermined inclusion criterion was

that children were rated at least 7/10 in comprehension in both languages)

10 English-dominant children and 9 French-dominant children



Experiment 2

21 healthy Spanish–English bilingual children

average age of 3.70 years (range: 3.20–4.10).

9 males and 12 females. 



Language dominance measured as in Experiment 1.

8 English-dominant children and 13 Spanish-dominant children

For Spanish, all children were exposed regularly from birth. For English, 8 children were

exposed regularly from birth (i.e., were simultaneous bilinguals), 9 were exposed after birth but within the first year of life, and 4 were exposed between 12 and 36 months.

*5 children tested but not included in the final sample due to not meeting pre-established inclusion criteria for bilingual exposure (n = 4) or reported language delay (n = 1).*





**# Power**

Experiment 1

A sensitivity analysis indicated

that this sample size has 80% power to detect an effect size of dz

= .68 or greater in a two-tailed repeated measures t-test, which is

the average effect size observed in word recognition paradigms in

children older than 16 months according to MetaLab (https://

metalab.stanford.edu; Bergmann et al., 2018).





**# Exclusion**

Another 10 children excluded from the final sample due to fussiness (n = 3), reported health or developmental issues (n = 3), not meeting preestablished language criteria (n = 3), or because of technical difficulties (n = 1).





**# Measures**



Experiment 1

Modified version of the Language Experience and Proficiency Questionnaire (Marian,

Blumenfeld \& Kaushanskaya, 2007) for assessing the children’s language background and proficiency. 

**10 English-dominant** children and **9 French-dominant** children. 

**8 children** regularly exposed to both English and French **from birth** (i.e., were simultaneous

bilinguals), and **11 who began regular exposure to their second language later in life** (in all cases prior to age 18 months).



Children’s exposure to intra-sentential language mixing was measured via the Language Mixing Scale. Average score in this sample = **13.50 (range: 4–28)**.



Children’s productive vocabulary was measured in each of their languages via the Developmental Vocabulary Assessment for Parents (DVAP; Libertus, Odic, Feigenson \& Halberda, 2015) and, for French, an adaptation of a checklist similar to the DVAP, based on words used in the French adaptation of the PPVT (Échelle de vocabulaire en images Peabody; Dunn, Dunn \& Thériault-Whalen, 1993). 

**Data were missing for one language for one participant.** 

average of **77 words** in their dominant language (**range: 37–177**), **48 words** in their non-dominant language **(range: 2–131) \[t(17) = 6.08, p < .001, d = 1.43]**

average number of words produced across both languages = **125 (range: 39–308).**



Socioeconomic status was assessed via mothers’ highest educational attainment. All mothers had completed high school. Specifically, 4 mothers had completed a graduate degree, 9 had

completed a bachelor’s degree, 5 had completed other postsecondary training (e.g., college diploma, some university, trade school), and 1 had completed high school but had not received further formal education. For subsequent analysis, these categories were then **converted to approximate years of education** (e.g., high school = 12 years, bachelor’s degree=16 years). Mothers’ average educational attainment was **15.80 years (SD = 2.50).**



Experiment 2

As in Experiment 1, children’s exposure to parental language mixing was measured via the Language Mixing Scale Score (Byers-Heinlein, 2014)

average score = 16.50 (range: 0–30) --> not statistically different from the amount of mixing reported by parents in Experiment 1 who had a mean of 13.50 \[t(38) = 1.18, p = .244, d = 0.37].



Socioeconomic status was assessed via mothers’ highest educational attainment: 7 had completed a graduate degree, 4 had completed some university, 5 had completed high school, 3 had not completed high school, and 2 did not report. As in Experiment 1, these categories were then converted to approximate years of education-->  average educational

attainment = 14.40 years (SD = 4.10). 

We infer that the sample of Spanish–English bilingual children had a different profile of

socioeconomic status, including more mothers with lower educational attainment, compared to the sample of French–English bilingual children.





**# Analyses**

conducted in R (R Core Team, 2018), primarily using the eyetrackingR package (Dink \& Ferguson, 2015), directly compared data for French–English (Experiment 1) and Spanish–English (Experiment 2) bilingual children.

Explored whether performance at test was predicted by performance during the learning phase, and whether this relationship was moderated by sentence type (single language, mixed-language) and population (French–English, Spanish–English) --> linear mixed-effects model



fixed effects: 

* performance during the learning phase sentence type
* population
* the interaction between sentence type and population

random intercepts by participants



The reference level for population was French–English bilinguals, and the reference

level for sentence type was single-language. The model equation was prop.test ∼ prop.learning + sentence.type\*population + (1|id).





**# Results**

significant main effect of performance during the learning phase

significant interaction between sentence type and population

significant main effect of sentence type, which is interpreted at the reference level of French–English bilinguals.



Compared this model to a larger model that included interactions of all predictors, but found no evidence that the more complicated model was a significantly better fit to the data, based on a chi-squared test comparing the models.





# Data

Experiment 1

Stimuli, data, and analysis scripts

are available via the Open Science Framework at https://osf.io/

q2nzr/



Experiment 2

Stimuli, data, and analysis scripts are available via the Open

Science Framework at https://osf.io/q2nzr/.



