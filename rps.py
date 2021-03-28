import random 
import main

# Print multiline instruction 
# performstring concatenation of string 

def game():
  print("Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs Paper -> Paper wins \n"
                                +"Rock vs Scissor -> Rock wins \n"
                                +"Paper vs Scissor -> Scissor wins \n") 
  while True: 
      print("Enter:\n 1 For 🗻 Rock\n 2 For 📰 Paper\n 3 For ✂ Scissor") 
        
      # take the input from user 
      choice = int(input("User turn: ")) 
    
      # OR is the short-circuit operator 
      # if any one of the condition is true 
      # then it return True value 
        
      # looping until user enter invalid input 
      while choice > 3 or choice < 1: 
          choice = int(input("Enter valid input: ")) 
            
    
      # initialize value of choice_name variable 
      # corresponding to the choice value 
      if choice == 1: 
          choice_name = '🗻 Rock'
      elif choice == 2: 
          choice_name = '📰 Paper'
      else: 
          choice_name = '✂ Scissor'
            
      # print user choice  
      print("User choice is: " + choice_name) 
      print("\nNow its computer turn.......") 
    
      # Computer chooses randomly any number  
      # among 1 , 2 and 3. Using randint method 
      # of random module 
      comp_choice = random.randint(1, 3) 
        
      # looping until comp_choice value  
      # is equal to the choice value 
      while comp_choice == choice: 
          comp_choice = random.randint(1, 3) 
    
      # initialize value of comp_choice_name  
      # variable corresponding to the choice value 
      if comp_choice == 1: 
          comp_choice_name = '🗻 Rock'
      elif comp_choice == 2: 
          comp_choice_name = '📰 Paper'
      else: 
          comp_choice_name = '✂ Scissor'
            
      print("Computer choice is: " + comp_choice_name) 
    
      print(choice_name + " V/s " + comp_choice_name) 
    
      # condition for winning 
      if((choice == 1 and comp_choice == 2) or
        (choice == 2 and comp_choice ==1 )): 
          print("📰 Paper Wins!! ", end = "") 
          result = "📰 Paper"
            
      elif((choice == 1 and comp_choice == 3) or
          (choice == 3 and comp_choice == 1)): 
          print("🗻 Rock Wins!! ", end = "") 
          result = "🗻 Rock"
      else: 
          print("✂ Scissor Wins!! ", end = "") 
          result = "✂ Scissor"
    
      # Printing either user or computer wins 
      if result == choice_name: 
          print("\n⭐ User wins ⭐") 
      else: 
          print("\n⭐ Computer wins ⭐") 
    
      ans = input("Do you want to play again? (Y/N): ")
      if ans.lower()=="y":
          game()
      # if user input n or N then condition is True 
      elif ans.lower()=="n": 
        main.menu()
        break
         
          
          
      
