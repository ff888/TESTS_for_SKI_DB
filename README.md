Tests for Ski Jumping Database (pytest) #

 **Description:**

 The purpose of tests here is to check if fails created by SKI-JUMPING-DATABASE-PROJECT engine holds valid data.
 The structure of DB and file is described in SKI-JUMPING README file.

 **There are 11 tests:**
 1. Check if first line of the files is line with HEADERS
 2. Check if second column (RANKING) value are max 2 characters long.
 3. Check if second column (RANKING) column holds only numerical values
 4. Check if third column (NAME) value is title.
 5. Check if forth column (NATIONALITY) value is uppercase characters only.
 6. Check if forth column (NATIONALITY) is 3 characters long.
 7. Check if fifth column (DOB - Date Of Birth) value is holding 3 elements.
 8. Check if fifth column (DOB - Date Of Birth) the first element is max 2 characters long. 
 9. Check if fifth column (DOB - Date Of Birth) the second element is the same as one in the month list.
 10. Check if fifth column (DOB - Date Of Birth) the third element is 4 characters long.
 11. Check if sixth column (CLUB) values are title.
 12. Checks if values are floating point number in given columns.

 **Preconditions:**

 To run those tests you need to have a SKI-JUMPING_DATABASE downloaded, and you need to provide path to where the DB is located.
