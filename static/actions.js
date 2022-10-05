
function setresreactions(likes,dislikes){
    document.getElementById('like').innerHTML = likes
    document.getElementById('dislike').innerHTML = dislikes
}

function setcomment(comment){
    comments_html = document.getElementById('comments')
    new_comment = `<li>
        <p>${comment}</p>
        <i>${user_full_name}</i>
        </li>`
       comments_html.innerHTML += new_comment
    console.log(comment,comments_html.innerText)
}

function setreaction(id,react){
      url = `/reaction/${id}/${react}`
      request = new Request(
           url,
           {
               method: 'GET',
               headers: {'X-CSRFToken': csrftoken}
           }
      )
      fetch(request)
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          console.log(data);
          setresreactions(data.likes,data.dislikes)
        });
}

function send_comment(id){
    text = document.getElementById('comment').value
    console.log(text),
    url =  `/comment/${id}`
    request = new Request(
     url,
     {
        method: 'POST',
        headers: {'X-CSRFToken': csrftoken},
        body:JSON.stringify({
          'comment':text
        })
     }
    )
    fetch(request)
        .then((response) => {
          if (response.status == 201)
            setcomment(text)
        })
//        .then((data) => {
//          console.log(data);
//          setresreactions(data.likes,data.dislikes)
//        });
}