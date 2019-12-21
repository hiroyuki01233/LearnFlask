<script>
  const whitelist = ['intigriti.com','intigriti.io'];
  var url = new URL(location.hash.substr(1));{/*新しいURLをnew URLで作る、形 ["hoge", "url"] location.hashで「#」後の文字列を取得その中の最初の一文字を削っている*/}
  if(whitelist.indexOf(url.hostname) > -1){{/* whitelistの中の何個めにあるのか判定 new urlの中のhostnameをとってくる*/}
    document.write("Redirecting you to " + encodeURIComponent(url.href) + "...");
    window.setTimeout(function(){
      location = location.hash.substr(1);
    });
  }
  else{
    document.write(url.hostname + " is not a valid domain.")
  }
</script>