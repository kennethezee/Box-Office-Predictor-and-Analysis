interface Post {
  id: number;
  title: string;
  body: string;
}

export default async function Server() {
  const res = await fetch('https://api.themoviedb.org/3/movie/11');
  const posts: Post[] = await res.json();

  return (
    <ul>
      {posts.map(post => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  );
}