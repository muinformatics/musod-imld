------------------------------------------------------------------------

Rounds: Team Grading

**Purpose:** This module uses the *StudentScoreCreator* class, which is responsible for calculating and aggregating various scores and grade values for students participating in the ***Rounds*** program.

------------------------------------------------------------------------

## Scoring Process and Weights:

Each component is scored based on specific rules and deadlines. The final total score is a weighted sum of all components, normalized to a 100-point scale. The weights for each component are as follows:

- Case presentation / ACE Assessment: **40**%

- Article classification: **20**%

- Discussion participation: **20**%

- Written material: ***10***% (D3/D4), ***20***% (D1/D2)

- Item 2 (D3/D4 only): ***10***% (Not applicable for D1/D2)

------------------------------------------------------------------------

## Case Presentation / ACE Assessment (40%): 

This is based on the Faculty's Student Evaluation and its associated criteria. Each criterion is converted to a normalized score, and the average is computed.

### Normalization 

Each criterion is rated from 0-5, with 5 being the highest. The criterion is then normalized as follows:

- 5 = 100

- 4 = 88

- 3 = 79

- 0-2 = 0

The evaluation criteria typically varies from year to year. Usually, D4 has the largest number of criteria.

------------------------------------------------------------------------

## Article Classification (20%):

This score is calculated for article classification based on submission timing. The article due date is determined and then the submission date is used for comparison.

- If the "first" article date is greater than the due date, a score of 9 is given

- If the \"first\" article date is less than or equal to the due date, a score of 10 is given.

All other options result in a 0 score.

------------------------------------------------------------------------

## (Observer) Discussion Participation (20%):

This score is calculated using the list of discussion scores for all observer teams. There are **four** discussion questions scores. Each "initial" question's *submission* *date* is compared against the due date for grading.

- If the "first" discussion question date is greater than the due date, a score of 9 is given

- If the \"first\" discussion question date is less than or equal to the due date, a score of 10 is given.

All other options result in a 0 score.

------------------------------------------------------------------------

## Written Material (10/20%):

This weight varies by student level (D1/D2 or D3/D4) and checks for timely submission of required files or articles.

- D1/D2 this is 20%

- D3/D4 this is 10%

The score is calculated using the submission date of the material and comparing it to the due date (of the presentation files).

- If the file submission date is greater than the file due date, a score of 9 is given

- If the file submission date is less than or equal to the due date, a score of 10 is given.

All other options result in a 0 score.

TECH NOTE: The file submission date is the record "create date".

## Additional Assignment / "Item 2" (10%):

This weight applies only to students' level D3 or D4. Its original scope represents an additional assignment or requirement specific to D3/D4 students (e.g., a supplemental project, quiz, or other program-defined task). It does NOT apply to D1/D2 students.

NOTE: This option has never been fully implemented. As a result, the following values are 'hardcoded'

- If the student is a D3 or D4 a value of 10 is assigned and summed up with the written material to equate to a full 20%

- If the student is a D1 or D2 a value 0 is assigned and summed up with the full 20% weight of the written material.

------------------------------------------------------------------------
