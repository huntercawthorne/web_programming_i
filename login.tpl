<!DOCTYPE html>
<html lang="en" dir="ltr">
    <head>
        <meta charset="utf-8">
        <title>Login</title>
        <link rel="stylesheet" type="text/css" href="/static/login.css">
    </head>

    <body>
        <form class="box" action="/login" method="POST">
            <h1>To-Do List Login</h1>
            <input type="text" size="100" maxlength="100" name="username" placeholder="Username" required/><br>
            <input type="password" size="100" maxlength="100" name="password" placeholder="Password" required/><br>
            <input type="submit" name="login" value="Login"/>
            <a href="/register" class="button">Create Account</a>
            <span class="password"><a class="Forgot" href="/forgot_password">Forgot password?</a></span>
            <input type="hidden" type="text" size="100" maxlength="100" name="csrf_token" value="{{csrf_token}}"/><br>
        </form>
    </body>
</html>