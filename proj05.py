##############################################################
    #  Computer Project #5
    #
    #  Open file function
    #   Takes input for what file
    #       Try/ except to see if file opens
    #           returns file or returns open file
    #  Find max function
    #   If the number is greater than the max
    #       return number
    #   If they are equal
    #       return the max
    #   Otherwise
    #       return max and max name
    #  Find min function
    #   If the number is less than the max
    #       return number
    #   If they are equal
    #       return the min
    #   Otherwise
    #       return min and min name
    #  Read file function
    #   Define all varibles
    #   Use for loop to iterate through text
    #       Create title, episode and score by splicing text 
    #       if score is NA in text
    #           Define varibles to find max and min
    #       if episodes is NA in text
    #           Define varibles to find max
    #   Find average score by using counters
    #   return all the values
    #  Search anime function
    #   Define all varibles
    #   Use for loop to iterate through text
    #       Create title and release by splicing text 
    #       use title and relase to format out string
    #   return count and out strings
    #  Main function
    #   Define menu options 
    #   If statement for error message
    #       print error statement and menu options
    #   Intiate while loop for when the option is not 3
    #       Initiate while loop for every option
    #           Call necessay functions to the main function in each option
    #           Print statemnets for options
    #           Print menu options 
    #    Display closing message
##############################################################

def open_file():
    """
    Checks for if file is a vaild file

    Returns
    -------
    a file

    """
    while 1==1:
        file = input("Enter filename: ")
        try:
            #looks to see if the file can open 
            data_fp = open(file, "r", encoding="utf-8")
            return data_fp
        except:
            #if the file is not found return the function to reask for file
            print("\nFile not found!")
            print("")
            return open_file()

    
def find_max(num, name, max_num, max_name):
    """
    Finds the maximum value 

    Parameters
    ---------- 
    num : float
        a number in file
    name : str
        a name of the series
    max_num : float
        the maximum number found
    max_name : str
        name found with max value

    Returns
    -------
    max_num: float
        The maximum number
    max_name: str
        the name associated with the max number

    """
    #if the number is greater than max return the number
    #if they are equal return the maximum with the formatting
    #Else return the max and the name
    if num > max_num:
        return num, "\n\t{}".format(name)
    elif num == max_num:
        return max_num, "{}\n\t{}".format(max_name, name)
    else:
        return max_num, max_name
    
    
def find_min(num, name, min_num, min_name):
    """
    find the minimum value

    Parameters
    ----------
    num : float
        a number in file
    name : str
        a name of the series
    min_num : float
        The minimum number found
    min_name : str
        name found with min value

    Returns
    -------
    min_num: float
        The minimum number
    min_name: str
        The name associated with the minimum number

    """
    #if the number is less than max return the number
    #if they are equal return the minimum with the formatting
    #Else return the min and the name
    if num < min_num:
        return num, "\n\t{}".format(name)
    elif num == min_num:
        return min_num, "{}\n\t{}".format(min_name, name)
    else:
        return min_num, min_name
    
def read_file(data_fp):
    """
    Reads the files to take out specific numbers and strings

    Parameters
    ----------
    data_fp : A file
        The file that is imputted 

    Returns
    -------
    max_score : float
        The max score
    max_score_name : str
        Name associated with max score
    max_episodes : float
        max count of episodes
    max_episode_name : str
        Name associated with max episodes 
    min_score : float
        The minimum score
    min_score_name : str
        Name associated with min score
    avg_score : float
        The average of all the scores in the file

    """
    #define varible names
    max_score = 0.0
    max_score_name = ""
    max_episodes = 0
    max_episode_name = ""
    min_score = 500000000.0
    min_score_name = ""
    avg_score = 0.0
    total_score = 0
    count = 0
    
    for line in data_fp:
        #splice the text file
        title = line[0:100].strip()
        score = line[100:105].strip()
        episodes = line[105:110].strip()
        
        if score != "N/A":
            #count used later to fnd average
            #total_score used later to fnd average
            #redefine varible names to find max/min functions
            score = float(score)
            count +=1
            total_score += score
            max_score, max_score_name = find_max(score, title, max_score,
                                                 max_score_name)
            min_score, min_score_name = find_min(score, title, min_score,
                                                 min_score_name)
            
        if episodes != "N/A":
            #redefine varible names to find max function
            episodes = int(episodes)
            max_episodes, max_episode_name = find_max(episodes, title,
                                                      max_episodes, 
                                                      max_episode_name)

    if total_score > 0:
        #if total score is 0 it returns 0.0 as defined above
        avg_score = round(total_score / count, 2)
    
    return max_score, max_score_name, max_episodes, max_episode_name, min_score, min_score_name, avg_score

def search_anime(data_fp, anime_name): 
    """
    

    Parameters
    ----------
    data_fp : A file
        The file that is imputted 
    anime_name : str
        The user imputs the search in file

    Returns
    -------
    count : int
        The amount of times the search is in the file
    out_str : str
        The title and dates

    """
    #define varibles
    count = 0
    out_str = ""
    
    for line in data_fp:
        #splice text file
        title = line[0:100]
        release_season = line[110:122]
    
        #use the splicing above to create the out string
        #use the counter to see how many times it is in the file
        if anime_name in title:
            out_str += "\n\t{:100s}{:12s}".format(title, release_season)
            count += 1
            
    return count, out_str


def main():
    """
    The user imputs option and prints respective option    

    Returns
    -------
    None.

    """
    #defined menu and banner options
    BANNER = "\nAnime-Planet.com Records" \
             "\nAnime data gathered in 2022"
    
    MENU ="Options" + \
          "\n\t1) Get max/min stats" + \
          "\n\t2) Search for an anime" + \
          "\n\t3) Stop the program!" + \
          "\n\tEnter option: "
    
    print(BANNER)
    print(MENU)
    
    #ask for user input
    option = input("")
    codes = ("1","2","3")
    
    #While loop to keep prmpting for option unless option "3" is inputed
    while option !="3":
        #If inputted code is not a possible code print error message
        if option not in codes:
            print("Invalid menu option!!! Please try again!")
            print(MENU)
            option = input("")
    
        #while loop initiaed when option "1" is selected 
        while option == "1":
          #call both functions to use in print statements
          #Final print statements 
          file = open_file() 
          max_score, max_score_name, max_episodes, max_episode_name, min_score, min_score_name, avg_score= read_file(file)
          print("\n\nAnime with the highest score of {:,}:".format((max_score))
                + "\n" + max_score_name)
          print("\n\nAnime with the highest episode count of {:,}:".format((max_episodes))
                + "\n" + max_episode_name)
          print("\n\nAnime with the lowest score of {:,.2f}:".format((min_score))
                + "\n" + min_score_name)
          print("\n\nAverage score for animes in file is {:,}".format(avg_score))
          
          print(MENU)
          option = input("")
    
        while option =="2":
            #call both functions to use in print statements
            #Final print statements 
            file = open_file()
            anime_name = input("\nEnter anime name: ")
            count, out_str = search_anime(file, anime_name)
            #If else statement for error message
            if anime_name not in out_str:
                print("\nNo anime with '{}' was found!".format(anime_name))
            else:
                print("\nThere are {} anime titles with '{}'".format(count,anime_name))
                print(out_str)
            
            print(MENU)
            option = input("")
    #print closing statement
    print("Thank you using this program!")
    
# These two lines allow this program to be imported into other code
# such as our function tests code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.
#DO NOT CHANGE THESE 2 lines  
if __name__ == "__main__":
    main()