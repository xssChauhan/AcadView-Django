
def like_view(request):
    data = request.POST
    post_id  = data.get('post_id')
    user_id = data.get('user_id')

    if post_id and user_id:
        if isinstance(post_id , int) and isinstance(user_id , int):
            #Do something
            post = PostModel.objects.get(pk = post_id)
            user = UserModel.objects.get(pk = user_id)
            if not post:
                return "Post Not Found"
            if not user:
                return "User Not Found"
            like = LikeModel(user = user , post = post)
            like.save()
            return render(request , "post.html")
        else:
            return "Invalid data sent"
    else:
        #Return Someerror
        if not post_id:
            return "Post Id not received"
        if not user_id:
            return  "User Id not received"