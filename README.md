# Sports Reference Engineering Internship Prompt 2023
The solution I used relies on three classes. A team class to store the data for each team, a league class to hold all the teams together, and a matrix class that creates and holds the table results.

**The logic of the code can be explained in the following steps:**
1. The json data is read from the file using the default python json library which returns a dictionary of the contents.
2. A for loop iterates through the json dictionary and assigns a team name and a head-to-head results dictionary to a new team object which is appended to a list.
3. The list of teams is passed to a league object which automatically creates a list fo team names to be used as labels in the matrix.
4. The league object runs code to populate the matrix with the head-to-head data for each team. This can be broken down into the following substeps:
   1. The league object goes through each team and calls a populateRow() function.
   2. The populateRow() function finds the index of the given team in the matrix's list of labels.
   3. Then, the function goes through each element of the team's head-to-head dictionary and finds the index of the opposing team in the list of matrix labels.
   4. Once the 2 indices are located, the corresponsing cell is filled with team 1's head-to-head wins against team 2 (no need to do the losses because those are just other teams' wins).
5. The league object prints the finished matrix with formatting to make it look nice.
