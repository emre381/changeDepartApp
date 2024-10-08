
### Breakdown of Code

1. **`school` class:**
   - The `school` class has four attributes:
     - `branch`: Represents the class branch (e.g., "12-A").
     - `teacher`: Represents the teacher's name.
     - `department`: Represents the department the class belongs to (e.g., "SE" for Software Engineering).
     - `avaliable`: Represents the number of available students in the class.

2. **Methods of the `school` class:**
   - `show_info()`: Displays detailed information about the class, such as branch, teacher, department, and available students.
   - `teacher_name()`: Prints only the teacher's name.
   - `depart_change()`: Allows the user to input a new department, prints the old department, updates it, and shows the updated class information.

3. **Main Loop:**
   - The program runs an infinite `while` loop, asking the user to input details about the class:
     - Branch name
     - Teacher name
     - Department name
     - Number of available students
   - After creating a `school` object, the program gives the user the option to change the department of the class by entering `1`. If the user does not want to change the department, the loop breaks, and the process finishes.

### Example Flow:

1. User inputs the following:
   - Branch: "12-A"
   - Teacher: "Mr. Smith"
   - Department: "SE"
   - Available Students: 30

2. The user is asked if they want to change the department. If they enter `1`, they will be prompted to input a new department name. For example, if the new department is "CE" (Civil Engineering), the following will be displayed:

```
Please enter branch name: 12-A
Please enter teacher name: Mr. Smith
Please enter department: SE
Please enter available students: 30
--Welcome--

Please enter 1 if you want to change the department: 1
Please enter new department: CE
***Old  Department***:  SE
---------------------------------------------
Branch: 12-A
Teacher: Mr. Smith
Department: CE
Avaliable Student: 30
---------------------------------------------
```

If the user does not want to change the department, they can press any other key, and the program will end with:

```
Process is done!!!
```


