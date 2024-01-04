// class Movie {
//   constructor(title) {
//     this.title = title;
//   }

//   setTitle(newTitle) {
//     this.title = newTitle;
//   }

//   getTitle() {
//     return this.title;
//   }
// }

// document.addEventListener("DOMContentLoaded", function () {
//   const form = document.getElementById("my-form");
//   const movieList = document.getElementById("movieList");

//   form.addEventListener("submit", async function (e) {
//     e.preventDefault();

//     const title = document.getElementById("title").value;

//     const movie = new Movie(title);

//     // Make an HTTP request to the Python server
//     const response = await fetch("http://localhost:5000/scrape", {
//       method: "POST",
//       headers: {
//         "Content-Type": "application/json",
//       },
//       body: JSON.stringify({ title: movie.getTitle() }),
//     });

//     if (response.ok) {
//       const movieDetails = await response.json();
//       const li = document.createElement("li");
//       li.textContent = `Title: ${movieDetails.title}, Rating: ${movieDetails.rating}, Year: ${movieDetails.yearReleased}`;
//       movieList.appendChild(li);
//     } else {
//       console.error("Failed to retrieve movie details");
//     }

//     // Clear the form inputs
//     form.reset();
//   });
// });

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

    const title = document.getElementById("title").value;
    const movie = new Movie(title);

    const li = document.createElement("li");
    li.textContent = `Title: ${movie.getTitle()}`;

    movieList.appendChild(li);

    // Make an AJAX request to your Python script
    const xhr = new XMLHttpRequest();
    xhr.open(
      "GET",
      `http://127.0.0.1:5000/get_movie_details?title=${title}`,
      true
    );
    xhr.onreadystatechange = function () {
      if (xhr.readyState == 4 && xhr.status == 200) {
        const response = JSON.parse(xhr.responseText);
        console.log(response); // You can handle the response here
      }
    };
    xhr.send();

    // Clear the form inputs
    form.reset();
  });
});
