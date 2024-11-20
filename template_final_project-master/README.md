
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# << Project Title >>
## CS110 Final Project  << Semester, Year >>

## Team Members

Joyal Paul

*** 

## Project Description

There is a player that starts off at the bottom of a volcano. The objective is to get to the top and escape the volcano before the magma rises and kills the player. 
There are obstacles on each level of the volcano, like monsters, falling or cracking steps, and dripping lava that hurts and slows down the player. 
Some of the steps can drop you to lower levels and some can kill you due to fall damage. The player must escape in limited time and make a final jump to the helicopter to be rescued. 
If the player doesn't make it up in time, the player loses. I might add levels with faster times and more obstacles to let the player pick a difficulty level. 

***    

## GUI Design

### Initial Design

![initial gui](gui-1.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. Start menu
2. Rising lava
3. Moving / falling objects
4. Screen shaking when taking damage
5. Game over screen

### Classes

- Player - creates a player object thats able to move around, jump, and block
- Enemies - creates an enemy or multiple enemy objects that are able to move back and forth, face the player, and shoot bullets

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Run Counter Program  |GUI window appears with count = 0  |
|  2                   | click count button   | display changes to count = 1      |
etc...
