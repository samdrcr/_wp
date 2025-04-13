import { DB } from "https://deno.land/x/sqlite/mod.ts";

const db = new DB("my_blog.db");

db.query(`
  CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    content TEXT,
    user TEXT,
    time DATETIME DEFAULT CURRENT_TIMESTAMP
  )
`);

const posts = [
  {
    title: "Late night study session",
    content: "Can't sleep, might as well review biology. Exams are around the corner.",
    user: "By Mira",
  },
  {
    title: "Anyone up for group study?",
    content: "Looking for people to go over physics problems together. Library, 4pm?",
    user: "By Leo",
  },
  {
    title: "Snack recommendations?",
    content: "Need energy boosts while studying. What are your go-to snacks?",
    user: "By Sami",
  },
];

for (const post of posts) {
  db.query(
    "INSERT INTO posts (title, content, user) VALUES (?, ?, ?)",
    [post.title, post.content, post.user]
  );
}

for (
  const [id, title, content, user, time] of db.query(
    "SELECT id, title, content, user, time FROM posts"
  )
) {
  console.log(id, title, content, user, time);
}

db.close();
