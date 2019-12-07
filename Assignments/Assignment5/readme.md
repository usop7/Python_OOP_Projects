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

    
### Expanded mode for pokemon
1. 'create_pokemon' method will call 3 helper methods to create stats, abilities and moves.
2. Each method will call 'process_async_tasks' with a list of URL parameters.
3. 'process_task' will query for a single URL and will create an expanded version of object based on the query result, and append it to a corresponding list.
4. When all tasks are completed, 3 methods will return a list of objects(Stat, Ability, Move).
5. Then 'create_pokemon' method will create a Pokemon object with those returned lists. 




