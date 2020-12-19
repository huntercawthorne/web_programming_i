<head>
<link href="https://www.w3schools.com/w3css/4/w3.css" rel="stylesheet" >
</head>
<body>
<hr>
{{str(session['username'])}}, welcome to your todo list!
<hr>
<u>Session Info</u>
<ul>
    <li><b>Username</b> - {{str(session['username'])}}</li>
    <li><b>ID</b> - {{str(session['id'])}}</li>
    <li><b>Session ID</b> - {{str(session['session_id'])}}</li>
    <li><b>Time</b> - {{str(session['time'])}}</li>
</ul>
</body>