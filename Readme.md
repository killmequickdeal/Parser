Problem: 
Data Parsing

Description:
We want to be able to parse large data sets and provide a simple interface to search and view parsed messages. Create a module that parses messages in the following format:

  <seg>|<field>|<field>...||<seg>|<field>...||<seg>...

Where <seg> is a 3-character segment name, <field> is a 3-character field name, and the field value immediately follows the field name. A final segment separator (||) is optional.

For example, a message could look like this:
  NAM|FNAFred|LNABlogs||BIO|DOB02/03/1974||

The interface should allow iterating over segments and fields in a message and searching by segment and field name. Assume that field names may repeat.

Include whatever unit tests and/or user interface you feel are appropriate.

Guidelines:
1. You are free to use any language of your choice
2. Please comment your code to explain complex design patterns
3. If you use a database, include your database schema in the solution
4. There is no deadline, but please do not spend more than a few hours to solve this problem
5. Include a readme.txt with instructions on how to execute your code
6. Please provide your solution via email (zipped please) or link I can access your work
7. If you have any questions, please respond quickly


Initial Ideas: large data set normally stored in file. 
1. Read from file
2. Parse string into Segments (segment names can repeat (cant use hash)
3. Parse segment into fields (fields can repeat, cant use hash) database would probably make these easier if I have time
4. Provide a simple GUI interface for iteration and searching through segments

Search might be inefficient with this initial idea. O(num_segments*num_fields)

Questions:
1. It states "Assume that field names may repeat". Does this mean segment names cannot repeat?
    answer - Yes you can read them from a file
    
2. It states "A final segment separator (||) is optional." Does this mean there may be messages which do not use || to separate segments?
    answer - you will always || between segs

3. Should I be reading these data sets from a file?
    answer - Yes you can read them from a file

4. Can a segment have the same field twice? ex) NAM | FNAFred | FNAGeorge | | ...
    answer - Just assume duplicates are possible

5. Is there a desired output format from the search for segments & fields?
    answer - I like asking for clarity, however it is up to you on how to display the output.


Language: Python3.7

Execute program w/ default file "../test1.txt": python main.py

Execute program w/ a different file: python main.py -f filename

example: python main.py -f test2.txt



Final remarks: Total programming time ~2.5 hours. I wish I had given more time for developing test cases,
but I am happy with the outcome. I also had finished programming the solution before questions 3,4,5 were answered.
For questions 3&5 this is fine. 

However, question 4 will not work in my current solution and I do not wish to
spend more time fixing this. I believe the simplest solution would be to make the fields dictionary go from
str -> list instead of str -> str. This would allow you to check if the field name already exists and add a
new entry to the list.
