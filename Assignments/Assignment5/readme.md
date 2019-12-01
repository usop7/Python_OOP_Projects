# Pokedex
Pokedex is a simple console app that allows users to search for 'pokemon', 'ability', or 'move'.

### Entry Point
pokedex.py

### Console Arguments
python pokedex.py {"pokemon" | "ability" | "move"} {"filename.txt" | "name or id'} [--expanded] [--output "filename.txt"]

### Additional Validation
- Query mode must be one of the followings: 
    - pokemon, ability, move

- Input file and Output file (if specified) must end with '.txt' extension.

### Workflow
1. When creating a Pokedex object, Request object will be created based on command line arguments
2. 'process_async_tasks' method will create multiple async tasks and run them concurrently by using 'gather'.
    - 'process_task' handles a single async task with a given parameter.
    - If the GET request is successful, it calls a corresponding method based on the query mode in order to create an object based on the returned json data.
    - The new object will be stored in a corresponding result list based on the query mode.
3. When completed, a report will be printed out either to a console or a file if specified.




