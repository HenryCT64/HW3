# Your name: Henry Collins-Thompson
# Your student id: 0874 7961
# Your email: henryct@umich.edu
# Who or what you worked with on this homework (including generative AI like ChatGPT):
# If you worked with generative AI also add a statement for how you used it.  
# e.g.: 
# Asked Chatgpt hints for debugging and suggesting the general sturcture of the code

import random
# create a Digital Book of Answers
class DigitalBookofAnswers():

    # create the constructor (__init__) method 
    # ARGUMENTS: 
    #       self: the current object
    #       answers: a list of potential answers
    # RETURNS: None
    def __init__(self, answers):

        self.book_answer_list = answers
        self.questions_asked_list = []
        self.answered_list = []

    # Create the __str__ method
    # ARGUMENTS: 
    #       self: the curent object
    # RETURNS: a string
    def __str__(self):
        return (" - ".join(self.book_answer_list))

    # Creates the check_get_answer method
    # ARGUMENTS:
    #       self: the current object
    #       question: the question the user wants to ask the digital book of answers
    # RETURNS: a string
    def check_get_answer(self, question):

        if question in self.questions_asked_list:
            return f"I've already answered this question. The answer is: {self.book_answer_list[self.answered_list[self.questions_asked_list.index(question)]]}"
        else:
            self.rand_num = random.randrange(len(self.book_answer_list))
            self.questions_asked_list.append(question)
            self.answered_list.append(self.rand_num)
            return str(self.book_answer_list[self.rand_num])
    # Creates open_book method
    # ARGUMENTS:
    #   self: the current object
    # RETURNS: None
    def open_book(self):
        temp_val = 1
        while temp_val:
            question = input(f"Turn {1+len(self.questions_asked_list)} - Please enter your question: ")
            if (question == "Done"):
                print("Goodbye! See you soon.")
                temp_val = 0
            else: print(self.check_get_answer(question))

    # Create the answer_log method
    # ARGUMENTS: 
    #       self: the curent object
    # RETURNS: a list
    def answer_log(self):
        unique_list = []
        count_list = []
        for j in self.answered_list:
            if j not in unique_list:
                unique_list.append(j)
                count_list.append(self.answered_list.count(j))
        nuList = []
        for i in reversed(list(set(count_list))):
            nuList.append(f"{i} - {self.book_answer_list[unique_list[count_list.index(i)]].lower()}")

        return nuList

def test():
    answers_list = ['Believe in Yourself', 'Stay Open to the Future', 'Enjoy It']
    book = DigitalBookofAnswers(answers_list)

    print("Test __init__:")
    print(f"Answer History List: Expected: {[]}, Actual: {book.answered_list}")
    print(f"Question History List: Expected: {[]}, Actual: {book.questions_asked_list}")
    print(" ")

    print("Test __str__:")
    expected = "Belive in Yourself - Stay Open to the Future - Enjoy It"
    print(f"Expected: {expected}, Actual: {str(book)}")
    print(" ")
    
    empty_book = DigitalBookofAnswers([])
    print("Test __str__: when it's an empty book without possible answers")
    expected = ""
    print(f"Expected: {expected}, Actual: {str(empty_book)}")
    print(" ")

    print("Testing return value of check_get_answer:")
    res = book.check_get_answer('test question')
    print(f"Expected: {str}, Actual: {type(res)}")
    print(" ")


    print("Testing check_get_answer")
    book.book_answer_list = ['Go For It']
    print(book.questions_asked_list)
    res = book.check_get_answer('test question 2')
    print(f"Expected: {'Go For It'}, Actual: {res}")
    print(" ")

    print("Testing that check_get_answer adds answer index to answered_list:")
    # ↓ newly added - reset the questions_asked_list
    book.questions_asked_list = []
    ##############################
    book.book_answer_list = ['Go For It']
    book.answered_list = []
    book.check_get_answer('test question 2')
    expected = [0]
    res = book.answered_list
    print(f"Expected: {expected}, Actual: {res}")
    print(" ")

    print("Testing that check_get_answer does not add 'I've already answered this question' part to answered_list:")
    book.book_answer_list = ['Believe In Yourself']
    book.answered_list = [0]
    book.questions_asked_list = ['test question 3']
    book.check_get_answer('test question 3')
    expected = [0]
    res = book.answered_list
    print(f"Expected: {expected}, Actual: {res}")
    print(" ")


    print("Testing return value answer_log")
    book.book_answer_list = ['Follow Your Inner Voice', 'Stay Positive', 'Go For It']
    book.answered_list = [0, 0, 0, 1, 1, 2]
    res = type(book.answer_log())
    print(f"Expected: {list}, Actual: {res}")
    print(" ")

    print("Testing return value answer_log elements")
    book.answered_list = [0, 0, 0, 1, 1, 2]
    res = type(book.answer_log()[0])
    print(f"Expected: {str}, Actual: {res}")
    print(" ")

    print("Testing answer_log")
    book.answered_list = [0, 0, 0, 1, 1, 2]
    res = book.answer_log()
    expected = ['3 - follow your inner voice', '2 - stay positive', '1 - go for it']
    print(f"Expected: {expected}, Actual: {res}")
    print(" ")

    print("Testing empty answer_log")
    book.answered_list = []
    res = book.answer_log()
    expected = []
    print(f"Expected: {expected}, Actual: {res}")
    print(" ")




# Extra Credit
def my_test():
    # Put your test code here

    answer_list = ["Follow Your Inner Voice", "Stay Positive", "Go For It", "Believe in Yourself", "Stay Open to the Future", "Enjoy It"]
    book = DigitalBookofAnswers([])
    
    print("Testing empty __str__")
    print(f"Expected: , Actual: {str(book)}")

    book.book_answer_list = (answer_list)
    print("Testing check_get_answer")
    book.check_get_answer("Yo")
    print(f"Expected: I've already answered this question. The answer is: {book.book_answer_list[book.answered_list[-1]]}, result: {book.check_get_answer("Yo")}")
    
    print(f"Expected: ['1 - {book.book_answer_list[book.answered_list[-1]].lower()}'], actual: {book.answer_log()}")
    pass    

def main():
    
    answer_list = ["Follow Your Inner Voice", "Stay Positive", "Go For It", "Believe in Yourself", "Stay Open to the Future", "Enjoy It"]
    book = DigitalBookofAnswers(answer_list)
    book.open_book()
    print(book.answer_log())
    pass    


# Only run the main function if this file is being run (not imported)
if __name__ == "__main__":
    main()
    test() 
    my_test() #TODO: Uncomment if you do the extra credit
    
