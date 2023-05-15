##################################################################################################################################################################################################################################################################################
#  Computer Project #9
#    
#    Algorithm: 
#       writing function definition for init_game() which initializes the game by creating a new deck of cards, shuffling it, and dealing one card to each column of the tableau.
#       writing function definition for deal_to_tableau(tableau, stock) which deals cards from the stock to the tableau by taking one card from the stock and adding it to each column of the tableau.
#       writing function definition for validate_move_to_foundation(tableau, from_col) which validates if the move to the foundation is valid. Returns True if a higher ranked card of the same suit is at the bottom of another tableau column.
#       writing function definition for move_to_foundation(tableau, from_col, foundation) which moves the card at the bottom of the given tableau column to the foundation if the move is valid.
#       writing function definition for validate_move_between_tableau(tableau, from_col, to_col) which validates if the move between tableau columns is valid. Returns True if the bottom card of the "from" column can be moved to the "to" column according to the game's rules. 
#       writing function definition for move_between_tableau(tableau, from_col, to_col) which moves the bottom card from the "from" column to the "to" column if the move is valid. If the move is not valid, it prints an error message. 
#       writing function definition for check_for_win(tableau, stock) which checks the current status of the game and checks whether only 4 aces are left are not
#       writing function definition for display(): Displays the current status of the game
#       writing function definition for get_option() which prompts the user for an input and checks if it;s valid or invalid
#       writing a function definition defining main() which calls all of the above defined functions according to the user's choice
#
##################################################################################################################################################################################################################################################################################

import cards  # required !!!

RULES = '''
Aces High Card Game:
     Tableau columns are numbered 1,2,3,4.
     Only the card at the bottom of a Tableau column can be moved.
     A card can be moved to the Foundation only if a higher ranked card 
     of the same suit is at the bottom of another Tableau column.
     To win, all cards except aces must be in the Foundation.'''

MENU = '''     
Input options:
    D: Deal to the Tableau (one card on each column).
    F x: Move card from Tableau column x to the Foundation.
    T x y: Move card from Tableau column x to empty Tableau column y.
    R: Restart the game (after shuffling)
    H: Display the menu of choices
    Q: Quit the game        
'''

def init_game():
    '''
    The program will use this function to initialize a game. The function has no parameters and returns the
starting state of the game with the three data structures initialized as described above. 
    Parameter:
        None

    Returns
    -------
    ini_stock : type class deck
        the stock of the cards game
    ini_tab : list of lists
        the tableau of the game
    list = empty list
        the fondation of the aces games

    '''
    ini_stock = cards.Deck()
    ini_stock.shuffle()
    ini_tab =[]
    for i in range(4):
        ini_tab.append([ini_stock.deal()])
        
    return (ini_stock, ini_tab, []) 
    
def deal_to_tableau( tableau, stock):
    '''
    The program will use this function to deal cards to the tableau.This function has two parameters: the
data structure representing the stock and the data structure representing the tableau. It will deal a card
from the stock to each column of the tableau, unless the stock has fewer than 4 cards; in which case it
will just deal a card to consecutive columns until the stock is empty.

    Parameters
    ----------
    tableau : list of lists
        the tableau of the game
    stock : Class Deck
        the stock of the Aces

    Returns
    -------
    None.

    '''
    num = 0
    deal_resp = stock.deal()
    while num<4:
        if deal_resp == None:
            break
        else:
            tableau[num].append(deal_resp)
            if num!=3:
                deal_resp = stock.deal()
            num+=1

           
