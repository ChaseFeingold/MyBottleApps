<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Hello World In A Bottle</title>
<style type="text/css">
body {
    margin: 25px;
    padding: 25px;
}
main {
    border: 1px dotted #555;
}
h1 {
    padding: 15px;
    text-align: center;
    font-size: 3em;
    font-weight: bold;
}
p {
    text-align: center;
    font-size: 1.5em;
}
a, a:visited {
    color: #663;
    text-decoration: none;
}
footer {
    margin-top: 5px;
    text-align: center;
}
body {
 background-image:https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQDSdfKkeifrUcrPQB-fmqXpoR9QvJDzBdgk8_82MHa37BSIFIYTm4Fzto:https://pyxis.nymag.com/v1/imgs/f55/980/f57a2f1d6de4cbf768e5f97fb39f69caa7-dog-food-106-final.2x.rsocial.w600.jpg&s;
}
</style>
<script>
function add_validation_links() {
  var loc = window.location.href;
  var HTMLvalidLinkStr = 'http://validator.w3.org/check?uri=' + loc;
  var CSSvalidLinkStr = 'http://jigsaw.w3.org/css-validator/validator?uri=' +
                        loc + '?profile=css3';
  document.getElementById("vLink1").setAttribute("href", HTMLvalidLinkStr);
  document.getElementById("vLink2").setAttribute("href", CSSvalidLinkStr);
}
window.onload = add_validation_links;
</script>
</head>
<body>
<main>



</main>
<h1>What they eat</h1>
<h2> Dogs eat all sorts of stuff like meat, vegtables, penut butter, and even eggs.</h2>
<footer>
<a id="vLink1">
<strong> HTML </strong> Valid! </a> | 
<a id="vLink2">
<strong> CSS </strong> Valid! </a>
</footer>

</body>
</html>