# Snake
Snake game developped in Python with the Pygame library.

The game has been developped according to the MVC design pattern (for well organized code) : 
- model/ : package containing Snake.py and Snack.py 
- view/ : package containing all the HMIs -> view.py (the main interface class), gameOver.py, scoreBanner.py (The black banner visible during the game), tools.py (containing generic methods for the view).
- controller/ : package containing controller.py (Intermediate between the view and the model).

As soon as the user does something, the controller checks the nature of the action and calls either the model or the view. 
The model may need to display some things to the user. In that case, it calls the controller which will call the view in order to display it.

Every time a new functionality needs to be coded, a new dedicated branch is created. 
When the functionality is finished and functional, then the master branch merges the dedicated branch. 