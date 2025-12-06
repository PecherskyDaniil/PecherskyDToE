

class log_levels:
    @staticmethod
    def LEVELS_RANK():
        return {
                log_levels.ERROR():1,
                log_levels.INFO():2,
                log_levels.DEBUG():3
                }
    @staticmethod
    def INFO():
        return "INFO"
    
    @staticmethod
    def DEBUG():
        return "DEBUG"
    
    @staticmethod
    def ERROR():
        return "ERROR"
    
    #@staticmethod
    #def LEVELS():
    #    result = []
    #    methods = [method for method in dir(log_levels) if
    #                callable(getattr(log_levels, method)) and not method.startswith('__') and method != "LEVELS"]
    #    for method in methods:
    #        key = getattr(log_levels, method)()
    #        result.append(key)
#
    #    return result