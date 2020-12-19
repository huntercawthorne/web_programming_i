<head>
    <meta charset="utf-8">
    <title>Update Task</title>
</head>
<style>
body{
	margin: 0;
	padding: 0;
	font-family: sans-serif;
	background: #607d8b;
}

.box{
	width: 600px;
	padding: 40px;
	position: absolute;
	top: 50%;
	left: 50%;
	transform: translate(-50%,-50%);
	background: #191919;
	text-align: center;
}

.box h1{
	color: white;
	text-transform: uppercase;
	font-weight: 500;
}

.box input[type = "text"],.box input[type = "password"]{
	border: 0;
	background: none;
	display: block;
	margin: 1px auto;
	text-align: center;
	border: 2px solid #34495E;
	padding: 14px 10px;
	width: 500px;
	outline: none;
	color: white;
	border-radius: 24px;
	transition: 0.25s;
}

.box input[type = "text"]:focus,.box input[type = "password"]:focus{
	border-color: #3498DB;

}

.box input[type = "submit"]{
	border: 0;
	background: none;
	display: block;
	margin: 20px auto;
	text-align: center;
	border: 2px solid #009688;
	padding: 14px 40px;
	outline: none;
	color: white;
	border-radius: 24px;
	transition: 0.25s;
	cursor: pointer;
}

.box input[type = "submit"]:hover {
	background: #009688;
}


.box a.button {
	border: 0;
	background: none;
	display: block;
	margin: 20px auto;
	border: 2px solid #9E9E9E;
	padding: 14px 40px;
	outline: none;
	color: white;
	border-radius: 24px;
	transition: 0.25s;
	cursor: pointer;
	text-decoration: none;
	font-size: 13px;
	width: 70px;
}

.box a.button:hover {
	background: #9E9E9E;
	color: black;
}
</style>
<form class="box" action="/update_task" method="POST">
    <h1>Update Task</h1>
    <input type="hidden" type="text" size="100" maxlength="100" name="id" value="{{str(row['id'])}}"/>
    <input type="text" size="100" maxlength="100" name="updated_task" value="{{row['task']}}"/>
    <input type="submit" name="update_button" value="Update"/>
    <a href="/" class="button">Cancel</a>
</form>