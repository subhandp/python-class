from time import strftime

class Log:
    def write(type,message):
        date = strftime("%Y-%m-%dT%H:%M:%S.%SZ")
        f = open("app.log", "a")
        f.write(f"[{date}] {type}: {message}\n")
        f.close()
    
    def info(self,message):
        Log.write("INFO",message)
    
    def error(self,message):
        Log.write("ERROR",message)
    
    def notice(self,message):
        Log.write("NOTICE",message)
    
    def warning(self,message):
        Log.write("WARNING",message)
    
    def debug(self,message):
        Log.write("DEBUG",message)
    
    def alert(self,message):
        Log.write("ALERT",message)
    
    def critical(self,message):
        Log.write("CRITICAL",message)
    
    def emergency(self,message):
        Log.write("EMERGENCY",message)

log = Log()
log.error("We can't divide any numbers by zero.")
log.info("This is an information about something.")
log.notice("Someone loves your status.")
log.warning("Insufficient funds.")
log.debug("This is debug message.")
log.alert("Achtung! Achtung!")
log.critical("Medic!! We've got critical damages.")
log.emergency("System hung. Contact system administrator immediately!")