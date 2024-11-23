# Program Verlauf
- Daten werden generiert
  - Jede 100ms wird ein sample generiert
    - hier koennte man auch etwas Varianz reinbringen
- Position der Daten ueber den optischen Fluss updaten
  - Woher kommt der 
- Woher weiss ich ob die ID zweier Unkrauter gleich ist




# Chat GPT TASK

My goal is to develop a program which simulates the acquisition of weed positions which are constantly changing. The setup is as follows:

- the weed position frame is 100x100 pixel wide
- a new weed position is generated every 100ms
  - since the weed position moves throught the frame they all start a x = 0
- after a new weed is beeing generated its posission is appended to a list called weed_list
- every time new data is generated the old weed positions are updated by a before defined value, it consists of the speed and the rotation of the frame, in the weed_list
- all weed get an ID which stays with the certain weed even after a position update
- even if a weed leaves the frame it still stays in the list
- This simulation should be also visualized in the console
  - the weed are shown as white stars and when they are in the weed_list their color changes
