import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=r'C:/Users/A4003/PycharmProjects/pythonProject/Logs/automation.log',
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                            force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
