// ! categorical chart calculation

const catSumDiv = document
  .getElementById("categorical-table")
  .getElementsByTagName("div");

const cats = [];
const catSums = [];

for (let i = 0; i < catSumDiv.length; i++) {
  if (i % 2 == 0) {
    cats.push(catSumDiv[i].innerText);
  } else {
    catSums.push(catSumDiv[i].innerText.replace("$", "").replace(",", ""));
  }
}
const ctx = document.getElementById("expense-category");

new Chart(ctx, {
  type: "pie",
  data: {
    labels: cats,
    datasets: [
      {
        label: "Expense accross Category",
        data: catSums,
        backgroundColor: [
          "rgba(255, 99, 132, 0.2)",
          "rgba(54, 162, 235, 0.2)",
          "rgba(255, 206, 86, 0.2)",
          "rgba(75, 192, 192, 0.2)",
          "rgba(153, 102, 255, 0.2)",
          "rgba(255, 159, 64, 0.2)",
        ],
        borderColor: [
          "rgba(255, 99, 132, 1)",
          "rgba(54, 162, 235, 1)",
          "rgba(255, 206, 86, 1)",
          "rgba(75, 192, 192, 1)",
          "rgba(153, 102, 255, 1)",
          "rgba(255, 159, 64, 1)",
        ],
        borderWidth: 1,
      },
    ],
  },
});

// ! calculating daily expense sum
const dailySumDiv = document
  .getElementById("past-30-day-table")
  .getElementsByTagName("div");

console.log(dailySumDiv);
const dates = [];
const dailySums = [];

for (let i = dailySumDiv.length - 1; i >= 0; i--) {
  if (i % 2 == 0) {
    dates.push(dailySumDiv[i].innerText);
  } else {
    dailySums.push(dailySumDiv[i].innerText.replace("$", "").replace(",", ""));
  }
}

const ctx1 = document.getElementById("daily-expense");
new Chart(ctx1, {
  type: "line",
  data: {
    labels: dates,
    datasets: [
      {
        label: "Sum of daily Expenses",
        data: dailySums,
        backgroundColor: [
          "rgba(255, 99, 132, 0.2)",
          "rgba(54, 162, 235, 0.2)",
          "rgba(255, 206, 86, 0.2)",
          "rgba(75, 192, 192, 0.2)",
          "rgba(153, 102, 255, 0.2)",
          "rgba(255, 159, 64, 0.2)",
        ],
        borderColor: [
          "rgba(255, 99, 132, 1)",
          "rgba(54, 162, 235, 1)",
          "rgba(255, 206, 86, 1)",
          "rgba(75, 192, 192, 1)",
          "rgba(153, 102, 255, 1)",
          "rgba(255, 159, 64, 1)",
        ],
        borderWidth: 1,
      },
    ],
  },
  options: {
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  },
});
