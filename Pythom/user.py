#user class
class User:
    def __init__(self, user_name, user_email, password, current_job_title ):
        self.name = user_name
        self.email = user_email
        self.password = password
        self.current_job_title = current_job_title
    

    def change_password(self, new_password):
        self.password = new_password
    
    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(f"User: {self.name} Works as a: {self.current_job_title}. email: {self.email}")


app_user_one = User("Mahmudul Hasan", "mahmudulrm@gmail.com", "pss123", "DevOps Engineer")
app_user_one.get_user_info()

app_user_one.change_job_title("IT")
app_user_one.get_user_info()