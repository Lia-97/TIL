## Cafe Olleh Study (08.25)

#### login &register에 대해 주석을 달며 복습.

- login.html

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
		</script>
	{% endif %}

	<section class="h-100">
		<div class="container h-100">
			<div class="row justify-content-md-center h-100">
				<div class="card-wrapper">
					<div class="brand">
						<a href="{% url 'home' %}"><img src="/static/img/logo_login.png"></a>
					</div>
					<div class="card fat">
						<div class="card-body">
							<h4 class="card-title">Login</h4>
							<form method="POST" action="{% url 'usersapp:login' %}">
							   {% csrf_token %}
								<div class="form-group">
									<label for="email">E-Mail Address</label>
									<input id="email" type="email" class="form-control" name="email" value="" required autofocus>
								</div>

								<div class="form-group">
									<label for="password">Password
										<a href="{% url 'usersapp:forgot' %}" class="float-right" style="color:#4d3319;">
											Forgot Password?
										</a>
									</label>
									<input id="password" type="password" class="form-control" name="password" required data-eye>
								</div>

								<div class="form-group">
									<label>
										<input type="checkbox" name="remember"> Remember Me
									</label>
								</div>

								<div class="form-group no-margin">
									<button type="submit" class="btn btn-primary btn-block" style="background-color:#4d3319; border-color:#4d3319;">
										Login
									</button>
								</div>
								<div class="margin-top20 text-center">
									Don't have an account? <a href="{% url 'usersapp:register' %}" style="color:#4d3319;">Create One</a>
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

	<script src="/static/js/jquery.min.js"></script>
	<script src="/static/bootstrap/js/bootstrap.min.js"></script>
	<script src="/static/js/my-login.js"></script>
</body>
</html>
```

#server에게 /usersapp/login/페이지를 POST 방식으로 보내겠다. 근데 post 방식인 경우 보안 목적으로 csrf를 꼭 써줘야한다.



- views ---> def login

```python
def login(request):
    context = None
    if request.method == 'POST': 
        useremail = request.POST.get('email', None)
        password = request.POST.get('password', None)
        try:
            user = Users.objects.get(useremail=useremail)
        except Users.DoesNotExist:
            context = {'error': '아이디 또는 비밀번호가 일치하지 않습니다.'}
            return render(request,'login.html',context)
        else:
            user_name=user.username
            if check_password(password, user.password):
                request.session['user'] = user_name
                return redirect('/mainapp/home/')
            else:
                context = {'error': '아이디 또는 비밀번호가 일치하지 않습니다.'}
                return render(request, 'login.html', context)
    else:
        return render(request, 'login.html', context)

```

#POST방식으로 요청받으면, useremail에는 POST방식으로 받아온 input name이 email인 value값을 가져오고, 그 값이 없으면 오류가 아니라 None으로 처리한다.(하지만 input 방식이 required이기 때문에 입력 받은 값이 없을 수는 없다.)

#Users 클래스에 저장된 useremail 객체를 가져오는데, 그 useremail은 위에서 정의한 useremail이다.         Users 클래스의 모든 객체를 가져오려면 Users.objects.all()

#예외처리문 : get한 useremail이 Users 클래스에 저장된 객체가 아니라면, error 메세지를 login.html 파일과 함께 랜더링한다.(딕셔너리형태)

#입력한 비밀번호와 db에 등록된 user.password를 비교해서 같다면,  session에 user키의 value를 위에서 정의한 user_name으로 저장한다. 

#로그인에 성공했으면 /mainapp/home/으로 redirect

#먄약 입력한 비밀번호와 db에 등록된 password가 다르면 error메세지와 함께 다시 login.html을 랜더링한다.
#get방식일때는 login.html을 랜더링한다. 맨 처음 로그인 페이지에 접근했을 때 보여지는 화면.





- register.html

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
			alert("비밀번호 일치하지 않습니다.");
		</script>
	{% endif %}

	<section class="h-100">
		<div class="container h-100">
			<div class="row justify-content-md-center h-100">
				<div class="card-wrapper">
					<div class="brand">
						<a href="{% url 'home' %}"><img src="/static/img/logo_login.png"></a>
					</div>
					<div class="card fat">
						<div class="card-body">
							<h4 class="card-title">Register</h4>
							<form method="POST" action="{% url 'usersapp:register'%}">
								{% csrf_token %}
								<div class="form-group">
									<label for="name">Name</label>
									<input id="name" type="text" class="form-control" name="name" required autofocus>
								</div>

								<div class="form-group">
									<label for="email">E-Mail Address</label>
									<input id="email" type="email" class="form-control" name="email" required>
								</div>

								<div class="form-group">
									<label for="password">Password</label>
									<input id="password" type="password" class="form-control" name="password" required data-eye>
								</div>

								<div class="form-group">
									<label for="re-password">re-Password</label>
									<input id="re-password" type="password" class="form-control" name="re-password" required data-eye>
								</div>

								<div class="form-group">
									<label>
										<input type="checkbox" name="aggree" value="1"> I agree to the Terms and Conditions
									</label>
								</div>

								<div class="form-group no-margin">
									<button type="submit" class="btn btn-primary btn-block" style="background-color:#4d3319; border-color:#4d3319;">
										Register
									</button>
									<!--Register를 누르면 상단에 입력한 내용을 submit-->
								</div>
								<div class="margin-top20 text-center">
									Already have an account? <a href="{% url 'usersapp:login' %}" style="color:#4d3319;">Login</a>
								</div>
							</form>
						</div>
					</div>
					<div class="footer">
						Copyright &copy; Cafe Olleh 2020
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

#server에게 /usersapp/register/페이지를 POST 방식으로 보내겠다. 근데 post 방식인 경우 보안 목적으로 csrf를 꼭 써줘야한다.



- views ---> def register

```python
def register(request):
    if request.method =='GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        useremail = request.POST.get('email', None)
        username = request.POST.get('name', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)
        res_data={}
        if password != re_password:
            res_data['error']='비밀번호가 다릅니다.'
            return render(request, 'register.html', res_data)
        else:
            users = Users(
            useremail=useremail,
            username=username,
            password=make_password(password)
            )
            users.save()
            return render(request,'login.html')
```

#get방식이면 register.html을 렌더링한다. 처음 보여지는 등록 화면.

#POST방식으로 받아온 input name이 email인 value를 useremail에 저장한다.

#POST방식으로 받아온 input name이 name인 value를 username에 저장한다.

#POST방식으로 받아온 input name이 password인 value를 password에 저장한다.

#password가 re_paassword와 다르면, 비어있던 res_data 딕셔너리에 key는 error, value는 비번이 다릅니다를 저장하고,

#그 res_data를 담아서 register.html로 전달한다.

 #비밀번호와 재입력한 비밀번호가 일치하면, 상단에 정의된 useremail, username, password를 각각 Users 클래스에 저장한다.

#그리고 save를 해주고, login.html 렌더한다.

