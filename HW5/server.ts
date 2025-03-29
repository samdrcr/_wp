import { Application } from "https://deno.land/x/oak/mod.ts";

const app = new Application();

app.use(async (ctx) => {
  console.log("Request URL:", ctx.request.url);
  let pathname = ctx.request.url.pathname;

  if (pathname === "/") {
    ctx.response.body = `
    <html>
    <head>
        <title>關於我</title>
        <link rel="stylesheet" href="/styles.css">
    </head>
    <body>
    <div class="container">
        <h1>歡迎來到我的個人介紹</h1>
        <ol>
            <li><a href="/name">姓名</a></li>
            <li><a href="/age">年齡</a></li>
            <li><a href="/gender">性別</a></li>
            <li><a href="/university">大學</a></li>
            <li><a href="/ID">學號</a></li>
        </ol>
    </div>
    </body>

    </html>
    `;
  } else if (pathname === "/name") {
    ctx.response.body = "范權榮";
  } else if (pathname === "/age") {
    ctx.response.body = "19";
  } else if (pathname === "/gender") {
    ctx.response.body = "男";
  } else if (pathname === "/university") {
    ctx.response.body = "國立金門大學";
  } else if (pathname === "/ID") {
    ctx.response.body = "111210557";
  } else if (pathname === "/styles.css") {
    ctx.response.headers.set("Content-Type", "text/css");
    ctx.response.body = await Deno.readTextFile("styles.css"); 
  } else {
    ctx.response.status = 404;
    ctx.response.body = "Page Not Found!";
  }
});

console.log("Server running at: http://127.0.0.1:8000");
await app.listen({ port: 8000 });
