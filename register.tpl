<!DOCTYPE html>
<html lang="en" dir="ltr">
    <head>
        <meta charset="utf-8">
        <title>Register</title>
        <link rel="stylesheet" type="text/css" href="/static/login.css">
    </head>

    <body>
        <form class="box" action="/register" method="POST">
            <h1>Create Your Account</h1>
            <p style="color:white;">Username:</p> <input type="text" size="100" maxlength="100" name="username"/><br>
            <p style="color:white;">Password:</p> <input type="text" size="100" maxlength="100" name="password"/><br>
            <input type="submit" name="register" value="Register"/>
            <input type="hidden" type="text" size="100" maxlength="100" name="csrf_token" value="{{csrf_token}}"/><br>
        </form>
    </body>
</html>