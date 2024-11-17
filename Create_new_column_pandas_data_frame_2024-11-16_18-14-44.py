# Problem: Create new column pandas data frame
# Link: https://leetcode.com/studyplan/introduction-to-pandas/#:~:text=Create%20a-,New,-Column 
import pandas as pd
            def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
                employees['bonus'] = employees['salary']*2
                return employees
    