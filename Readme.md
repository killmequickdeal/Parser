
Initial Ideas: large data set normally stored in file. 
1. Read from file
2. Parse string into Segments (segment names can repeat (cant use hash)
3. Parse segment into fields (fields can repeat, cant use hash) database would probably make these easier if I have time
4. Provide a simple GUI interface for iteration and searching through segments
*Search might be inefficient with this initial idea. O(num_segments*num_fields)*

Test Ideas:
1. Empty file
2. Single Segment, single fields
2. multi segment, multi fields
3. duplicate segment name
4. duplicate field name
5. segment with no fields
6. field without a segment?
