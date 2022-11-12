 # Final Project Milestone #2

[Final Project Description](https://docs.google.com/document/d/1j3zgypVjPjzXl4pL1_Wpjvp3GLCW9zcFydkwUjNfNUA/edit?usp=sharing)

Complete this document in **your** portfolio (CH 6). 

Let's decide on our Final project. Select the idea from Milestone 1 that seems the most interesting to you.

Each class is a model of some real world object. We often refer to data classes as the ***models*** in a GUI program. Your models represent your application data.

Given what you have learned about classes on Chapter 6, describe the ***interface only*** of 3 classes you think you might need for your project.

*For example*, if you want to create a space invaders type game, you would need a class to represent the ship, which could have an interface such as: 

* class ship
    * moveLeft()
    * moveRight()
    * shoot()

***

Come up with interfaces for 3 possible classes you think you may need. Again, brainstorm a little. Nothing is *wrong*.

## Class Interface 1

class Card
- attributes:
  1- image
  2- suite
  3- number
  4- value
  5- x
  6- y
  7- length
  8- width
- methods:
  1- move_up
  2- move_down
  3- switch_player 


## Class Interface 2

class Player
-attributes:
  1- name
  2- points
  3- cards (hand)
  4- winnter/loser
  5- x
  6- y
-methods:
  1- deal
  2- flip
  3- hit

## Class Interface 3

class Deck
-attributes:
  1- number of cards
  2- card ID
  3- x
  4- y
-methods:
  1- deal
  2- collect
  3- restart