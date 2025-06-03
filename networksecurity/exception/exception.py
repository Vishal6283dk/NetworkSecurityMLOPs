import sys
import os 


# Add the project root (2 levels up) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from networksecurity.logging import logger


class NetworkSecurityException(Exception):
    def __init__(self,error_message,error_details:sys):
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()
        
        self.lineno=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename 
    
    def __str__(self):
        return "Error occured in python Script Name [{0}] Line Number is [{1}] Error Message is [{2}]".format(
        self.file_name, self.lineno, str(self.error_message))
        
if __name__=='__main__':
    try:
        logger.logging.info("Entering the Try Block")
        a=1/0
        print("This will not be Printed",a)
    except ZeroDivisionError as e:
           raise NetworkSecurityException(e,sys)