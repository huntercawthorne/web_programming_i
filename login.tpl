<p>Login</p>
<form action="/login" method="POST">
<<<<<<< HEAD
    Username: <input type="text" size="100" maxlength="100" name="username"/><br>
    Password: <input type="text" size="100" maxlength="100" name="password"/><br>
=======
    User Name: <input type="text" size="100" maxlength="100" name="username"/><br>
    Password:  <input type="text" size="100" maxlength="100" name="password"/><br>
>>>>>>> 21696687a61c2083725d5abb03db46140a5e20f5
    <hr>
    Token: <input type="text" size="100" maxlength="100" name="csrf_token" value="{{csrf_token}}"/><br>
    <hr>
    <input type="submit" name="login" value="Login"/>
</form>