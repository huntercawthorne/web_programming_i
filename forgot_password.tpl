<!DOCTYPE html>
<html lang="en" dir="ltr">
    <head>
        <meta charset="utf-8">
        <title>Forgot Password</title>
        <link rel="stylesheet" type="text/css" href="/static/login.css">
    </head>

    <body>
        <form class="box" action="/forgot_password" method="POST">
            <h1>Forgot Your Password?</h1>
            <p style="color:white;">What's your username?</p> <input type="text" size="100" maxlength="100" name="username" required/><br>
            <p style="color:white;">Enter your new password:</p> <input type="text" size="100" maxlength="100" name="password" required/><br>
            <input type="submit" name="register" value="Submit"/>
            <input type="hidden" type="text" size="100" maxlength="100" name="csrf_token" value="{{csrf_token}}"/><br>
        </form>
    </body>

</html>