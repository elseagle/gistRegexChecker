
from helpers import github



class Worker:
    def __init__(self, number_of_gists, list_of_regex):
        self.list_of_regex = list_of_regex
        self.number_of_gists = number_of_gists


    def run(self):
        # do the main function here
        response = github(self.number_of_gists, self.list_of_regex)
        if response is None:
            return 'Regex not found'
        return WorkerResponse(data=response)




class WorkerResponse:
    def __init__(self, data):
        self.data = data


#Test
match_patterns = ['let', 'const', 'int', 'class', 'print', 'var']
my_worker = Worker(50, match_patterns)
if __name__ == '__main__':

    my_worker_response = my_worker.run()
    print(my_worker_response.data)


