<html>
<head>
<title>Todo List 0.001</title>
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet"/>
<link href="https://www.w3schools.com/w3css/4/w3.css" rel="stylesheet" >
</head>
<div class="w3-blue-grey">
<body>
%include("header.tpl", session=session)
<div class="table">
<table class="w3-table w3-bordered w3-border w3-grey">
%for row in rows:
    <tr>
        <td>
            <a href="/update_task/{{row['id']}}"><i class="material-icons">edit</i></a>
        </td>
        <td>
            {{row['task']}}
        </td>
        <td>
        %if row['status']==0:
            <a href="/update_status/{{row['id']}}/1"><i class="material-icons">check_box_outline_blank</i></a>
        %else:
            <a href="/update_status/{{row['id']}}/0"><i class="material-icons">check_box</i></a>
        %end
        </td>
        <td>
            <a href="/delete_item/{{row['id']}}"><i class="material-icons">delete</i></a>
        </td>
        <td>
            Added by: {{session['username']}}
        </td>
    </tr>
%end
</table>
</div>
%include("footer.tpl", session=session)
</body>
</div>
</html>