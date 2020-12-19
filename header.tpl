<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
</head>
<style>
.w3-bar, .title {
background: #3D3D3D;
margin: none;
}
</style>
<div class="title">
<h3 class="w3-center w3-padding-16">{{str(session['username'])}}'s To-do List</h3>
</div>
<div class="w3-bar">
  <a href="/login"><button class="w3-bar-item w3-button">Login</button></a>
  <a href="/logout"><button class="w3-bar-item w3-button">Logout</button></a>
  <a href="/new_item"><button class="w3-bar-item w3-button">New item...</button></a>
</div>