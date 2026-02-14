class NumberUtils():

    @staticmethod
    def num_is_even(num):
        """Checks if the number is even"""
        if (num % 2) == 0:
            return True
    @staticmethod
    def num_is_prime(num):
        """Checks if the number is prime"""
        if num == 2 or num == 1:
            return True

        count = 0
        for i in range(2,num+1):
            if (num % i) == 0:
                count += 1
        if count != 1:
            return False
        elif count == 1:
            return True
        
if __name__ == '__main__':
    instance = NumberUtils()
    result = instance.num_is_prime(21)
    print(result)