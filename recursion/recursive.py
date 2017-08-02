class recursion_solution:
    
    @staticmethod
    def sum(array):
        if len(array)>1:
            return array[0]+ recursion_solution.sum(array[1:])
        return array[0]
    
    @staticmethod
    def int2bin(num):
        if num > 1: return recursion_solution.int2bin(num//2) + str(num%2)
        return str(num)
    
    @staticmethod
    def reverse_string(string):
        if len(string)<1: return string
        return string[-1]+ recursion_solution.reverse_string(string[0:-1])
    