/**

function deleteNote(noteId){
    fetch('/delete-note', {
        method: 'POST',
        body: JSON.stringify({ noteId: noteId })
    }).then((_res) => {
        window.location.href = "/";
    })
}

**/

$(document).ready(function () {

    $(".nav-link").hover(
        function(){
            // Action to perform when mouse enters
            $(this).css("background-color", "#FF5F1F");
        },
        function(){
            // Action to perform when mouse leaves
            $(this).css("background-color", ""); // Reset background color
        }
    );

})