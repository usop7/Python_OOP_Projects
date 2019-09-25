# Tamagotchi Simulator

Tamagotchi Simulator is a simple console game that holds a pet(Tamagotchi) that a user will take care of.

## Entry Point

* console.py

## Known Errors

* There is no known errors.

* Regarding user inputs, if a user input doesn't belong to the valid answer list, the system will keep prompting user with the same list of options until a user gives a proper answer.

## Limitation

* It is not a real-time simulator, which means it will only update a tamagotchi's status when a user calls actions - check status, feed, give medicine and play.

## Play Feature

* If a user selects 'Play' option, it calls 'Game Controller' which has a list of Game objects.

* Each Game object has name(string), output(name), and level of fun(float) attributes.

* Tamagotchi's Happiness meter will be increased proportionately based on the selected game's level of fun.

* Game object's output attribute will be printed out to users as a result.

 ## Feed Feature

- If a user selects 'Feed' option, it calls 'Food Controller' which has a list of Food objects.

- Each Food object has name(string), and calorie(float) attributes.

- Tamagotchi's Hunger meter will be decreased proportionately based on the selected food's calorie.