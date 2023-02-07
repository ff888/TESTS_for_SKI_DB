Tests for Ski Jumping Database (pytest) #

 **Description:**

 The purpose of tests here is to check if fails created by SKI-JUMPING-DATABASE-PROJECT engine holds valid data.
 The structure of DB and file is described in SKI-JUMPING README file.

 **There are 11 tests:**
 1. test_headers_upper --> Test if first line of the files is line with HEADERS
 2. test_ranking_length_is_max_2 --> Test if second column (RANKING) value are max 2 characters long.
 3. test_ranking_is_numerical --> Test if second column (RANKING) column holds only numerical values
 4. test_name_is_title --> Test if third column (NAME) value is title.
 5. test_nationality_upper --> Test if forth column (NATIONALITY) value is uppercase characters only.
 6. test_nationality_length_is_3 --> Test if forth column (NATIONALITY) is 3 characters long.
 7. test_dob_list_length --> Test if fifth column (DOB - Date Of Birth) value is holding 3 elements.
 8. test_dob_day --> Test if fifth column (DOB - Date Of Birth) the first element is max 2 characters long. 
 9. test_dob_month --> Test if fifth column (DOB - Date Of Birth) the second element is the same as one in the month list.
 10. test_dob_year_length --> Test if fifth column (DOB - Date Of Birth) the third element is 4 characters long.
 11. test_club_istitle --> Test if sixth column (CLUB) values are title.
 12. test_judge_marks_max_value --> Test if values in judge marks columns (10 columns -> 9-13 and 22-26) are max 20.0.
 13. test_judge_marks_isfloat --> Test if values in judge marks columns (10 columns -> 9-13 and 22-26) are floating point number type.
 14. test_rankings_max_length --> Test if rankings 4 columns are max characters long.
 15. test_rankings_for_numerical_characters_only --> Test if rankings columns contain only numerical characters.
 16. test_judge_points_max_value --> Test if judge marks points columns contain values are max 60.0.

 **Preconditions:**

 To run those tests you need to have a SKI-JUMPING_DATABASE downloaded, and you need to provide path to where the DB is located.
