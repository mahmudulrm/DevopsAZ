#import user
from user import User
from post import Post

app_user_one = User("Mahmudul Hasan", "mahmudulrm@gmail.com", "pss123", "DevOps Engineer")
app_user_one.get_user_info()

app_user_one.change_job_title("IT ss")
app_user_one.get_user_info()

new_post = Post("on a secret message", app_user_one.name)
new_post.get_post_info()
