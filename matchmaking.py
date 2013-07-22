import time

class MatchMaker:
    def __init__(self):
        """
            default constructor
        """
        self.names_and_answers_women = {}
        self.names_and_answers_men = {}

        self.query_woman = ""

    def __is_equal_size(self, list, other_list):
        if len(list) == len(other_list):
            return True
        else:
            return False

    def __set_names_and_answers_women(self, names_women, answers_women):
        """
        :param names_women: list of women names
        :param answers_women:
        """
        self.names_and_answers_women = dict(zip(names_women, answers_women))
        #print self.names_and_answers_women

    def __set_names_and_answers_men(self, names_men, answers_men):
        """
        :param names_men:
        :param answers_men:
        """
        self.names_and_answers_men = dict(zip(names_men, answers_men))
        #print self.names_and_answers_men

    def __compare_answers(self, answer, other_answer):
        """
        Compare the answers of two persons.

        :param woman_answer: string containing woman answers
        :param man_answer: string containing man answers
        :return: number of matched answers
        """

        # the count of matched answers
        count = 0
        for index in range(0, len(answer)):
            if answer[index] == other_answer[index]:
                count += 1
        return count

    def make_match(self, names_women, answers_women, names_men, answers_men, query_woman):
        """
            Method

        :type self: object
        :param names_women:
        :param answers_women:
        :param names_men:
        :param answers_men:
        :param query_woman:
        """
        if query_woman not in names_women:
            print query_woman, "is not in list of women names"
            return

        if not self.__is_equal_size(names_women, answers_women):
            print "lists of women names and answers are not equal"
            return

        if not self.__is_equal_size(names_men, answers_men):
            print "lists of men names and answers are not equal"
            return

        if not self.__is_equal_size(names_men, names_women):
            print "lists of men and women names are not equal"
            return

        self.__set_names_and_answers_women(names_women, answers_women)
        self.__set_names_and_answers_men(names_men, answers_men)

        start_time = time.time()
        for woman in sorted(self.names_and_answers_women.keys()):

            men_match = {}
            for man in self.names_and_answers_men:
                men_match[man] = self.__compare_answers(self.names_and_answers_women[woman],
                                                        self.names_and_answers_men[man])

            max_count_value = max(men_match.values())
            matched_men_list = []
            for man in men_match:
                if men_match[man] == max_count_value:
                    matched_men_list.append(man)

            matched_men_list.sort()

            if woman == query_woman:
                print woman, "matches with", matched_men_list[0]

                del self.names_and_answers_women[woman]
                del self.names_and_answers_men[matched_men_list[0]]

                end_time = time.time()
                print "Elapsed Time:", start_time - end_time
                return

            del self.names_and_answers_women[woman]
            del self.names_and_answers_men[matched_men_list[0]]


names_women = ["Constance", "Alice", "Bertha", "Delilah", "Emily"]

answers_women = ["baabaa", "ababab", "aaabbb", "bababa", "baabba"]

names_men = ["Ed", "Duff", "Chip", "Abe", "Biff"]

answers_men = ["aabaab", "babbab", "bbbaaa", "abbbba", "abaaba"]

if __name__ == "__main__":
    match_maker = MatchMaker()
    match_maker.make_match(names_women, answers_women, names_men, answers_men, "Emily")