def validate_move_to_foundation( tableau, from_col):
    '''
    The program will use this function to determine if a requested move to the foundation is valid. The
function should not modify the tableau in any case.
This function has two parameters: the data structure representing the tableau and an int indicating the
index of the column whose bottom card should be moved. 

    Parameters
    ----------
    tableau : list of lists
        the tableau of the game
    from_col : int
        the index range from 0 to 3

    Returns
    -------
    bool = boolean value
        True or false to validate the move to the foundation

    '''
    y = None
    try:
        card_val = str(tableau[from_col][-1]).strip()
        if card_val[0] == "A":
            print("\nError, cannot move  {}.".format(card_val))
            return False
        elif card_val[0] == "K":
            y= "king"
        elif card_val[0] == "Q":
            y = "queen"
        elif card_val[0]=="J":
            y="jack"
        else:
            y="num"
        end_list = []
        for k in range(4):
            try:
                val = str(tableau[k][-1]).strip()
                end_list+=[val]
            except IndexError:
                continue
    
        #print(end_list)
        for j in end_list:
            #print(j[0],y,j[1],card_val[1])
            if j[0].isalpha() == False and j!= card_val:
                if (y in ["king","queen","jack"]) and j[-1]== card_val[-1]:
                    #print("pol")
                    if j==end_list[-1]:
                        print("\nError, cannot move  {}.".format(card_val))
                        return False
                    else:
                        #print("moringa")
                        continue
                    #return False
                else:
                    try:
                        #print("ayyy", card_val)
                        x = int(card_val[:-1])
                        #print(j, card_val)
                        #print(x,j[-2:])
                        if int(j[:-1]) > int(card_val[:-1]) and j[-1]== card_val[-1] and j!= card_val:
                            return True
                        else:
                            if j==end_list[-1]:
                                print("\nError, cannot move  {}.".format(card_val))
                                return False
                            else:
                                #print("moringa")
                                continue
                                #return False
                    except ValueError:
                        #print(j, card_val)
                        #print("lou")
                        if j==end_list[-1]:
                            print("\nError, cannot move  {}.".format(card_val))
                            return False
                        else:
                            #print("moringa")
                            continue
                            #return False
            else:
                if j[0]=="A" and j[-1]==card_val[-1]:
                    #print("kooooooooo")
                    return True
                elif j[0]=="K" and (y in ["queen","jack","num"]) and j[-1]==card_val[-1]:
                    #print("klllll")
                    return True
                elif j[0]=="Q" and (y in ["jack","num"]) and j[-1]==card_val[-1]:
                    return True
                elif j[0]=="J" and (y=="num") and j[-1]==card_val[-1]:
                    return True
                else:
                    if j==end_list[-1]:
                        print("\nError, cannot move  {}.".format(card_val))
                        return False
                    else:
                        #print("moringa")
                        continue
    except IndexError:
        #print("mop")
        return False
                
    
def move_to_foundation( tableau, foundation, from_col ):
    '''
    The program will use this function to move a card from the tableau to the foundation.
This function has three parameters: the data structure representing the tableau, the data structure
representing the foundation, and an int indicating the index of the column whose bottom card should
be moved.

    Parameters
    ----------
    tableau : list of lists
        the tableau of the game
    from_col : int
        the index range from 0 to 3
    foundation : list
        the foundation deck of the game
   
    Returns
    -------
    None.

    '''
    bool_val = validate_move_to_foundation( tableau, from_col)
    if bool_val == True:
        move_val = tableau[from_col][-1]
        tableau[from_col].remove(move_val)
        foundation+=[move_val]
        
def validate_move_within_tableau( tableau, from_col, to_col ):
    '''
Validates if the move between tableau columns is valid. Returns True if the bottom card of the
"from" column can be moved to the "to" column according to the game's rules. 
Otherwise, it returns False.    

    Parameters
    ----------
    tableau : list of lists
        the tableau of the game
    from_col : int
        the index range from 0-3
    to_col : int
        the index range from 0-3

    Returns
    -------
    bool - checking if we can move
        the true or false value

    '''
    if tableau[to_col]!=[]:
        print("\nError, target column is not empty: {}".format(to_col+1))
        return False
    elif tableau[from_col]==[]:
        print("\nError, no card in column: {}".format(from_col + 1))
        return False
    else:
        return True

def move_within_tableau( tableau, from_col, to_col ):
    '''
    The program will use this function to move a card from the tableau to the foundation.
This function has three parameters: the data structure representing the tableau, an int indicating the
column whose bottom card should be moved, and an int indicating the column the card should be
moved to.
If the move is valid, the function will update the tableau; otherwise, it will do nothing to it.

    Parameters
    ----------
    tableau : list of lists
        the tableau of the game
    from_col : int
        the index range from 0-3
    to_col : int
        the index range from 0-3

    Returns
    -------
    None.

    '''
    bool_value = validate_move_within_tableau( tableau, from_col, to_col )
    if bool_value == True:
        move_val = tableau[from_col][-1]
        tableau[from_col].remove(move_val)
        tableau[to_col].append(move_val)
  

        
