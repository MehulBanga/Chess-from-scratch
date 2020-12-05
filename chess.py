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
  
  def invalid_check_move(self,new_pos):
    if(self.color == "black"):
        if (new_pos[0]==self.position[0]+1 and new_pos[1]==self.position[1]):
            return True
        else:
            return False
    else:
        if(new_pos[0] == self.position[0]-1 and new_pos[1] == self.position[1]):
            return True
        else:
            return False
        pass
    pass
  def takes_validity_check(self,takes_pos):
    if(self.color == "black"):
      if(takes_pos[0]==self.position[0]+1 and (takes_pos[1]==self.position[1]+1 or takes_pos[1]==self.position[1]-1)):
        return True
      else:
        return False
    else:
      if(takes_pos[0]==self.position[0]-1 and (takes_pos[1]==self.position[1]+1 or takes_pos[1]==self.position[1]-1)):
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
  
  def invalid_check_move(self,new_pos):
    if(self.position[0] == new_pos[0] or self.position[1] == new_pos[1]):
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
    def invalid_check_move(self,new_pos):
        if(abs(self.position[0]-new_pos[0])==abs(self.position[1]-new_pos[1])):
            return True
        else:
            return False
  
class chessboard():
    def __init__(self):
        self.pawns = [bishop([7,2],"white"),bishop([7,5],"white"),bishop([0,2],"black"),bishop([0,5],"black"),rook([7,0],"white"),rook([7,7],"white"),rook([0,0],"black"),rook([0,7],"black"),pawn([6,0],"white"),pawn([6,1],"white"),pawn([6,2],"white"),pawn([6,3],"white"),pawn([6,4],"white"),pawn([6,5],"white"),pawn([6,6],"white"),pawn([6,7],"white"),pawn([1,0],"black"),pawn([1,1],"black"),pawn([1,2],"black"),pawn([1,3],"black"),pawn([1,4],"black"),pawn([1,5],"black"),pawn([1,6],"black"),pawn([1,7],"black")]
        self.deleted = []
        self.board = array_maker()
        
    def index_finder(self,input_position):
        for i in range(len(self.pawns)):
            if(self.pawns[i].position == input_position):
                return i
        else:
          return -1
    
    def update_board(self):
        for i in range(8):
          for j in range(8):
            self.board[i][j] = "_"
        for i in range(len(self.pawns)):
            position = self.pawns[i].position
            self.board[int(position[0])][int(position[1])] = self.pawns[i].symbol
            
        
  
  
    def invalid_check(self,new_pos,pawn_index):
        if(self.pawns[pawn_index].invalid_check_move(new_pos)):
            if(self.board[new_pos[0]][new_pos[1]]== "_"):
                return True
        else:
            return False
            
            
            
    def takes_takes(self,initial_position,takes_pos):
        pawn_index = self.index_finder(initial_position)
        takes_index = self.index_finder(takes_pos)
        if(self.pawns[pawn_index].takes_validity_check(takes_pos)):
          if(takes_index != -1) and (self.pawns[takes_index].color != self.pawns[pawn_index].color):
            self.delete_pieces(takes_pos)
            self.pawns[pawn_index].position = takes_pos
            self.update_board()
        else:
          print("are maa chudi padi hai")
         
    def invalid_check_rook(self,in_pos,new_pos):
      piece_index = self.index_finder(in_pos)
      answer = True
      if(self.pawns[piece_index].invalid_check_move(new_pos)):
        if(in_pos[0] == new_pos[0]):
          if(new_pos[1] - in_pos[1]>0):
            for i in range(1,new_pos[1] - in_pos[1]+1):
              if(self.board[in_pos[0]][in_pos[1]+i] != "_"):
                answer = False
          else:
            for i in range(1,in_pos[1] - new_pos[1]+1):
              if(self.board[in_pos[0]][in_pos[1]-i] != "_"):
                answer = False
        else:
          if(new_pos[0] - in_pos[0]>0):
            for i in range(1,new_pos[0] - in_pos[0]+1):
              if(self.board[in_pos[0]+i][in_pos[1]] != "_"):
                answer = False
          else:
            for i in range(1,in_pos[0] - new_pos[0]+1):
              if(self.board[in_pos[0]-i][in_pos[1]] != "_"):
                answer = False
              
        return answer
      else:
        return False
            
    def invalid_check_bishop(self,in_pos,new_pos):
        piece_index = self.index_finder(in_pos)
        answer=True
        if(self.pawns[piece_index].invalid_check_move(new_pos)):
            if(in_pos[0]>new_pos[0] and in_pos[1]<new_pos[1]):
                for i in range(1,abs(in_pos[0]-new_pos[0]+1)):
                    if(self.board[in_pos[0]-i][in_pos[1]+i] != "_"):
                        answer=False
            elif(in_pos[0]>new_pos[0] and in_pos[1]>new_pos[1]):
                for i in range(1,abs(in_pos[0]-new_pos[0]+1)):
                    if(self.board[in_pos[0]-i][in_pos[1]-i] != "_"):
                        answer=False
            elif(in_pos[0]<new_pos[0] and in_pos[1]>new_pos[1]):
                for i in range(1,abs(in_pos[0]-new_pos[0])+1):
                    if(self.board[in_pos[0]+i][in_pos[1]-i] != "_"):
                        answer=False
            else:
                for i in range(1,abs(in_pos[0]-new_pos[0])+1):
                    if(self.board[in_pos[0]+i][in_pos[1]+i] != "_"):
                        answer=False
            return answer
        else:
            return False
    def move_bishop(self,in_pos,new_pos):
        piece_index = self.index_finder(in_pos)
        if(self.invalid_check_bishop(in_pos,new_pos)):
            self.pawns[piece_index].position = new_pos
            self.update_board()  
        else:
          print("Arre maa chudi padhi hai")
        
                
                    
        
            
    def move_rook(self,in_pos,new_pos):
      piece_index = self.index_finder(in_pos)
      if(self.invalid_check_rook(in_pos,new_pos)):
        self.pawns[piece_index].position = new_pos
        self.update_board()  
      else:
        print("Arre maa chudi padhi hai")
      
      
      
      
    def move_pawn(self,input_position,new_pos):
        pawn_index = self.index_finder(input_position)
        if(self.invalid_check(new_pos,pawn_index)):
            self.pawns[pawn_index].position = new_pos
            self.update_board( )
        else:
            print("Are Maa Chudi Padi Hai")
            
            
            
    def move(self,input_position,new_pos):
      piece_index = self.index_finder(input_position) 
      piece = self.pawns[piece_index].symbol
      if(piece == "P"):
        self.move_pawn(input_position,new_pos)
        pass
      elif(piece == "R"):
        self.move_rook(input_position,new_pos)
        pass
      elif(piece == "B"):
          self.move_bishop(input_position,new_pos)
          pass
          
        
        
        
        
    def print_board(self):
        for i in range(8):
            for j in range(8):
                print(self.board[i][j],end = '   ')
            print(end = "\n\n")
    
    
    
    def delete_pieces(self,position):
        self.deleted.append(self.pawns[self.index_finder(position)])
        self.pawns[self.index_finder(position)].is_on_board = False
        self.pawns.remove(self.pawns[self.index_finder(position)])
        
        self.update_board()
    
    
    
game = chessboard()
game.update_board()



game.print_board()

