<html>
<head>
<<<<<<< HEAD
    <title>Ajax Demo Page</title>
    <script>
    function onLoad() {
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                content = this.responseText;
                document.getElementById("my_text").innerHTML = content;
            }
        }
        xhttp.open("GET", "http://dev-web-hcawthor.pythonanywhere.com/static/data.txt", true);
        xhttp.send();
    };
    </script>
=======
  <title>Ajax Demo Page</title>
  <script>
  function onLoad() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            content = this.responseText;
            document.getElementById("my_text").innerHTML = content;
        }
    }
    console.log("sending request");
    xhttp.open("GET", "http://dev-web-drdelozier.pythonanywhere.com/static/data.txt", true);
    xhttp.send();
  };
  </script>
>>>>>>> 21696687a61c2083725d5abb03db46140a5e20f5
</head>
<body onload='onLoad();'>
Hello from the sandbox.
<hr/>
<div id="my_text"></div>
<hr/>
</body>
</html>