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
    const date = document.getElementById("date").value;

    // Make an AJAX request to the Flask server
    fetch("http://127.0.0.1:5000/get_movie_info", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ title: title, date: date }),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Received data:", data);
        const li = document.createElement("li");
        li.textContent = `Title: ${data.title}, Budget: $${data.budget}`;
        movieList.appendChild(li);
      })
      .catch((error) => console.error("Error:", error));
  });
});
