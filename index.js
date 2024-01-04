class Movie {
  constructor(title) {
    this.title = title;
  }

  setTitle(newTitle) {
    this.title = newTitle;
  }

  getTitle() {
    return this.title;
  }
}

document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("my-form");
  const movieList = document.getElementById("movieList");

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    console.log("Form submitted.");

    const title = document.getElementById("title").value;
    const movie = new Movie(title);

    // Make an AJAX request to the Flask server
    fetch("http://127.0.0.1:5000/get_movie_info", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ title: movie.getTitle() }),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Received data:", data);
        const li = document.createElement("li");
        li.textContent = `Title: ${data.title}, ID: ${data.id}`;
        movieList.appendChild(li);
      })
      .catch((error) => console.error("Error:", error));
  });
});
