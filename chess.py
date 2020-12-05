# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 07:27:09 2020

@author: mehul
"""

def array_maker():
  array = []
  for i in range(8):
    temp = []
    for j in range(8):
      temp.append("_")
    array.append(temp)
  return array
  pass


def converter(s):
  s= s[1:]
  s = s.lower()
  temp = "abcdefgh"
  answer  =[]
  answer.append(temp.index(s[0]))
  answer.append(int(s[1])-1)
  return answer
  
 

class pawn():
  def __init__(self,position,color):
    self.value = 1
    self.color = color
    self.position = position
    self.symbol = "P"
    self.is_on_board = True
    pass
  
  def invalid_check_move(self,new_position):
    if(self.color == "black"):
        if (new_position[0]==self.position[0]+1 and new_position[1]==self.position[1]):
            return True
        else:
            return False
    else:
        if(new_position[0] == self.position[0]-1 and new_position[1] == self.position[1]):
            return True
        else:
            return False
        pass
    pass
  def takes_validity_check(self,takes_position):
    if(self.color == "black"):
      if(takes_position[0]==self.position[0]+1 and (takes_position[1]==self.position[1]+1 or takes_position[1]==self.position[1]-1)):
        return True
      else:
        return False
    else:
      if(takes_position[0]==self.position[0]-1 and (takes_position[1]==self.position[1]+1 or takes_position[1]==self.position[1]-1)):
        return True
      else:
        return False
      
class rook():
  def __init__(self,position,color):
    self.value = 5
    self.position = position
    self.symbol = "R"
    self.is_on_board = True
    self.color=color
    pass
  
  def invalid_check_move(self,new_position):
    if(self.position[0] == new_position[0] or self.position[1] == new_position[1]):
      return True
      
    else:
      return False
   
  def takes_validity_check(self,takes_position):
      if(takes_position[0]==self.position[0]  or takes_position[1]==self.position[1]):
        return True
      else:
        return False
    
  
class bishop():
    def __init__(self,position,color):
        self.value = 3
        self.position = position
        self.symbol = "B"
        self.is_on_board=True
        self.color=color
        pass
    def invalid_check_move(self,new_position):
        if(abs(self.position[0]-new_position[0])==abs(self.position[1]-new_position[1])):
            return True
        else:
            return False
        
    def takes_validity_check(self,takes_position):
      if(abs(takes_position[0]-self.position[0]) == abs(takes_position[1]-self.position[1])):
        return True
      else:
        return False
  
class Queen():
    def __init__(self,position,color):
        self.value = 9
        self.position = position
        self.symbol = "Q"
        self.is_on_board=True
        self.color=color
        pass
    
    def invalid_check_move(self,new_position):
        if(abs(self.position[0]-new_position[0])==abs(self.position[1]-new_position[1]) or self.position[0] == new_position[0] or self.position[1] == new_position[1] ):
            return True
        else:
            return False  
    
    def takes_validity_check(self,takes_position):
        if(abs(self.position[0]-takes_position[0])==abs(self.position[1]-takes_position[1]) or (self.position[0] == takes_position[0] or self.position[1] == takes_position[1]) ):
            return True
        else:
            return False    
        
class chessboard():
    def __init__(self):
        self.pieces = [Queen([0,4],"black"),Queen([7,3],"white"),bishop([7,2],"white"),bishop([7,5],"white"),bishop([0,2],"black"),bishop([0,5],"black"),rook([7,0],"white"),rook([7,7],"white"),rook([0,0],"black"),rook([0,7],"black"),pawn([6,0],"white"),pawn([6,1],"white"),pawn([6,2],"white"),pawn([6,3],"white"),pawn([6,4],"white"),pawn([6,5],"white"),pawn([6,6],"white"),pawn([6,7],"white"),pawn([1,0],"black"),pawn([1,1],"black"),pawn([1,2],"black"),pawn([1,3],"black"),pawn([1,4],"black"),pawn([1,5],"black"),pawn([1,6],"black"),pawn([1,7],"black")]
        self.deleted = []
        self.board = array_maker()
        
    def index_finder(self,initial_position):
        for i in range(len(self.pieces)):
            if(self.pieces[i].position == initial_position):
                return i
        else:
          return -1
    
    def update_board(self):
        for i in range(8):
          for j in range(8):
            self.board[i][j] = "_"
        for i in range(len(self.pieces)):
            position = self.pieces[i].position
            self.board[int(position[0])][int(position[1])] = self.pieces[i].symbol
            
        
    def invalid_check(self,new_position,piece_index):
        if(self.pieces[piece_index].invalid_check_move(new_position)):
            if(self.board[new_position[0]][new_position[1]]== "_"):
                return True
        else:
            return False
            
    def takes_takes(self,initial_position,takes_position):
        piece_index = self.index_finder(initial_position)
        takes_index = self.index_finder(takes_position)
        if(takes_index != -1) and (self.pieces[piece_index].color != self.pieces[takes_index].color):
          if(self.pieces[piece_index].takes_validity_check(takes_position) and self.pieces[piece_index].invalid_check_move(takes_position)):  
            self.delete_pieces(takes_position)
            new_piece_index = self.index_finder(initial_position)
            self.pieces[new_piece_index].position = takes_position
            self.update_board()
        else:
          print("are maa chudi padi hai - chessboard")
         
    def invalid_check_rook(self,initial_position,new_position):
      piece_index = self.index_finder(initial_position)
      answer = True
      if(self.pieces[piece_index].invalid_check_move(new_position)):
        if(initial_position[0] == new_position[0]):
          if(new_position[1] - initial_position[1]>0):
            for i in range(1,new_position[1] - initial_position[1]+1):
              if(self.board[initial_position[0]][initial_position[1]+i] != "_"):
                answer = False
                break
          else:
            for i in range(1,initial_position[1] - new_position[1]+1):
              if(self.board[initial_position[0]][initial_position[1]-i] != "_"):
                answer = False
                break
        else:
          if(new_position[0] - initial_position[0]>0):
            for i in range(1,new_position[0] - initial_position[0]+1):
              if(self.board[initial_position[0]+i][initial_position[1]] != "_"):
                answer = False
                break
          else:
            for i in range(1,initial_position[0] - new_position[0]+1):
              if(self.board[initial_position[0]-i][initial_position[1]] != "_"):
                answer = False
                break
              
        return answer
      else:
        return False
            
    def invalid_check_bishop(self,initial_position,new_position):
        piece_index = self.index_finder(initial_position)
        answer=True
        if(self.pieces[piece_index].invalid_check_move(new_position)):
            if(initial_position[0]>new_position[0] and initial_position[1]<new_position[1]):
                for i in range(1,abs(initial_position[0]-new_position[0]+1)):
                    if(self.board[initial_position[0]-i][initial_position[1]+i] != "_"):
                        answer=False
                        break
            elif(initial_position[0]>new_position[0] and initial_position[1]>new_position[1]):
                for i in range(1,abs(initial_position[0]-new_position[0]+1)):
                    if(self.board[initial_position[0]-i][initial_position[1]-i] != "_"):
                        answer=False
                        break
            elif(initial_position[0]<new_position[0] and initial_position[1]>new_position[1]):
                for i in range(1,abs(initial_position[0]-new_position[0])+1):
                    if(self.board[initial_position[0]+i][initial_position[1]-i] != "_"):
                        answer=False
                        break
            else:
                for i in range(1,abs(initial_position[0]-new_position[0])+1):
                    if(self.board[initial_position[0]+i][initial_position[1]+i] != "_"):
                        answer=False
                        break
            return answer
        else:
            return False
        
    def move_bishop(self,initial_position,new_position):
        piece_index = self.index_finder(initial_position)
        if(self.invalid_check_bishop(initial_position,new_position)):
            self.pieces[piece_index].position = new_position
            self.update_board()  
        else:
          print("Arre maa chudi padhi hai -bishop")
           
            
    def move_rook(self,initial_position,new_position):
      piece_index = self.index_finder(initial_position)
      if(self.invalid_check_rook(initial_position,new_position)):
        self.pieces[piece_index].position = new_position
        self.update_board()  
      else:
        print("Arre maa chudi padhi hai  -rook")
      
    def move_queen(self,initial_position,new_position):  
        piece_index = self.index_finder(initial_position)       
        if (initial_position[0] ==new_position[0] or new_position[1] == initial_position[1]):
            if(self.invalid_check_rook(initial_position,new_position)):
                self.pieces[piece_index].position = new_position
                self.update_board()
        elif(abs(initial_position[0]-new_position[0])==abs(initial_position[1]-new_position[1])):
            if(self.invalid_check_bishop(initial_position,new_position)):
                self.pieces[piece_index].position = new_position
                self.update_board()
                
        else:
            print("Maa chudi padi hai -queen")
      
      
    def move_pawn(self,initial_position,new_position):
        piece_index = self.index_finder(initial_position)
        if(self.invalid_check(new_position,piece_index)):
            self.pieces[piece_index].position = new_position
            self.update_board( )
        else:
            print("Are Maa Chudi Padi Hai  -pawn")
            
            
    def move(self,initial_position,new_position):
      piece_index = self.index_finder(initial_position) 
      piece = self.pieces[piece_index].symbol
      if(piece == "P"):
        self.move_pawn(initial_position,new_position)
        pass
      elif(piece == "R"):
        self.move_rook(initial_position,new_position)
        pass
      elif(piece == "B"):
          self.move_bishop(initial_position,new_position)
          pass
      elif(piece == "Q"):
          self.move_queen(initial_position,new_position)
          
        
    def print_board(self):
        for i in range(8):
            for j in range(8):
                print(self.board[i][j],end = '   ')
            print(end = "\n\n")
    
    def delete_pieces(self,position):
        self.deleted.append(self.pieces[self.index_finder(position)])
        self.pieces[self.index_finder(position)].is_on_board = False
        self.pieces.remove(self.pieces[self.index_finder(position)])
        
        self.update_board()
    
    
    
game = chessboard()
game.update_board()



# #Moves to check movement of Queen
# game.move([6,3], [5,3])
# game.move([7,3],[6,3])
# game.move([6,3],[4,1])

# #move to check Queen takes
# game.takes_takes([4,1],[1,1])
# game.takes_takes([1,1],[0,2])
# game.takes_takes([0,4],[0,2])
# print(game.pieces[game.index_finder([0,2])].color)


# #Set of moves to test bug 0.1's correction
# game.move([1,1], [2,1]) #pawn move
# game.move([0,2],[2,0])#bishop to 2,0
# game.move([6,4],[5,4])#pawn move
# game.takes_takes([2,0], [7,5]) #bishop takes 7,5 bishop
# game.takes_takes([7,7],[7,5]) #rook takes bishop
# print(game.pieces[game.index_finder([7,5])].color)





game.print_board()

