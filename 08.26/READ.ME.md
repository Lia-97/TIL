## Cafe Olleh Study (08.26)

#### pwreset에 대해 주석을 달며 복습.

- pwreset.html

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="author" content="Kodinger">
	<title>My Login Page &mdash; Bootstrap 4 Login Page Snippet</title>
	<link rel="stylesheet" type="text/css" href="/static/bootstrap/css/bootstrap.min.css">
	<link rel="stylesheet" type="text/css" href="/static/css/my-login.css">
</head>
<body class="my-login-page">
	{% if error %}
		<script>
			alert("{{error}}");
			location.href="{% url 'usersapp:pwreset'%}?email="+"{{email}}";
		</script>
	{% endif%}
	<section class="h-100">
		<div class="container h-100">
			<div class="row justify-content-md-center align-items-center h-100">
				<div class="card-wrapper">
					<div class="brand">
						<a href="{% url 'home' %}"><img src="/static/img/logo_login.png"></a>
					</div>
					<div class="card fat">
						<div class="card-body">
							<h4 class="card-title">Reset Password</h4>
							<form method="POST" action="{% url 'usersapp:pwreset'%}?email={{email}}">
								{% csrf_token %}
								<div class="form-group">
									<label for="new-password">New Password</label>
									<input id="new-password" type="password" class="form-control" name="password" required autofocus data-eye>

									<label for="re-password">Re Password</label>
									<input id="re-password" type="password" class="form-control" name="re-password" required autofocus data-eye>
									<div class="form-text text-muted">
										Make sure your password is strong and easy to remember
									</div>
								</div>
								<div class="form-group no-margin">
									<button type="submit" class="btn btn-primary btn-block">
										Reset Password
									</button>
								</div>
							</form>
						</div>
					</div>
					<div class="footer">
						Copyright &copy; Your Company 2017
					</div>
				</div>
			</div>
		</div>
	</section>

	<script src="js/jquery.min.js"></script>
	<script src="bootstrap/js/bootstrap.min.js"></script>
	<script src="js/my-login.js"></script>
</body>
</html>
```



- views ---> pwreset

```python
def pwreset(request):
    if request.method == "POST":
        password=request.POST.get("password")
        re_password=request.POST.get("re-password")
        e = request.GET.get('email', "NotFound")
        if password != re_password:
            return render(request,'pwreset.html',context={"error":"비밀번호가 일치하지 않습니다.",'email':e})
        else:
            if e == "NotFound": return render(request,'/usersapp/forgot/',{'error':"변경할 이메일을 입력해 주세요."})
            user=Users.objects.get(useremail=e)
            user.password=make_password(password)
            user.save()
            return redirect("usersapp:login")
    else:
        e=request.GET.get('email',"NotFound")
        if e == "NotFound": return render(request, 'forgot.html', {'error': "변경할 이메일을 입력해 주세요."})
        return render(request, 'pwreset.html',{'email':request.GET['email']})
```

#get방식으로 가져온 query에 있는 email key가 없으면 forgot.html로 돌아가서 error 메세지 출력.

#query에 email key가 전달되면 pwreset.html 렌더.

#POST방식으로 전달되었을 때는 password와 re-password라는 변수에 각각 POST방식으로 get한 input의 value를 저장하고, 만약 password랑 re_password가 다르다면, pwreset.html을 렌더하는데, 이때 context에는 에러메세지와 쿼리문으로 전달되는 email이 있다.

#password와 re_password가 같은데, 쿼리문으로 전달되는 email을 찾을 수 없다면 usersapp/forgot/을 에러메세지와 렌더한다.

쿼리문으로 전달되는 email이 있으면,  그 email을 Users 클래스의 db에 저장하고, password도 Users 클래스의 db에 저장해서 save한다. 그리고 usersapp:login을 리다이렉트해서 로그인 가능하도록 한다.