def check_for_win( tableau, stock ):
    '''
    The program will use this function to check if the game has been won.
This function has two parameters: the data structure representing the stock and the data structure
representing the tableau

    Parameters
    ----------
    stock: class Deck
        the stock of the game
    tableau : list of lists 
        the tableau of the aces up games

    Returns
    -------
    bool - checking for the win
        true for win, false for for lose

    '''
    counts = 0
    count_other = 0
    if stock.is_empty()== True:
        for j in range(4):
            for k in tableau[j]:
                #print(str(k).strip()[0])
                if  str(k).strip()[0]=="A":
                    counts+=1
                else:
                    count_other+=1
        if counts==4 and count_other==0:
            #print("hi")
            return True
        else:
            #print(900000)
            return False
    else:
        #print(777777777)
        #print(counts)
        return False
def display( stock, tableau, foundation ):
    '''
    this function is udes to display the game for the viewers

    Parameters
    ----------
    stock : Class Deck
        the stock of the game
    tableau : list of lists 
        the tableau of the aces up games
    foundation : list
        tre foundation deck of the game

    Returns
    -------
    None.

    '''
    '''Provided: Display the stock, tableau, and foundation.'''

    print("\n{:<8s}{:^13s}{:s}".format( "stock", "tableau", "  foundation"))
    maxm = 0
    for col in tableau:
        if len(col) > maxm:
            maxm = len(col)
    
    assert maxm > 0   # maxm == 0 should not happen in this game?
        
    for i in range(maxm):
        if i == 0:
            if stock.is_empty():
                print("{:<8s}".format(""),end='')
            else:
                print("{:<8s}".format(" XX"),end='')
        else:
            print("{:<8s}".format(""),end='')        
        
        #prior_ten = False  # indicate if prior card was a ten
        for col in tableau:
            if len(col) <= i:
                print("{:4s}".format(''), end='')
            else:
                print( "{:4s}".format( str(col[i]) ), end='' )

        if i == 0:
            if len(foundation) != 0:
                print("    {}".format(foundation[-1]), end='')
                
        print()

def get_option():
    '''
    The program will use this function to prompt the user to enter an option and return a representation of
the option designed to facilitate subsequent processing.
has no parameters
    
    Parameters
    ----------
    None

    Returns
    -------
    list- the options 
        the diffrent options

    '''
    choice_user = input("\nInput an option (DFTRHQ): ")
    if choice_user.lower()== "d":
        return ["D"]
    elif choice_user.lower() in ["f 1","f 2","f 3","f 4"]:
        return ["F", int(choice_user[-1])-1]
    elif choice_user.lower()[0] == "t":
        ch_list = choice_user.lower().split()
        x_val = int(ch_list[1])
        try:
            y_val = int(ch_list[2])
        
            if x_val in [1,2,3,4] and y_val in [1,2,3,4]:
                return ["T",x_val-1, y_val-1]
            else:
                print("\nError in option: {}".format(choice_user))
                return []
        except:
            print("\nError in option: {}".format(choice_user))
            return []
            
    elif choice_user.lower()=="r":
        return ["R"]
    elif choice_user.lower()=="h":
        return ["H"]
    elif choice_user.lower()=="q":
        return ["Q"]
    else:
        print("\nError in option: {}".format(choice_user))
        return []
        
def main():
    """
    This is the main function which displays the various menu options and 
    performs the activities(calling the above written functions accordingly)
    which the user asks for and loops until the user wants to break.
    
    Parameters
    ----------
    None.

    Returns
    -------
    None.

    """
    stock_val, tab_val, found_val = init_game()
    print(RULES)
    print(MENU)
    display(stock_val, tab_val, found_val)
    user_ch = get_option()
    while True:
        if user_ch[0]=="Q":
            print("\nYou have chosen to quit.")
            break
        elif user_ch[0]=="D":
            deal_to_tableau(tab_val, stock_val)
        elif user_ch[0]=="F":
            move_to_foundation(tab_val, found_val, user_ch[1])
        elif user_ch[0]=="R":
            print("\n=========== Restarting: new game ============")
            stock_val, tab_val, found_val = init_game()
            print(RULES)
            print(MENU)
        elif user_ch[0] == "H":
            print(MENU)
        elif user_ch[0]== "T":
            move_within_tableau(tab_val, user_ch[1], user_ch[2])
        else:
            pass
        bool_result = check_for_win(tab_val, stock_val)

        if bool_result == True:
            print("\nYou won!")
            break
        else:
            display(stock_val, tab_val, found_val)
            user_ch = get_option()
            while user_ch == []:
                user_ch = get_option()
if __name__ == '__main__':
     main()

