class Movie {
  constructor(title, rating, yearReleased) {
    this.title = title;
    this.rating = rating;
    this.yearReleased = yearReleased;
  }

  setTitle(newTitle) {
    this.title = newTitle;
  }

  getTitle() {
    return this.title;
  }

  setRating(newRating) {
    this.rating = newRating;
  }

  getRating() {
    return this.rating;
  }

  setYearReleased(newYearReleased) {
    this.yearReleased = newYearReleased;
  }

  getYearReleased() {
    return this.yearReleased;
  }
}

document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("my-form");
  const movieList = document.getElementById("movieList");

  form.addEventListener("submit", function (e) {
    e.preventDefault();

    const title = document.getElementById("title").value;
    const rating = document.getElementById("Rating").value;
    const yearMade = document.getElementById("YearMade").value;

    const movie = new Movie(title, rating, yearMade);

    const li = document.createElement("li");
    li.textContent = `Title: ${movie.getTitle()}, Rating: ${movie.getRating()}, Year Made: ${movie.getYearReleased()}`;

    movieList.appendChild(li);

    // Clear the form inputs
    form.reset();
  });
});
